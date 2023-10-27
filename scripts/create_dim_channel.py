import os
import boto3
import pandas as pd
from io import BytesIO
from botocore.config import Config
from dotenv import load_dotenv
from functions import minio, postgres
from sqlalchemy import create_engine

# Especifique o caminho absoluto para o arquivo .env
env_file_path = '../conf/.env'

# Carregue as variáveis de ambiente do arquivo .env
load_dotenv(env_file_path)

NESSIE_URI = os.environ.get("NESSIE_URI") ## Nessie Server URI
RAW = os.environ.get("WAREHOUSE") ## BUCKET TO WRITE DATA TOO
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY") ## AWS CREDENTIALS
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY") ## AWS CREDENTIALS
AWS_S3_ENDPOINT= os.environ.get("AWS_S3_ENDPOINT") ## MINIO ENDPOINT
#DB_URI = 'postgresql+psycopg2://username:password@localhost:5432/mydatabase'
DB_URI = 'postgresql+psycopg2://dashaqui:dashaqui@localhost:5432/lakehouse_a3'

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

dados_channel = s3.read_file_from_minio('raw' , 'channels.csv')

df_channel = pd.read_csv(BytesIO(dados_channel))

df_channel = df_channel[['channel_name', 'channel_type']]

#print(df_channel)

create_channel_sql = """
DROP TABLE IF EXISTS dim_channel CASCADE;

CREATE TABLE dim_channel (
    channel_id SERIAL PRIMARY KEY,
    channel_name varchar(255) NOT NULL,
    channel_type varchar(255) NOT NULL
);
"""

ps.query(create_channel_sql)

engine = create_engine(DB_URI)

df_channel.to_sql(
    'dim_channel',
    engine,
    if_exists='append',
    index=False)