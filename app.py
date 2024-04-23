from flask import Flask, request, render_template

erro = 'Erro: Inserir somente números binários!'

app = Flask(__name__)

def binario_para_decimal(binario):
    return int(binario, 2)

def decimal_para_binario(decimal):
    if decimal < 0:
        return '-' + bin(abs(decimal))[2:]
    else:
        return bin(decimal)[2:]

def soma_binaria(binario1, binario2):
    decimal1 = binario_para_decimal(binario1)
    decimal2 = binario_para_decimal(binario2)
    resultado_decimal = decimal1 + decimal2
    return decimal_para_binario(resultado_decimal)

def subtracao_binaria(binario1, binario2):
    decimal1 = binario_para_decimal(binario1)
    decimal2 = binario_para_decimal(binario2)
    resultado_decimal = decimal1 - decimal2
    return decimal_para_binario(resultado_decimal)

def multiplicacao_binaria(binario1, binario2):
    decimal1 = binario_para_decimal(binario1)
    decimal2 = binario_para_decimal(binario2)
    resultado_decimal = decimal1 * decimal2
    return decimal_para_binario(resultado_decimal)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        operacao = request.form['operacao']
        num1 = request.form['num1']
        num2 = request.form['num2']

        if operacao == 'soma':
            resultado = soma_binaria(num1, num2)
        elif operacao == 'subtracao':
            resultado = subtracao_binaria(num1, num2)
        elif operacao == 'multiplicacao':
            resultado = multiplicacao_binaria(num1, num2)
        else:
            resultado = "Operação inválida"

        return render_template('index.html', resultado=resultado)
    except:
        return render_template('index.html', resultado=erro)
if __name__ == '__main__':
    app.run(debug=True)
