# def formatter_client(info: dict):
#     """Formata as informações de
#     clientes.

#     Args:
#         info (dict): Informações
#         do banco de dados para
#         formatação
#     """

#     # has_multiple_customers = True if len(dict) > 1 else False
#     multiple_customers = list()

#     for client in info:
#         info_client_formated = formatter(client)
#         multiple_customers.append(info_client_formated)

#     return multiple_customers


def formatter(info_client: tuple):
    #
    # Essa é a ordem para definir os valores
    # das chaves:
    # 
    # Nome, local, número de telefone, estado
    #

    client = dict()
    keys = ['phone_number', 'name', 'local', 'state', 'scheduled_to']

    for i, k in zip(info_client, keys):
        client[k] = i
    
    return client