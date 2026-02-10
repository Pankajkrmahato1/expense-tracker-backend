from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from ..models import Expense
from ..schemas import ExpenseCreate, ExpenseResponse
from ..deps import get_db
from ..services.currency import get_exchange_rates

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

# PUT update an existing expense
@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(
    expense_id: UUID,
    payload: ExpenseCreate,
    db: Session = Depends(get_db)
):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    expense.item_name = payload.item_name
    expense.amount = payload.amount
    expense.category = payload.category
    expense.currency = payload.currency

    db.commit()
    db.refresh(expense)
    return expense

# DELETE an expense
@router.delete("/{expense_id}")
def delete_expense(expense_id: UUID, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()

    return {"success": True}

# Fetch exchange rates for a given base currency
@router.get("/{base_currency}")
def fetch_exchange_rates(base_currency: str):
    try:
        return get_exchange_rates(base_currency.upper())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))