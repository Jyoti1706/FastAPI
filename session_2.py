from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.exceptions import HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
#pydantic is use for schema validation when sent as body for post method

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True #optional parameter
    rating: Optional[int] = None
post_data = [{"title": "cloud", "content":" Defination of cloud","id":1}, {"title": "cloud app", "content":" deployment of app on cloud","id":2}]


@app.get("/")
async def root():
    return {"message": " welcome Hello World, trying reload functionality"}

@app.get("/posts")
def get_post():
    return {"data":post_data}


@app.post("/posts", status_code=HTTP_201_CREATED)
def create_post(post: Post):
    post_dic = post.dict()
    post_dic["id"] = randrange(0,1200000)
    post_data.append(post_dic)
    return {"message":"Successful", "data": post_dic }


def find_posts(id):
    for p in post_data:
        if p["id"]== id:
            return p
    # else:
    #     return "Id does not exists"

@app.get("/posts/{id}")
def get_posts(id: int, response: Response):    #id: int will make sur that id passed is integer
    print(id)
    post = find_posts(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"details Not Found for {id}")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": "Not Found"}  

    return {"post details": post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    for p in post_data:
        if p["id"] == id:
            post_data.remove(p)
            return {"message": f"Deletion Successful for id: {id}"}
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail= f" unable to delete, details not found for {id}")

    


