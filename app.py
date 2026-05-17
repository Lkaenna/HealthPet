#Iniciando o flask e conectando o banco de dados

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthypet.db'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

from routes import *
from models import *

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)