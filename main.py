import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {
        "app": "rep3",
        "platform": "render",
        "commit": os.getenv("RENDER_GIT_COMMIT", "local")[:7],
    }