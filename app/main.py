from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.expenses import router as expense_router
from .database import engine, Base


app = FastAPI(title="Global Expense Tracker API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://expense-tracker-backend-a4bi.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expense_router)

# Ensure DB tables are created
Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "OK"}