import streamlit as st
from ocr import extract_text
from categorizer import categorize
from advisor import get_advice
from save_expense import save_expense
from budget import get_budget

st.title("Financial Advisor AI Agent")

uploaded_file = st.file_uploader(
    "Upload Screenshot"
)

if uploaded_file:

    with open("temp.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text("temp.png")

    st.write("Extracted Text:")
    st.write(text)

    category = categorize(text)

save_expense(text, category)

st.write("Category:", category)
budget = get_budget(category)

st.write("Budget Recommendation:")
st.write(budget)

if st.button("Get Financial Advice"):

        advice = get_advice(text)

        st.write("AI Advice:")
        st.write(advice)