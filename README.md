# Stock-Agent: Chat-based-info-about-about-any-company

StockGPT is a Streamlit-based app that combines financial data with a Hugging Face language model to answer user questions about a company.

# Features
- Fetches company financials using `yfinance`
- Displays income statement, balance sheet, and stock chart
- Allows users to ask alomost all sorts of questions about the company like:
  - *How is the company performing?*
  - *What is its forward P/E?*
- Powered by Hugging Face `Mistral-7B-Instruct` 
- Clean and interactive UI using Streamlit

# How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/stockgpt.git
cd stockgpt

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Add Hugging Face token (create a file named `token.env`)
echo HF_TOKEN=your_token_here > token.env

# Run the app
streamlit run app.py
