from fastapi import FastAPI
from .routers.expenses import router as expense_router

app = FastAPI(title="Global Expense Tracker API")

app.include_router(expense_router)

@app.get("/health")
def health_check():
    return {"status": "OK"}