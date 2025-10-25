
"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""

import sqlite3

# Passo 1 : Conectar/criar um banco de dados
conn= sqlite3.connect('escola.db')
cursor = conn.cursor()

# Passo 2 : Criar Tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL, 
    idade INTEGER,
    email TEXT                                 
    )''')

print('Tabela criada com sucesso!\n')

# Passo 3 : Inserir dados
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Bianca',17,'bia@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Fernanda',23,'fê@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Thiago',21,'Thiago3@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Samuel',18,'Samuka18@gmail.com'))
conn.commit()
print('Dados gravados sem problemas encontrados!\n')

# Passo 4 : Listar todos
print('Lista de alunos cadastrados:')
cursor.execute('SELECT * FROM alunos') 
for linha in cursor.fetchall():
    print(linha)
print()
# Se não quiser duplicar os nomes, colocar # para comentar tudo no Passo 3

# Passo 5 : atualizar um registros
cursor.execute('UPDATE  alunos SET email = ? WHERE id = ?'
               ,('Thiaguinho9@gmail.com', 7))
conn.commit()
print('após atualização do email do Thiago:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Passo 6 : Deletar um registro
cursor.execute('DELETE FROM alunos WHERE id= ?',(8,))
conn.commit()
print('após deletar o id 8:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Encerrar a conexão 
conn.close()


