# 📘 Atividade: Criando uma API REST Calculadora com Flask

## 🎯 Objetivo
Nesta atividade, você vai aprender a:
- Criar uma aplicação **Flask** básica.  
- Usar o **`render_template`** para renderizar páginas HTML.  
- Implementar **rotas** que recebem parâmetros pela URL.  
- Retornar resultados em **formato JSON**.

---

## 🚀 Instruções

### 1. Estrutura inicial
Você já tem o arquivo `app.py` com o seguinte código:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### 2. Criando a página inicial
Crie a pasta `templates/` e dentro dela o arquivo `index.html`.  
Esse arquivo será exibido quando acessarmos a rota **`/`**.

👉 Dica: coloque um título e explique como usar a API.  
Exemplo:
```html
<h1>API Calculadora</h1>
<p>Use as rotas para somar, subtrair, multiplicar e dividir valores.</p>
```

---

### 3. Criando as rotas da calculadora
Agora você deve criar **4 rotas GET** que recebem parâmetros pela URL e retornam um JSON com o resultado:

- `/soma?valor1=5&valor2=6`  
- `/subtrair?valor1=5&valor2=6`  
- `/multiplicar?valor1=5&valor2=6`  
- `/dividir?valor1=5&valor2=6`

👉 Dicas:
- Use `request.args.get("valor1")` para pegar o parâmetro da URL.  
- Converta para número com `float()`.  
- Retorne o resultado como dicionário Python (o Flask converte automaticamente para JSON).  

Exemplo:
```python
@app.route("/soma")
def soma():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    return {"resultado": v1 + v2}
```

---

### 4. Tratando erros
Na divisão, tome cuidado com divisão por zero.  
👉 Dica: use um `if` para verificar e retorne uma mensagem de erro, por exemplo:
```python
if v2 == 0:
    return {"erro": "Divisão por zero não é permitida"}
```

---

## 📌 Tarefas [Checklist]
- [ ] Criar `index.html` dentro da pasta `templates/`.  
- [ ] Implementar rota `/soma`.  
- [ ] Implementar rota `/subtrair`.  
- [ ] Implementar rota `/multiplicar`.  
- [ ] Implementar rota `/dividir` (tratando divisão por zero).  
- [ ] Testar as rotas no navegador ou no **Postman/Insomnia**.  

---

## 🧪 Testando
Depois de rodar o projeto (`python app.py`), abra no navegador:

- [http://127.0.0.1:5000/soma?valor1=10&valor2=20](http://127.0.0.1:5000/soma?valor1=10&valor2=20)  
Deve retornar:
```json
{"resultado": 30.0}
```

---

## 💡 Desafios Extras (opcional)
1. Adicione um **formulário HTML** na página inicial para testar a calculadora.  
2. Crie uma rota `/tudo` que retorne todas as operações de uma vez só (soma, subtração, multiplicação e divisão).  
3. Melhore o visual da página inicial com **Bootstrap**.  

---

👉 Agora é com você: siga o passo a passo e construa sua primeira API REST!  
