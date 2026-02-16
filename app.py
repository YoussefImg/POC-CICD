from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Message": "POC CI/CD is running!"}

@app.get("/health")
def health():
    return {"status" : "Ok"}