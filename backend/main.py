from fastapi import FastAPI
from routes import pill_routes

app = FastAPI()

app.include_router(pill_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to PillPal API"}