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
