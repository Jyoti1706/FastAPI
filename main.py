from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": " welcome Hello World, trying reload functionality"}

@app.get("/post")
def get_post():
    return {"data":"This is your post"}
