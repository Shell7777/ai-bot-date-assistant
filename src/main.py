from fastapi import FastAPI

from src.lib.infrastructure.api.routes.routes import api_router

app = FastAPI(title="Automate AI")

app.include_router(api_router)

@app.get("/")
def health_check():
    return {"status": "ok", "version": "1.0.0"}