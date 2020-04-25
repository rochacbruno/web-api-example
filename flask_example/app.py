from flask import Flask, request

dados = {"canal": "LinuxTips", "msg": "Vaiiii!"}

app = Flask("app")

@app.route("/")
def linuxtips():
    return dados

@app.route("/hello/<nome>/")
def hello(nome):
    return f"<h1>Hello {nome} - {request.args['msg']}</h1>"