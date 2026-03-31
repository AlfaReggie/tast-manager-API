from fastapi import FastAPI

app = FastAPI(title="Operation September API")


@app.get("/")
def read_root():
    return {
        "message": "Backend is running",
        "project": "Operation September"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }