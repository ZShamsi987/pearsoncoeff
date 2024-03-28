import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def home():
    # Main title
    st.title("Stock Correlation App")

    # Description
    st.write("This app allows you to input two stock tickers and a time frame to calculate the Pearson coefficient and visualize the stock prices.")

    # Sub-heading for entering tickers
    st.markdown("<h2 style='text-align: center;'>Enter Ticker</h2>", unsafe_allow_html=True)

    # Text boxes for entering ticker symbols
    col1, col2 = st.columns(2)
    with col1:
        ticker1 = st.text_input("Ticker 1", value='', max_chars=None, key=None, type='default', help=None, placeholder="Ex: AAPL", on_change=None, args=None, kwargs=None)
    with col2:
        ticker2 = st.text_input("Ticker 2", value='', max_chars=None, key=None, type='default', help=None, placeholder="Ex: MSFT", on_change=None, args=None, kwargs=None)

    # Dropdown for selecting time frame
    st.markdown("<h3 style='text-align: center;'>Select Time Frame</h3>", unsafe_allow_html=True)
    time_frames = ["5d", "1mo", "3mo", "6mo", "1y", "ytd", "2y", "5y", "max"]
    selected_time_frame = st.selectbox("", options=time_frames, index=0, format_func=lambda x: x)

    st.session_state.button_width = 200 

    # Calculate the amount of space needed for centering
    space_width = st.session_state.button_width / 0.4

    # Create empty space before the button for centering
    st.write("")
    col1, col2, col3 = st.columns([space_width, st.session_state.button_width, space_width])

    # Button to calculate
    with col2:
        if st.button("Calculate", key="calculate_button"):

            # Fetch data
            data1 = yf.download(ticker1, period=selected_time_frame.lower())
            data2 = yf.download(ticker2, period=selected_time_frame.lower())

            # Calculate Pearson coefficient
            coefficient, _ = pearsonr(data1['Close'], data2['Close'])

            # Plot data
            plt.figure(figsize=(10, 6))
            plt.plot(data1['Close'], label=ticker1, color='blue')
            plt.plot(data2['Close'], label=ticker2, color='red')
            plt.title('Closing Stock Prices Over Time')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            st.pyplot(plt)

    # Display Pearson coefficient in a styled box
    if 'coefficient' in locals():
        st.info(f"The Pearson coefficient is: **{coefficient:.55f}**")

    # Adding the two lines of text at the bottom
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("NOTE: Check for normality before entering tickers")
    st.write("NOTE: To expand graph, hover over it and then click the maximize button")


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
