import boto3
from botocore.config import Config
import os
from dotenv import load_dotenv
from functions import minio, postgres

# Especifique o caminho absoluto para o arquivo .env
env_file_path = '../conf/.env'

# Carregue as variáveis de ambiente do arquivo .env
load_dotenv(env_file_path)

NESSIE_URI = os.environ.get("NESSIE_URI") ## Nessie Server URI
RAW = os.environ.get("WAREHOUSE") ## BUCKET TO WRITE DATA TOO
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY") ## AWS CREDENTIALS
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY") ## AWS CREDENTIALS
AWS_S3_ENDPOINT= os.environ.get("AWS_S3_ENDPOINT") ## MINIO ENDPOINT

s3 = minio(
    'http://localhost:9000',
    access_key=AWS_ACCESS_KEY,
    secret_key=AWS_SECRET_KEY
)

print(s3.list_buckets())

ps = postgres(
    host='localhost',
    port='5432',
    database='lakehouse_a3',
    user='dashaqui',
    password='dashaqui'
)

ps.conectar()   