from fastapi import FastAPI
import uvloop

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello World"}


@app.get("/main")
def home():
    return {"abc": "hello World"}