import boto3
import os
import requests
from fastapi import FastAPI,Path, Response, status,HTTPException
from pydantic import BaseModel
import json
from boto3.dynamodb.conditions import Key, Attr

dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'us-east-1',
              aws_access_key_id = '',
              aws_secret_access_key = '')

movie_table = dynamo_client.Table('Movies')
food_table= dynamo_client.Table('Food')
app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


class Details(BaseModel):
    Rating: int
    Description:str


class Movie(BaseModel):
    Title:str
    Year: str
    Test: list
    # Details: Details


# @app.get("/items/{Title}")
# def get_movie(Title: str):
#     response = movie_table.scan(FilterExpression=Attr("Title").eq(Title) )
#     data = response['Items']
#     return(data)

@app.get("/items/")
def get_movie():
    response = movie_table.scan()
    data = response['Items']
    return(data)

@app.post("/items/")
async def create_item(movie:Movie):

    payload=movie.dict()
    rsms=payload["Test"]
    
    return payload
    # payload=json.dumps(movie.dict())
    # async def create_item(title:str,year:str):
#     item={"Title":title,"Year":year}
    
    # response = movie_table.scan(FilterExpression=Attr('Title').eq(x) )
    # data = response['Items']
    # if data:
    #     print(True)
    # else:
    #     print(False)

    # movie_table.put_item(Item = payload)
    # print(response.status_code)
    # print(response.text)
    # return({"message":"movie added","response":response.json()})


# @app.get("/food")
# def get_movie(Title: str):
#     payload={"dish_name":"chole_bhature","time":"1.5 hours"}
#     food_table.put_item(Item = payload)
#     # response = food_table.scan(FilterExpression=Attr("dish_name").eq(Title) )
#     response = food_table.scan() 
#     data = response['Items']
#     return(data)

# payload={"dish_name":"chole_bhature","time":"2 hours"}
# food_table.put_item(Item = payload)
# response = food_table.scan(FilterExpression=Attr("dish_name").eq(Title) )
# response = food_table.scan() 
# data = response['Items']
# print(data)

# item={"Title":"Inception","Year":2011,"Rating":9}

# movie_table.put_item(Item = item)
# response = movie_table.scan()
# data = response['Items']
# print(data)
