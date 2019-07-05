#coding:utf-8

from flask import Flask

app = Flask(__name__)

@app.route("/")
def fistApp():
	return "<h1>Minha primeira Aplicação feita em Flask!</h1>"


	if __name__ == "__main__":
		app.run()

