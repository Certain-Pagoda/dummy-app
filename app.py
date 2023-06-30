from fastapi import FastAPI
import os
import boto3
from botocore.config import Config
import os
import logging

my_config = Config(region_name = 'eu-west-1')
try:
    print("Got creds from ECS")
    resource = boto3.resource('dynamodb', config=my_config)
except:
    print("Failed to get creds from ECS, reading from env")
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', None)
    print(f"ID populated: {AWS_ACCESS_KEY_ID is not None}")
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', None)
    print(f"Key populated: {AWS_SECRET_ACCESS_KEY is not None}")
    client = boto3.client('dynamodb', 
                          config=my_config,
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

app = FastAPI()

@app.get("/")
async def index():
    environ = os.environ
    return {"message": "OK"}

@app.get("/ping")
async def ping():
    return {"message": "pong!!!!!"}

@app.get("/env")
async def get_env():
    environ = os.environ
    return {"env": environ}

@app.get("/test_db")
def db_test():
    table = resource.Table('dummyapp-table')
    print(table.item_count)
    return {"items": table.scan()}
