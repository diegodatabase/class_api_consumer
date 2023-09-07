from api.consumer import APIConsumer
from api.load import BigQueryInserter
from configparser import ConfigParser

def main():

    config = ConfigParser()
    config.read('./config/config.ini')

    # Configurações
    CREDENTIALS_PATH =  config['DEFAULT']['CREDENTIALS_PATH']
    DATASET_ID = config['DEFAULT']['DATASET_ID']
    TABLE_ID = config['DEFAULT']['TABLE_ID']
    
    # Inicialização do BigQuery
    try:
        BigQueryInserter.initialize(CREDENTIALS_PATH)
    except Exception as e:
        print(f"Erro ao inicializar o BigQuery: {e}")
        return

    # Obter pessoas via API
    try:
        people = APIConsumer.get_people(1)
    except Exception as e:
        print(f"Erro ao obter dados da API: {e}")
        return

    # Validação básica dos dados
    if not people:
        print("Nenhum dado recebido da API para inserir no BigQuery.")
        return

    # Inserir dados no BigQuery
    try:
        BigQueryInserter.insert_data(DATASET_ID, TABLE_ID, people)
    except Exception as e:
        print(f"Erro ao inserir dados no BigQuery: {e}")

if __name__ == "__main__":
    main()
