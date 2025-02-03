import logging
from database.mongo import DataBaseConnection
from schemas.loginschema import LoginSchema
from fastapi.responses import RedirectResponse

service_db = DataBaseConnection.is_connction_db()["users"]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("api_controller.log"), logging.StreamHandler()]
)

class LoginController:
    def __init__(self):
        logging.info('LoginController initialized')

        if service_db is None:
            logging.critical("A conexão com banco de dados falhou!!!")
            raise ValueError("A conexão com banco de dados falhou!!!")
        
        self.service_db = service_db
        
    async def is_valid_login(self, data: LoginSchema) -> RedirectResponse:
        logging.info(f"Dados recebidos para criação: url={data.usuario}, title={data.senha}")

        user = self.service_db.find_one("usuário": data.uusuario, "senha": data.senha)

        if user:
            logging.info("Validação de usuário e senha OK!!!")
            return RedirectResponse(url="/dashboard", status_code=303)
    
        return {"erro": "Usuário ou senha inválidos"}

        
