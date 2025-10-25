from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.
@app.route('/soma')
def soma():
    v1=float(request.args.get('valor1',0))
    v2=float(request.args.get('valor2',0))
    return{'resultado':v1 +v2}

@app.route('/subtrair')
def subtrair():
    v1=float(request.args.get('valor1',0))
    v2=float(request.args.get('valor2',0))
    return{'resultado':v1 -v2}

@app.route('/mutiplicar')
def mutiplicar():
    v1=float(request.args.get('valor1',0))
    v2=float(request.args.get('valor2',0))
    return{'resultado':v1 * v2}

@app.route('/dividir')
def dividir():
    v1=float(request.args.get('valor1',0))
    v2=float(request.args.get('valor2',0))
    if v2 == 0:
        return{'erro':'Operação não permitida.'}
    return{'resultado': v1/v2}
    

if __name__ == "__main__":
    app.run(debug=True)
