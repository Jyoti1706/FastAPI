from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
#pydantic is use for schema validation when sent as body for post method

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True #optional parameter
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": " welcome Hello World, trying reload functionality"}

@app.get("/post")
def get_post():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_post(payload: Post):
    #Body(...) in fast api will exxtrac all body content and it will convert into dict and will assign to payload variable.
    #print(payload.dict())
    return {"message":"Successful", "data": payload }

@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    #Body(...) in fast api will exxtrac all body content and it will convert into dict and will assign to payload variable.
    print(payload)
    return {"message":"Successful", "data":f"Title is {payload['title']}" }
    


