from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Project started"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
