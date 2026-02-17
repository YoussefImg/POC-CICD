from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "version": "v3", "msg": "deploy test"}

@app.get("/health")
def health():
    return {"status" : "Ok from CI/CD"}