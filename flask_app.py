from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# cONFIGURAR O BANCO DE DADOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://bancoDeDados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# terminou a configuração de banco de dados

# criacao de modelo para o registro do ususario



class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(15), nullable=False)
    sobrenome = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    assunto = db.Column(db.String(25), nullable=False)
    mensagem = db.Column(db.String(250), nullable=False)
    hora = db.Column(db.DateTime, default=datetime.now)



@app.route('/contato')
def inicio():
    return render_template('morrendo.html')

# Para rodar o projeto em desenvolvimento
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
