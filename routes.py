#Configurando aas paginas e as acoes

from app import app, db
from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from models import User

@app.route("/register", methods=["GET", "POST"])

def register():

    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        user_existente = User.query.filter_by(email=email).first()

        if user_existente:
            return "Email já cadastrado."
        
        senha_hash = generate_password_hash(senha)

        novo_user = User(
            nome=nome,
            email=email,
            senha_hash=senha_hash
        )

        db.session.add(novo_user)
        db.session.commit()

        return "Conta criada com sucesso!"
    return render_template('register.html')
