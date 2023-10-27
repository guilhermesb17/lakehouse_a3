import boto3
from botocore.config import Config
import psycopg2

class minio:
    def __init__(self, endpoint_url, access_key, secret_key):
        self.endpoint_url = endpoint_url
        self.access_key = access_key
        self.secret_key = secret_key

        self.minio_client = self.create_minio_client()

    def create_minio_client(self):
        return boto3.client(
            's3', 
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
            )

    def list_buckets(self):
        response = self.minio_client.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        return buckets

    def upload_file(self, bucket_name, object_name, local_file_path):
        self.minio_client.upload_file(local_file_path, bucket_name, object_name)

    def download_file(self, bucket_name, object_name, local_file_path):
        self.minio_client.download_file(bucket_name, object_name, local_file_path)

    def read_file_from_minio(self, bucket_name, file):
    # Configurando o cliente do MinIO
        obj = self.minio_client.get_object(Bucket=bucket_name, Key=file)
    # Lendo o conteúdo do arquivo
        file_content = obj['Body'].read()
        
        return file_content

class postgres:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def conectar(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Conectado com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar: {e}")

    def desconectar(self):
        if self.connection:
            self.connection.close()
            print("Conexão encerrada!")

    def query(self, query):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
                print("Query executada com sucesso!")
            except Exception as e:
                print(f"Erro ao executar: {e}")
        else:
            print("Conect-se Primeiro")
