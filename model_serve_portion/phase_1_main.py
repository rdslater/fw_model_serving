from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def read_status():
    print("🚀 Received a ping from the Flywheel gear!")
    return {"message": "connected"}

if __name__ == "__main__":
    import uvicorn
    # Run on 0.0.0.0 so it listens on all network interfaces
    uvicorn.run(app, host="0.0.0.0", port=8008)
