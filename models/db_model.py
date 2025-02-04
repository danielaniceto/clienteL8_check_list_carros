"""from pydantic import BaseModel
from uuid import uuid4

class RequestModel(BaseModel):
    request_id_check_list: str = uuid4().hex
    request_route: str
    request_method: str
    request_header: str = {}
    request_parameters: str = {}
    request_body: str
    request_api_response: str = {}
    request_datatime: str"""