import boto3
import os
import requests
from fastapi import FastAPI,Path, Response, status,HTTPException,Form
from pydantic import BaseModel
from typing import Annotated


# dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'us-east-1',
#               aws_access_key_id = 'AKIAT2H2B7LBFAN32NWR',
#               aws_secret_access_key = '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')
# movie_table = dynamo_client.Table('Movies')

dynamodb_resource = boto3.resource('dynamodb')
movie_table = dynamodb_resource.Table("Movies")



app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/items/")
async def create_item(title: Annotated[str, Form()],year: Annotated[int, Form()]):
    if year<1900 or year>2023 :
        raise HTTPException(status_code=404,detail="Invalid")

    item={"Title":title,"Year":year}

    movie_table.put_item(Item = item)
    return({"message":"movie "+title+" added"})

# @app.get("/items/{movie_details}")
# async def read_item(movie_name: str):
#     response = movie_table.get_item(Key={"Title":movie_name})
#     return response

# response = movie_table.get_item(Key={'Title': '','Year': 'Doe'})
# item = response['Item']
# print(item)


    