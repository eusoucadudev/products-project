from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def app_route():
    return "Hello World!"