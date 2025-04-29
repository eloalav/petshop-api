import jwt
import os
from datetime import datetime, timedelta
from flask import request, jsonify

from main import app

# Chave secreta para encriptação (ideal usar variável de ambiente em produção)
SECRET_KEY = os.getenv("SECRET_KEY", "sua-chave-super-secreta")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify(message="Dados de login não fornecidos!"), 400
    if "username" not in data or "password" not in data:
        return jsonify(message="Campos 'username' e 'password' são obrigatórios!"), 400
    if data["username"] == "admin" and data["password"] == "123":
        # Gerar o token com expiração
        token = jwt.encode(
            {"user": data["username"], "exp": datetime.utcnow() + timedelta(minutes=30)},
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify(token=token)

    return jsonify(message="Credenciais inválidas!"), 401