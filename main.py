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
    st.write("This app calculates the Pearson coefficient between two stock tickers based on the selected time frame and visualizes the stock prices.")
    
    st.subheader("How does it work?")   
    st.write("The Pearson correlation coefficient (r) is a measure of the linear relationship between two variables, typically denoted as $x$ and $y$. The formula to calculate $r$ is:")
    st.write("$$r = \\frac{\\sum (x - m_x)(y - m_y)}{\\sqrt{\\sum (x - m_x)^2 \\sum (y - m_y)^2}}$$")
    st.write("where:")
    st.write("- $x$ and $y$ are the variables being analyzed,")
    st.write("- $m_x$ and $m_y$ represent the means (average values) of variables $x$ and $y$, respectively, and")
    st.write("- $\\sum$ denotes the summation across all data points.")
    st.write("The Pearson correlation coefficient $r$ measures the strength and direction of the linear relationship between $x$ and $y$. It ranges from -1 to 1:")
    st.write("- $r = 1$ indicates a perfect positive linear relationship, where $y$ increases as $x$ increases.")
    st.write("- $r = -1$ indicates a perfect negative linear relationship, where $y$ decreases as $x$ increases.")
    st.write("- $r = 0$ indicates no linear relationship between $x$ and $y$.")

    st.subheader("Coming soon:")
    st.write("Below are some features I would like to eventually add to this app(or another app in the future)/noticed would be helpful")
    st.write("-1 day graph and coeffecient")
    st.write("-Nicer/interactive graph")
    st.write("-More securities and commodities from other markets")
    st.write("-Moving averages")
    st.write("-Custom time range")
    st.write("-Other statistical/quant elements")
    st.subheader("This app was written by [Zafir Shamsi](https://github.com/ZShamsi987)")
    st.write("")
    st.write("")
    st.caption("Send [feedback or report bugs](mailto:shamsizafir@gmail.com)")
    st.caption("This app was heavily inspired by [this post](https://www.reddit.com/r/quant/comments/1bm28bx/i_did_a_comprehensive_correlation_analysis_on_all/) on r/quant")



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
