from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.expenses import router as expense_router
from .database import engine, Base

app = FastAPI(title="Global Expense Tracker API")

# ✅ CORS middleware (Frontend origins ONLY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://expense-tracker-frontend-tqzs-opkvua1l5.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(expense_router)

# Create DB tables (safe to run on startup)
Base.metadata.create_all(bind=engine)

# Health check
@app.get("/health")
def health_check():
    return {"status": "OK"}