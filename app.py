from flask import Flask
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)

class Agendamento(Resource):
    def get():
        """O método GET retornará
        todos os dias ocupados e livres, com a intenção
        de validar agendamentos e mostrar ao usuário
        os dias que estão livres
        """

    def post(self):
        """O método POST criará um novo agendamento
        caso não exista nenhum outro agendamento marcado
        30 minutos antes
        """


if __name__ == '__main__':
    app.run(debug=True, port=3000)