🌍 Global Expense Tracker – Backend API
A production-ready backend API for the Global Expense Tracker application.
Built with FastAPI, PostgreSQL (Supabase), and deployed on Render.
This API supports full CRUD operations for expenses, real-time usage by a frontend client, and is CORS-enabled for secure web deployment.

🚀 Tech Stack
FastAPI – High-performance Python web framework
PostgreSQL – Database (hosted on Supabase)
SQLAlchemy – ORM
Pydantic – Data validation
Render – Cloud deployment

📦 Features
Create, Read, Delete expenses
PostgreSQL persistence
CORS configured for frontend access
Health check endpoint
OpenAPI / Swagger documentation

📂 Project Structure
app/
├── main.py # App entry point
├── database.py # DB connection & session
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas
├── routers/
│ └── expenses.py # Expense CRUD routes
└── **init**.py

🧾 Database Schema (Supabase)
| Column | Type | Description |
| ---------- | --------- | ------------------ |
| id | UUID | Primary Key |
| item_name | TEXT | Expense name |
| amount | NUMERIC | Expense amount |
| category | TEXT | Food, Travel, etc. |
| currency | TEXT | INR, USD, EUR |
| created_at | TIMESTAMP | Auto-generated |

🔌 API Endpoints
Get all expenses
GET /expenses

Create an expense
POST /expenses
{
"item_name": "Lunch",
"amount": 250,
"category": "Food",
"currency": "INR"
}

Delete an expense
DELETE /expenses/{expense_id}

Health check
GET /health

📑 API Documentation
Swagger UI available at:
https://expense-tracker-backend-a4bi.onrender.com/docs

🌐 Deployment
Platform: Render
Free tier note: Backend may sleep after inactivity and take ~15–30 seconds to wake up

🧪 Local Development
pip install -r requirements.txt
uvicorn app.main:app --reload

👤 Author
Pankaj Mahato
Full Stack Developer | FastAPI | React | PostgreSQL
