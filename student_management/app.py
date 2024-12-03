from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI()

# Include the router
app.include_router(student_router)

@app.get("/")
def root():
    return {"message": "Student Management System API"}

if _name_ == "_main_":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)