import pdfplumber
import pandas as pd

def extract_pdf(file):
    tables = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_table()
            if extracted:
                df = pd.DataFrame(extracted[1:], columns=extracted[0])
                tables.append(df)
    if tables:
        return pd.concat(tables, ignore_index=True)
    return pd.DataFrame()
