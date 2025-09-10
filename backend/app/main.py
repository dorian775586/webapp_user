from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routers import offers

app = FastAPI(title="nolikby API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()  # создаём таблицы и тестовые данные

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(offers.router, prefix="/offers", tags=["offers"])
