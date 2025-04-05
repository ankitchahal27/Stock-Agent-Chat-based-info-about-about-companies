def generate_prompt(company_data, question):
    summary = company_data["summary"]
    
    prompt = f"""
You are a financial assistant. Use the company data below to answer the user's question in a clear and concise way.

[Company Data]
Name: {summary['name']}
Sector: {summary['sector']}
Industry: {summary['industry']}
Market Cap: {summary['marketCap']}
Trailing P/E: {summary['trailingPE']}
Forward P/E: {summary['forwardPE']}
Dividend Yield: {summary['dividendYield']}

User Question: {question}

Answer:
""".strip()
    
    return prompt
