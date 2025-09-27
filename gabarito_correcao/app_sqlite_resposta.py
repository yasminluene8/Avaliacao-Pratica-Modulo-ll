import sqlite3

# Passo 1 - Conectar/criar o banco
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# Passo 2 - Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT
)
""")

print("Tabela criada com sucesso!\n")

# Passo 3 - Inserir dados
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)",
               ("Ana", 20, "ana@example.com"))
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)",
               ("Bruno", 22, "bruno@example.com"))
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)",
               ("Carla", 19, "carla@example.com"))
conn.commit()

print("Dados inseridos!\n")

# Passo 4 - Listar todos
print("Lista de alunos cadastrados:")
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)
print()

# Passo 5 - Atualizar um registro
cursor.execute("UPDATE alunos SET email = ? WHERE nome = ?",
               ("bruno.dev@example.com", "Bruno"))
conn.commit()

print("Após atualização do email do Bruno:")
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)
print()

# Passo 6 - Deletar um registro
cursor.execute("DELETE FROM alunos WHERE nome = ?", ("Carla",))
conn.commit()

print("Após deletar Carla:")
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)
print()

# Encerrar conexão
conn.close()