import pymysql
from utils.format_client import formatter

conn = pymysql.connect(
    user='root',
    password='',
    autocommit=True
)

cur = conn.cursor()

# inicializando banco de dados
cur.execute('CREATE DATABASE IF NOT EXISTS APIAgendamento')
cur.execute('USE APIAgendamento')
cur.execute('CREATE TABLE IF NOT EXISTS clientes(phone_number varchar(13) primary key, name varchar(40), local varchar(70), state char(2), scheduled_to datetime)')

class APIDatabase:
    def add_client(self, client_info: dict):
        """Adiciona um novo cliente
        ao banco de dados com suas
        informações.

        Args:
            client_info (dict): Todas as informações
            necessárias para o agendamento
        """

        #
        # Se o cliente já existir, o cadastro
        # não será realizado e False é
        # retornado. Caso contrário,
        # o cliente será adicionado
        # e True é retornado. 
        #

        has_exist_client = self.get_client(client_info['phone_number'])

        if has_exist_client:
            return False

        cur.execute('INSERT INTO clientes values(%s, %s, %s, %s, %s)',
                    (client_info['phone_number'], client_info['name'],
                    client_info['local'], client_info['state'],
                    client_info['scheduled_to']))

        return True


    def get_client(self, phone_number: str):
        """Obtém um cliente que
        já fez (ou não) um agendamento na base
        de dados.

        Args:
            phone_number (str): Número utilizado
            no agendamento.
        """

        #
        # Para identificar agendamentos já
        # realizados pelo usuário, será
        # solicitado seu número de telefone
        # para a verificação, caso exista,
        # as informações do agendamento são
        # retornadas.
        # 
        # se o usuário não comparecer após 5
        # minutos de atraso, o agendamento é
        # cancelado. 
        #

        cur.execute('SELECT * FROM clientes WHERE phone_number = %s', (phone_number, ))
        client_data = cur.fetchone()

        if client_data is None:
            client_info = False
        else:
            client_info = formatter(client_data)


        return client_info


# Código para testes

# app = APIDatabase()

# cliente = {
#     'name': 'Jaedson', 'local': 'Centro',
#     'phone_number': '994193546', 'state': 'AL',
#     'scheduled_to': '2021-12-03 12:30:00'
# }
# app.add_client(cliente)

# print(app.get_client('994193546'))