from pydantic import BaseModel, Field
import logging

logging.baseConfig(level=logging.INFO)

class CheckListSchema(BaseModel):
   placa_carro: str = Field(..., description="Recebe a placa do veiculo a ser vistoriado")
   nome_completo: str = Field(..., description="Recebe o nome completo do trabalhador que esta vistoriando o carro")
   trecho: str = Field(..., description="Recebe o trecho onde o trabalhador trabalha")
   data_ultima_manutencao: str = Field(..., description="Recebe a data da ultima manutenção realizada")
   hodometro: str = Field(..., description="Recebe a quantidade de KM's rodados")
   nivel_combustivel: str = Field(..., description="Recebe a quantidade de combustivel no tanque")
   validade_ipva: str = Field(..., description="Recebe se o IPVA do veiculo e valido no ano corrente do check list")
   conservacao_veiculo: str = Field(..., description="Recebe o estado de conservação geral do veiculo")