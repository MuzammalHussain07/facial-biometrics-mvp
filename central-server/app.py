from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "OK", "service": "Central Server"}

@app.post("/api/enroll")
def enroll():
    return {"message": "Demo enrolment successful"}

@app.post("/api/sync")
def sync():
    return {"message": "Demo sync complete"}
