import logging
from database.mongo import DataBaseConnection
from schemas.checklistschema import CheckListSchema

service_db = DataBaseConnection.is_connction_db()["campos_check_list_carro"]

class CheckListController:
    def __init__(self):
        logging.info("LoginController initialized")

    async def is_check_list_car(self, data: CheckListSchema):