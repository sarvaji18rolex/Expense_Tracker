
# 💰 Expense Tracker App

A simple personal expense tracker built with Streamlit + SQLite.

## Features
- Add expenses (amount, category, note, date)
- View expenses in a table
- Export expenses as CSV
- Analytics: Spending by category, monthly spending trends

## Requirements
- Python 3.8–3.11 (recommended)
- Streamlit, Pandas, Matplotlib

## Installation & Run

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # Activate:
   # Windows PowerShell: .\venv\Scripts\Activate.ps1
   # Linux/macOS: source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run expense_tracker.py
   ```

4. Open [http://localhost:8501](http://localhost:8501) in your browser.

## Notes
- Data is stored locally in `expenses.db` (SQLite).
- You can reset the database by deleting `expenses.db`.
