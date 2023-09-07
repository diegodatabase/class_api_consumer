from google.cloud import bigquery

class BigQueryInserter:
    
    _client = None

    @classmethod
    def initialize(cls, credentials_path: str):
        cls._client = bigquery.Client.from_service_account_json(credentials_path)
        
    @classmethod
    def insert_data(cls, dataset_id: str, table_id: str, rows: list):
        """
        Insere dados em uma tabela BigQuery.

        :param dataset_id: ID do conjunto de dados BigQuery.
        :param table_id: ID da tabela dentro do conjunto de dados.
        :param rows: Lista de dados a serem inseridos. Cada item deve ser um dicionário 
                     representando uma linha de dados a ser inserida.
        """
        if cls._client is None:
            raise RuntimeError("Client not initialized. Call 'initialize' method first.")

        table_ref = cls._client.dataset(dataset_id).table(table_id)
        table = cls._client.get_table(table_ref)
        
        errors = cls._client.insert_rows_json(table, rows)
        if errors:
            raise RuntimeError(f"BigQuery insert errors: {errors}")


