from fastapi import FastAPI
from routes.student_routes import router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Student Management API"}

app.include_router(router)