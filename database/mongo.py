from pymongo import MongoClient, errors
import logging

class DataBaseConnection():
    def is_connction_db():
        url_connection = "mongodb+srv://daniel_l8:1234@cluster0.s5jlp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        try:
            logging.info("Conectando ao banco de dados!!")

            client = MongoClient(url_connection, serverSelectionTimeoutMS=5000)
            db = client["projeto_l8"]
            logging.info("Conexão realizada com sucesso")

            client.admin.command("ping")
            logging.info("Conexão realizada com sucesso")

            return db
        
        except errors.ServerSelectionTimeoutError:
            logging.error("Erro: Não foi possível conectar ao MongoDB, verifique a string de conexão ou a disponibilidade do servidor.")

        except errors.ConnectionFailure:
            logging.error("Erro: Falha na conexão com o MongoDB.")

        except Exception as error:
            logging.error(f"Erro inesperado: {error}")

        return None