def answer_query(query, dataframe):
    query_lower = query.lower()
    
    if "revenue" in query_lower:
        col = [c for c in dataframe.columns if "revenue" in c.lower()]
        if col:
            return dataframe[col[0]].dropna().values.tolist()
        return "Revenue not found in document."
    
    elif "profit" in query_lower:
        col = [c for c in dataframe.columns if "profit" in c.lower()]
        if col:
            return dataframe[col[0]].dropna().values.tolist()
        return "Profit not found in document."
    
    elif "expense" in query_lower:
        col = [c for c in dataframe.columns if "expense" in c.lower()]
        if col:
            return dataframe[col[0]].dropna().values.tolist()
        return "Expenses not found in document."
    
    return "I could not understand the question. Please rephrase."
