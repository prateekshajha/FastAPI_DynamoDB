import boto3
import os
import requests
from fastapi import FastAPI,Path, Response, status,HTTPException
from pydantic import BaseModel


dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'us-east-1',
              aws_access_key_id = 'XXXX',
              aws_secret_access_key = 'XXXX')

movie_table = dynamo_client.Table('Movies')

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# class Movie(BaseModel):
#     Title:str
#     year: str
@app.post("/items/")
async def create_item(title:str,year:str):
    item={"Title":title,"Year":year}

    movie_table.put_item(Item = item)
    return({"message":"movie "+title+" added"})