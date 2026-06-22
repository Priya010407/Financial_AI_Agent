import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Page Title
st.title("📊 Expense Dashboard")

# Connect Database
conn = sqlite3.connect("expenses.db")

# Read Data
df = pd.read_sql_query(
    "SELECT * FROM expenses",
    conn
)

# Show Data Table
st.subheader("📋 All Expenses")
st.dataframe(df)

# Total Transactions
st.metric("Total Transactions", len(df))

# Category Summary
st.subheader("📈 Category Summary")

summary = df["category"].value_counts()

st.bar_chart(summary)

# Pie Chart
st.subheader("🥧 Expense Distribution")

fig = px.pie(
    names=summary.index,
    values=summary.values,
    title="Expense Distribution by Category"
)

st.plotly_chart(fig)

# Close Database
conn.close()