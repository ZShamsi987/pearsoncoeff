import streamlit as st

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
    time_frames = ["1D", "1W", "3M", "6M", "1Y", "All"]
    selected_time_frame = st.selectbox("", options=time_frames, index=0, format_func=lambda x: x)

    # Button to calculate
    col1, _, col3 = st.columns([1, 1, 1])  # Adjust column widths as needed
    with col1:
     st.write("")  # Create empty space to push button to center
    with col3:
     if st.button("Calculate", key="calculate_button"):
        st.write("Calculating...")  

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
