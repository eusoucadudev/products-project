from fastapi import FastAPI
from app.routes.category_routes import router as category_routes

app = FastAPI()

@app.get("/")
def app_route():
    return "Hello World!"

app.include_router(category_routes)
