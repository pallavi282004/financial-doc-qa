import pandas as pd

def extract_excel(file):
    sheets = pd.read_excel(file, sheet_name=None)
    frames = [df for name, df in sheets.items()]
    return pd.concat(frames, ignore_index=True)
