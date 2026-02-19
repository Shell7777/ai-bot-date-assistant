from fastapi import FastAPI
from src.lib.infrastructure.api.routes.appointment_routes import router as appointment_router

app = FastAPI(title="BarberShop AI")

app.include_router(appointment_router)

@app.get("/")
def health_check():
    return {"status": "ok", "version": "1.0.0"}