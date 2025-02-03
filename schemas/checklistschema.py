from pydantic import BaseModel, Field
import logging

logging.baseConfig(level=logging.INFO)

class CheckListSchema(BaseModel):
   placa_carro: str = Field(..., description="Recebe a placa do veiculo a ser vistoriado")
   nome_completo: str = Field(..., description="Recebe o nome completo do trabalhador que esta vistoriando o carro")
   trecho: str = Field(..., description="Recebo o trecho onde o trabalhador trabalha")
