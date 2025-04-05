import yfinance as yf
import pandas as pd
import plotly.graph_objs as go


def get_stock_info(ticker: str) -> dict:
    """
    Fetch stock summary info, financials, and balance sheet for a given ticker.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').

    Returns:
        dict: A dictionary containing summary info, financials, and balance sheet.
    """
    try:
        stock = yf.Ticker(ticker)
        
        info = stock.info
        financials = stock.financials
        balance_sheet = stock.balance_sheet

        summary = {
            "name": info.get("longName", "N/A"),
            "symbol": info.get("symbol", ticker.upper()),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "marketCap": info.get("marketCap", "N/A"),
            "trailingPE": info.get("trailingPE", "N/A"),
            "forwardPE": info.get("forwardPE", "N/A"),
            "dividendYield": info.get("dividendYield", "N/A"),
            "summary": info.get("longBusinessSummary", "No summary available.")
        }

        return {
            "summary": summary,
            "financials": financials.fillna("N/A") if isinstance(financials, pd.DataFrame) else "Not available",
            "balance_sheet": balance_sheet.fillna("N/A") if isinstance(balance_sheet, pd.DataFrame) else "Not available"
        }
    
    except Exception as e:
        return {
            "error": f"Failed to fetch data for {ticker}: {e}"
        }
    
def get_price_chart(ticker: str, period: str = "3mo"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], mode='lines', name='Close Price'))
    fig.update_layout(
        title=f"{ticker.upper()} Stock Price - Last {period}",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        height=400
    )
    return fig
