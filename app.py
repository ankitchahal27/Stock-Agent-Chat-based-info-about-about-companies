from huggingface_hub import login
from dotenv import load_dotenv
import os

load_dotenv()
login(token=os.getenv("HF_TOKEN"))

import streamlit as st
from stock_utils import get_stock_info
from transformers import pipeline
from prompt_utils import generate_prompt
from stock_utils import get_price_chart

st.set_page_config(page_title="StockGPT", page_icon="📊")
st.title("📊 StockGPT – Chat with a Stock")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", device_map="auto", max_new_tokens=256)

generator = load_model()

st.markdown(
    """
    Enter a stock ticker (like `AAPL`, `GOOGL`, `TSLA`) to get the latest company info, financials, and balance sheet.
    """
)

# Input box
ticker = st.text_input("Enter Stock Ticker", value="AAPL").upper()

# When ticker is entered
if ticker:
    with st.spinner("Fetching data..."):
        data = get_stock_info(ticker)

    if "error" in data:
        st.error(data["error"])
    else:
        st.subheader(f"🔹 {data['summary']['name']} ({data['summary']['symbol']})")
        st.write(f"**Sector**: {data['summary']['sector']}")
        st.write(f"**Industry**: {data['summary']['industry']}")
        st.write(f"**Market Cap**: {data['summary']['marketCap']:,}")
        st.write(f"**Trailing P/E**: {data['summary']['trailingPE']}")
        st.write(f"**Forward P/E**: {data['summary']['forwardPE']}")
        st.write(f"**Dividend Yield**: {data['summary']['dividendYield']}")
        st.write(f"**Summary**: {data['summary']['summary']}")

        st.divider()

        # Financials
        st.subheader("📈 Income Statement")
        st.dataframe(data["financials"], use_container_width=True)

        # Balance Sheet
        st.subheader("📊 Balance Sheet")
        st.dataframe(data["balance_sheet"], use_container_width=True)

st.divider()
st.subheader("🤖 Ask StockGPT a Question")

question = st.text_input("What would you like to ask?", placeholder="e.g., How is this company performing?")

if question:
    with st.spinner("Thinking..."):
        prompt = generate_prompt(data, question)
        response = generator(prompt)[0]['generated_text'].split("Answer:")[-1].strip()
        st.markdown(f"**Answer:** {response}")

st.divider()
st.subheader("📉 Stock Price Chart")

if ticker:
    chart = get_price_chart(ticker, period="3mo")  # You can change to '6mo', '1y', etc.
    st.plotly_chart(chart, use_container_width=True)
