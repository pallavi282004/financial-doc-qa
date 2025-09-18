# Financial Document Q&A Assistant

## Overview
This application allows users to upload financial documents (PDFs and Excel files) and ask natural language questions about the contained data (revenue, expenses, profit, etc.). It is built using Streamlit and powered by local Small Language Models (SLMs) via Ollama.

## Features
- Upload financial statements (Income, Balance Sheet, Cash Flow)
- Extract and display structured financial data
- Ask questions in natural language through an interactive chat interface
- Local-only deployment (no cloud dependencies)

## Installation

### Prerequisites
- Python 3.9+
- Streamlit
- Ollama installed locally
- Dependencies from `requirements.txt`

### Setup
```bash
git clone https://github.com/yourusername/financial-doc-qa.git
cd financial-doc-qa
pip install -r requirements.txt
# 📄 4. Sample `requirements.txt`

streamlit
pdfplumber
pandas
openpyxl
ollama

