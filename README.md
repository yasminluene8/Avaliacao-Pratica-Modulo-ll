# 📘 Avaliação 1. Criando uma API REST Calculadora com Flask

## 🎯 Critérios de Correção
- Criar uma aplicação **Flask** básica.  
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

### 2. Criando as rotas da calculadora
Agora você deve criar **4 rotas GET** que recebem parâmetros pela URL e retornam um JSON com o resultado:

- `/soma?valor1=5&valor2=6`  
- `/subtrair?valor1=5&valor2=6`  
- `/multiplicar?valor1=5&valor2=6`  
- `/dividir?valor1=5&valor2=6`

👉 Dicas:
- Use `request.args.get("valor1")` para pegar o parâmetro da URL.  
- Converta para número com `float()`.  
- Retorne o resultado como dicionário Python (o Flask converte automaticamente para JSON).  

---

### 3. Tratando erros
Na divisão, tome cuidado com divisão por zero.  
👉 Dica: use um `if` para verificar e retorne uma mensagem de erro, por exemplo:
```python
if v2 == 0:
    return {"erro": "Divisão por zero não é permitida"}
```

---

## 📌 Tarefas [Checklist]
- [ ] Implementar rota `/soma`.  
- [ ] Implementar rota `/subtrair`.  
- [ ] Implementar rota `/multiplicar`.  
- [ ] Implementar rota `/dividir` (tratando divisão por zero).  
- [ ] Testar as rotas no navegador ou no **Postman/requests**.  

---

## 🧪 Testando
Depois de rodar o projeto (`python app.py`), abra no navegador:

- [http://127.0.0.1:5000/soma?valor1=10&valor2=20]
Deve retornar:
```json
{"resultado": 30.0}
```

