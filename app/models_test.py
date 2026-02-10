from .database import SessionLocal
from .models import Expense

db = SessionLocal()

expense = db.query(Expense).first()
print("Expense from DB:", expense)

db.close()