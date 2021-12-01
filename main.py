from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": " welcome Hello World, trying reload functionality"}

@app.get("/post")
def get_post():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    #Body(...) in fast api will exxtrac all body content and it will convert into dict and will assign to payload variable.
    print(payload)
    return {"message":"Successful", "data":f"Title is {payload['title']}" }


