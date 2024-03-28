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
    col1, col2 = st.columns(2)
    with col1:
        ticker1 = st.text_input("Ticker 1", value='', max_chars=None, key=None, type='default', help=None, placeholder="Ex: AAPL", on_change=None, args=None, kwargs=None)
    with col2:
        ticker2 = st.text_input("Ticker 2", value='', max_chars=None, key=None, type='default', help=None, placeholder="Ex: MSFT", on_change=None, args=None, kwargs=None)

    # Dropdown for selecting time frame
    st.markdown("<h3 style='text-align: center;'>Select Time Frame</h3>", unsafe_allow_html=True)
    time_frames = ["5d", "1mo", "3mo", "6mo", "1y", "ytd", "5y", "max"]
    selected_time_frame = st.selectbox("", options=time_frames, index=0, format_func=lambda x: x)

    st.session_state.button_width = 200 

    # Calculate the amount of space needed for centering
    space_width = st.session_state.button_width / 0.4

    # Container for button
    button_container = st.container()

    # Button to calculate
    with button_container:
        st.write("")
        col1, col2, col3 = st.columns([space_width, st.session_state.button_width, space_width])
        with col2:
            if st.button("Calculate", key="calculate_button", help="Click this button to calculate"):
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

                # Embed HTML with CSS to control size
                st.markdown(f'<div style="overflow-x:auto;"><img src="data:image/png;base64,{plot_url}" style="width: 100%; height: auto;"></div>', unsafe_allow_html=True)

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
