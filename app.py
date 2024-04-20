from flask import Flask, request, render_template

app = Flask(__name__)

def binario_para_decimal(binario):
    return int(binario, 2)

def decimal_para_binario(decimal):
    return bin(decimal)[2:]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    operacao = request.form['operacao']
    num1 = request.form['num1']
    num2 = request.form['num2']

    decimal1 = binario_para_decimal(num1)
    decimal2 = binario_para_decimal(num2)

    if operacao == 'soma':
        resultado = decimal_para_binario(decimal1 + decimal2)
    elif operacao == 'subtracao':
        resultado = decimal_para_binario(decimal1 - decimal2)
    elif operacao == 'multiplicacao':
        resultado = decimal_para_binario(decimal1 * decimal2)
    else:
        resultado = "Operação inválida"

    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
