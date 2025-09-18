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

## Example Questions to Try

After uploading the sample documents (from `sample_data/`), you can try questions like:

**Income Statement**
- What is the net profit?
- Show me the revenue in 2023.
- What are the operating expenses?

**Balance Sheet**
- What are the total assets in 2022?
- List the cash balance in 2023.

**Cash Flow Statement**
- What is the closing cash balance?
- How much cash came from operating activities?
## Demo Screenshot

Below is a sample run of the Financial Document Q&A Assistant:

![App Screenshot](screenshot.png)
