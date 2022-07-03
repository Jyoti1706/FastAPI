from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Updated Hello World"}


@app.get("/posts")
def get_post():
    return {"Post1": "Data"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"message": "successfully created a post"}