from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.expenses import router as expense_router
from .database import engine, Base

app = FastAPI(title="Global Expense Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expense_router)

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "OK"}