from pydantic import BaseModel, Field
import logging

logging.baseConfig(level=logging.INFO)

class LoginSchema(BaseModel):
   usuario: str = Field(..., description="Recebe o nome do usuário, email")
   senha: str = Field(..., description="Recebe a senha do usuário")
