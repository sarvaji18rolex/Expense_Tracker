
import streamlit as st 
import sqlite3 
import pandas as pd   
import matplotlib.pyplot as plt  
from datetime import datetime  
    
# ---------- DATABASE ---------- 
def init_db(): 
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    amount REAL,
                    category TEXT,
                    note TEXT,
                    date TEXT
                )""")
    conn.commit()
    return conn

def add_expense(conn, amount, category, note, date):
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, category, note, date) VALUES (?,?,?,?)",
              (amount, category, note, date))
    conn.commit()

def get_expenses(conn):
    return pd.read_sql("SELECT * FROM expenses", conn)

# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="💰 Expense Tracker", layout="wide")
st.title("💰 Personal Expense Tracker")

conn = init_db()

menu = ["Add Expense", "View Expenses", "Analytics"]
choice = st.sidebar.radio("Menu", menu)

if choice == "Add Expense":
    st.subheader("➕ Add a New Expense")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"])
    note = st.text_area("Note (optional)")
    date = st.date_input("Date", datetime.today())

    if st.button("Save Expense"):
        add_expense(conn, amount, category, note, str(date))
        st.success("Expense added successfully!")

elif choice == "View Expenses":
    st.subheader("📜 All Expenses")
    df = get_expenses(conn)
    if not df.empty:
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "expenses.csv", "text/csv")
    else:
        st.info("No expenses recorded yet.")

elif choice == "Analytics":
    st.subheader("📊 Analytics")
    df = get_expenses(conn)
    if df.empty:
        st.info("No data available yet. Add some expenses!")
    else:
        # Convert date column to datetime
        df["date"] = pd.to_datetime(df["date"])

        # Spending by category
        cat_sum = df.groupby("category")["amount"].sum()

        st.write("### Spending by Category")
        fig1, ax1 = plt.subplots()
        cat_sum.plot(kind="bar", ax=ax1)
        st.pyplot(fig1)

        # Spending over time
        time_sum = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()

        st.write("### Monthly Spending Trend")
        fig2, ax2 = plt.subplots()
        time_sum.plot(kind="line", marker="o", ax=ax2)
        st.pyplot(fig2)
