from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Test CI/CD pipeline OK Ok"}

@app.get("/testql")
def testQL():
    return {"CodeQL test"}

@app.get("/test")
def test():
    return {"test"}

@app.get("/health")
def health():
    return {"status" : "Ok from CI/CD"}