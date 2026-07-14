from fastapi import FastAPI
from app.api import test  

app = FastAPI()

@app.get("/")
def home():
    return {"message": "project started"}

# include your test route
app.include_router(test.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
