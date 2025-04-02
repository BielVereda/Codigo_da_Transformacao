from flask import Flask

app = Flask(__name__)

@app.route('/saudacao/<nome>')

def saudacao(nome):
    return f"Olá, {nome}!"

if __name__ == '__main__':
    app.run(debug=True)