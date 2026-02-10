from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..models import Expense
from ..schemas import ExpenseCreate, ExpenseResponse
from ..deps import get_db

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

# GET all expenses
@router.get("/", response_model=List[ExpenseResponse])
def get_all_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).order_by(Expense.created_at.desc()).all()

# CREATE a new expense
@router.post("/", response_model=ExpenseResponse)
def create_expense(payload: ExpenseCreate, db: Session = Depends(get_db)):
    expense = Expense(**payload.dict())
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense