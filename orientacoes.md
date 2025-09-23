# Sugestões para Discussão entre Professores

- Discutir a clareza das instruções para os alunos, especialmente nos pontos marcados como [TAREFA].
- Avaliar se o nível de dificuldade está adequado para o objetivo da avaliação.
- Sugerir exemplos práticos ou casos de uso para enriquecer a atividade.
- Considerar a inclusão de testes automatizados para facilitar a correção.


# Parte 1 – Modelagem e Criação da Tabela 'users'

Você receberá o **diagrama** da tabela 'users' e deverá **implementar a criação da tabela** de uma das formas abaixo:

- **Opção A (linha de comando do SQLite)**  
- **Opção B (função em Python usando `sqlite3`)**

> Use **apenas uma** das opções para concluir esta parte.

---

# Parte 2 – Complete o Código no Flask

Nesta parte, você encontrará **trechos de código incompletos** no arquivo `app.py`.  
Sua tarefa é completar os pontos marcados com **[TAREFA]**.

---

## 1. Coleta dos Dados no Cadastro

Trecho no `/register`:

```python
if request.method == "POST":
    nome = request.form.get("[TAREFA-1]", "").strip()
    email = request.form.get("[TAREFA-2]", "").strip().lower()
    senha = request.form.get("[TAREFA-3]", "")

[TAREFA-1] complete com o nome do campo do formulário de cadastro.

[TAREFA-2] complete com o nome do campo de e-mail.

[TAREFA-3] complete com o nome do campo de senha.

## 2. Consulta do Usuário no Login

Trecho no /login:

with get_conn() as conn:
    cur = conn.execute("SELECT * FROM users WHERE [TAREFA-4] = ?", ([TAREFA-5],))
    user = cur.fetchone()


[TAREFA-4] complete com o nome da coluna correta da tabela.

[TAREFA-5] complete com a variável que guarda o valor do e-mail digitado no formulário.


## 3. Inserção de Usuário

Trecho ao cadastrar:

conn.execute(
    "INSERT INTO users (nome, email, senha, criado_em) VALUES (?, ?, ?, ?)",
    ([TAREFA-6], [TAREFA-7], [TAREFA-8], criado_em),
)


[TAREFA-6] complete com a variável que guarda o nome digitado.

[TAREFA-7] complete com a variável que guarda o e-mail digitado.

[TAREFA-8] complete com a variável que guarda a senha digitada.
---

