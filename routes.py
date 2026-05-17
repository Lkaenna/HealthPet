#Configurando aas paginas e as acoes

from app import app, db
from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
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

@app.route("/login", methods=["GET", "POST"])

def login():

    if request.method == "POST":
         email = request.form['email']
         senha = request.form['senha']

         user = User.query.filter_by(email=email).first()

         if user and check_password_hash(user.senha_hash, senha):
             return "Login realizado com sucesso!"
         return 'Email ou senha inválidos'
    
    return render_template('login.html')

