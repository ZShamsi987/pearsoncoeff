import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def home():
    # Main title
    st.title("Stock Correlation App")

    # Description
    st.write("This app allows you to input two stock tickers and a time frame to calculate the Pearson coefficient and visualize the stock prices.")

    # Sub-heading for entering tickers
    st.markdown("<h2 style='text-align: center;'>Enter Ticker</h2>", unsafe_allow_html=True)

    # Text boxes for entering ticker symbols
    ticker1 = st.text_input("Ticker 1", value='', placeholder="Ex: AAPL")
    ticker2 = st.text_input("Ticker 2", value='', placeholder="Ex: MSFT")

    # Dropdown for selecting time frame
    st.markdown("<h3 style='text-align: center;'>Select Time Frame</h3>", unsafe_allow_html=True)
    selected_time_frame = st.selectbox("Time Frame", options=["5d", "1mo", "3mo", "6mo", "1y", "ytd", "5y", "max"], index=0)

    # Button to calculate
    if st.button("Calculate", help="Click this button to calculate"):
        # Fetch data
        data1 = yf.download(ticker1, period=selected_time_frame.lower())
        data2 = yf.download(ticker2, period=selected_time_frame.lower())

        # Plot data
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.plot(data1['Close'], label=ticker1, color='blue')
        ax.plot(data2['Close'], label=ticker2, color='red')
        ax.set_title('Stock Prices Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.legend()

        # Convert plot to PNG image
        img = BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.read()).decode()

        # Display image
        st.image(f"data:image/png;base64,{plot_url}", use_column_width=True)

def about():
    # About page content
    st.title("About")
    st.write("This app is created by Zafir. It calculates the Pearson coefficient between two stock tickers based on the selected time frame and visualizes the stock prices.")

def main():
    # Set page title
    st.set_page_config(page_title="Stock Correlation App")

    # Sidebar navigation
    menu_selection = st.sidebar.radio("Navigation", ["Home", "About"])

    # Based on menu selection, display the corresponding page
    if menu_selection == "Home":
        home()
    elif menu_selection == "About":
        about()

if __name__ == "__main__":
    main()
