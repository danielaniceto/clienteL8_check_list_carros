import logging
from uuid import uuid4, UUID
from database.mongo import DataBaseConnection
from schemas.checklistschema import CheckListSchema
from models.db_model import RequestModel

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
            "conservacao_veiculo": data.conservacao_veiculo,
            "ar_condicionado": data.ar_condicionado,
            "cartao_abastecineto": data.cartao_abastecineto,
            "chave_ignicao": data.chave_ignicao,
            "cinto_seguranca": data.cinto_seguranca,
            "farol_lanternas": data.farol_lanternas,
            "limpeza_interior": data.limpeza_interior,
            "parabrisa": data.parabrisa,
            "pneus": data.pneus,
            "chave_roda": data.chave_roda,
            "retrovisor": data.retrovisor,
            "tag_sem_parar": data.tag_sem_parar,
            "triangulo_sinalizacao": data.triangulo_sinalizacao,
            "vidros": data.vidros,
            "macaco": data.macaco,
            "funcionamento_geral": data.funcionamento_geral,
            "limpador_parabrisa": data.limpador_parabrisa,
            "esguicho_agua": data.esguicho_agua,
            "rack_escada": data.rack_escada,
            "estado_geral": data.estado_geral,
            "descricao_varias": data.descricao_avarias
                }

        return self.is_insert_dict_db(check_list)

    def is_insert_dict_db(self, check_list: RequestModel) -> dict:
        service_db.insert_one(check_list)
        logging.info("Dicionário salvo no banco de dados!!!")
        return check_list
    