from pydantic import BaseModel, Field
import logging

logging.basicConfig(level=logging.INFO)

class CheckListSchema(BaseModel):
   placa_carro: str = Field(..., description="Recebe a placa do veiculo a ser vistoriado")
   nome_completo: str = Field(..., description="Recebe o nome completo do trabalhador que esta vistoriando o carro")
   trecho: str = Field(..., description="Recebe o trecho onde o trabalhador trabalha")
   data_ultima_manutencao: str = Field(..., description="Recebe a data da ultima manutenção realizada")
   hodometro: str = Field(..., description="Recebe a quantidade de KM's rodados")
   nivel_combustivel: str = Field(..., description="Recebe a quantidade de combustivel no tanque")
   validade_ipva: str = Field(..., description="Recebe se o IPVA do veiculo e valido no ano corrente do check list")
   conservacao_veiculo: str = Field(..., description="Recebe o estado de conservação geral do veiculo")
   ar_condicionado: str = Field(..., description="Recebe o estado de conservação do ar condicionado do veiculo")
   cartao_abastecineto: str = Field(..., description="Recebe o status do cartão de abastecimento do veiculo")
   chave_ignicao: str = Field(..., description="Recebe o estado de conservação da chave de ignição do veiculo")
   cinto_seguranca: str = Field(..., description="Recebe o estado de conservação do cinto de segurança do veiculo")
   farol_lanternas: str = Field(..., description="Recebe o estado de conservação do farol e lanternas do veiculo")
   limpeza_interior: str = Field(..., description="Recebe o estado de limpeza do interior do veiculo")
   parabrisa: str = Field(..., description="Recebe o estado de conservação do parabrisa do veiculo")
   pneus: str = Field(..., description="Recebe o estado de conservação dos pneus do veiculo")
   chave_roda: str = Field(..., description="Recebe o estado de conservação da chave de roda do veiculo")
   retrovisor: str = Field(..., description="Recebe o estado de conservação do retrovisor do veiculo")
   tag_sem_parar: str = Field(..., description="Recebe o status tag sem parar do veiculo")
   triangulo_sinalizacao: str = Field(..., description="Recebe o estado de conservação do triangulo de sinalização do veiculo")
   vidros: str = Field(..., description="Recebe o estado de conservação dos vidros do veiculo")
   macaco: str = Field(..., description="Recebe o estado de conservação do macaco do veiculo")
   funcionamento_geral: str = Field(..., description="Recebe o estado de funcionamento geral do veiculo")
   limpador_parabrisa: str = Field(..., description="Recebe o estado de conservação do limpador de parabrisa do veiculo")
   esguicho_agua: str = Field(..., description="Recebe o estado de conservação do esguicho de agua do veiculo")
   rack_escada: str = Field(..., description="Recebe o estado de conservação do rack de escada do veiculo")
   estado_geral: str = Field(..., description="Recebe o estado geral do veiculo")
   descricao_avarias: str = Field(..., description="Recebe todas as descrições das avarias do veiculo")