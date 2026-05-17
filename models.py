#Definindo o banco de dados
from app import db

class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable = False
    )

    email = db.Column(
        db.String(100), 
        unique = True,
        nullable = False
    )

    senha_hash = db.Column(
        db.String(100),
        nullable = False
    )
            

