from fastapi import FastAPI
#from routes import pill_routes
import models
from database import engine
from routes.pill_routes import router

from database import SessionLocal
from sqlalchemy.sql import text  # Import text

print("Main loaded")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
print(app.routes)
print("Router routes:", router.routes)

@app.get("/")
def read_root():
    return {"message": "Welcome to PillPal API"}

for route in app.routes:
    print(route.path, route.methods)

with SessionLocal() as db:
    print("Database connection successful:", db.execute(text("SELECT 1")).fetchall())