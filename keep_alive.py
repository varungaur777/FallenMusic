from fastapi import FastAPI
import threading
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "alive"}

def run():
    uvicorn.run(app, host="0.0.0.0", port=10000)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()
