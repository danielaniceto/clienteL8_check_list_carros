import logging
from uuid import uuid4, UUID
from database.mongo import DataBaseConnection
from schemas.checklistschema import CheckListSchema

service_db = DataBaseConnection.is_connction_db()["campos_check_list_carro"]

class CheckListController:
    def __init__(self):
        logging.info("LoginController initialized")

    async def is_check_list_car(self, data: CheckListSchema):
        logging.info("Novo processo de check list recebido")

        identificador = str(uuid4().hex)

        check_list = {
            "uuid_check_list": identificador,
            "placa_carro": data.placa_carro,
            "nome_completo": data.nome_completo,
            "trecho": data.trecho,
            "data_ultima_manutencao": data.data_ultima_manutencao,
            "hodometro": data.hodometro,
            "nivel_combustivel": data.nivel_combustivel,
            "validade_ipva": data.validade_ipva,
            "conservacao_veiculo": data.conservacao_veiculo
        }

        return self.is_insert_dict_db(check_list)

    def is_insert_dict_db(self, check_list: RequestModel) -> dict:
        service_db_recorder.insert_one(data_requisition)
        del data_requisition['_id']
        logging.info("Dicionário salvo no banco de dados!!!")
        return data_requisition