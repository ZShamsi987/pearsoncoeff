import streamlit as st

def main():
    # Set page title
    st.set_page_config(page_title="Stock Correlation App")

    # Main title
    st.title("Test title")

    # Description
    st.write("Welcome to the Stock Correlation App! This app allows you to input two stock tickers and a time frame to calculate the Pearson coefficient and visualize the stock prices.")

if __name__ == "__main__":
    main()
