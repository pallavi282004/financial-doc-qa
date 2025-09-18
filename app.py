import streamlit as st
from modules import parser_pdf, parser_excel, qa_engine
import pandas as pd

st.set_page_config(page_title="Financial Document Q&A Assistant")

st.title(" Financial Document Q&A Assistant")

uploaded_file = st.file_uploader("Upload Financial Document (PDF or Excel)", type=["pdf", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        data = parser_pdf.extract_pdf(uploaded_file)
    else:
        data = parser_excel.extract_excel(uploaded_file)
    
    st.success(" Document processed successfully!")
    st.dataframe(data.head())

    st.subheader("Ask a Question")
    query = st.text_input("Enter your question:")

    
    with st.expander(" Example Questions to Try"):
        st.write("""
        **Income Statement:**
        - What is the net profit?
        - Show me the revenue in 2023.
        - What are the operating expenses?

        **Balance Sheet:**
        - What are the total assets in 2022?
        - List the cash balance in 2023.

        **Cash Flow Statement:**
        - What is the closing cash balance?
        - How much cash came from operating activities?
        """)

    if query:
        response = qa_engine.answer_query(query, data)
        st.write("**Answer:**", response)




