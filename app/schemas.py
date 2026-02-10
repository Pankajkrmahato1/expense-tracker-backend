from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

# What client sends when creating an expense
class ExpenseCreate(BaseModel):
    item_name: str
    amount: float
    category: str
    currency: str

# What client receives from API
class ExpenseResponse(ExpenseCreate):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True