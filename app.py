from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev-secret"  # Trocar em produção

DB_NAME = "app.db"

# Conexão simples: abre, configura row_factory e retorna
def get_conn():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # permite user["campo"]
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                criado_em TEXT NOT NULL
            );
        """)
        conn.commit()

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        # Validação simples
        if not nome or not email or not senha:
            flash("Preencha todos os campos.", "warning")
            return render_template("registrar.html")

        # Verifica se email já existe
        with get_conn() as conn:
            cur = conn.execute("SELECT id FROM users WHERE email = ?", (email,))
            if cur.fetchone():
                flash("Este e-mail já está cadastrado.", "danger")
                return render_template("registrar.html")

            # Persiste
            criado_em = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn.execute(
                "INSERT INTO users (nome, email, senha, criado_em) VALUES (?, ?, ?, ?)",
                (nome, email, senha, criado_em),
            )
            conn.commit()

        flash("Cadastro realizado! Faça login.", "success")
        return redirect(url_for("login"))

    return render_template("registrar.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        # Busca usuário por e-mail
        with get_conn() as conn:
            cur = conn.execute("SELECT * FROM users WHERE email = ?", (email,))
            user = cur.fetchone()

        if not user or user["senha"] != senha:
            flash("Credenciais inválidas.", "danger")
            return render_template("login.html")

        # Guarda info mínima na sessão
        session["user_id"] = user["id"]
        session["user_nome"] = user["nome"]
        return redirect(url_for("perfil"))

    return render_template("login.html")

@app.route("/perfil")
def perfil():
    if "user_id" not in session:
        flash("Faça login para acessar.", "warning")
        return redirect(url_for("login"))

    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM users WHERE id = ?", (session["user_id"],))
        user = cur.fetchone()

    # Se usuário não existir mais (caso raro), limpa sessão
    if not user:
        session.clear()
        flash("Sessão inválida. Faça login novamente.", "warning")
        return redirect(url_for("login"))

    return render_template("perfil.html", user=user)

@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sessão.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    if not os.path.exists(DB_NAME):
        init_db()
    app.run(debug=True)