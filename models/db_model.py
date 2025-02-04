from pydantic import BaseModel
from uuid import uuid4

class RequestModel(BaseModel):
    request_id_check_list: str = uuid4().hex
    placa_carro: str
    nome_completo: str
    trecho: str
    data_ultima_manutencao: str
    conservacao_veiculo: str
    ar_condicionado: str
    cartao_abastecineto: str
    chave_ignicao: str
    cinto_seguranca: str
    farol_lanternas: str
    limpeza_interior: str
    parabrisa: str
    pneus: str
    chave_roda: str
    retrovisor: str
    tag_sem_parar: str
    triangulo_sinalizacao: str
    vidros: str
    macaco: str
    funcionamento_geral: str
    limpador_parabrisa: str
    esguicho_agua: str
    rack_escada: str
    estado_geral: str
    descricao_varias: str

class UserModel(BaseModel):
    user_id: str = uuid4().hex
    user_email: str
    user_password: str
    