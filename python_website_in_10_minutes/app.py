import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="👋",
    layout="wide"
)

# Add a title
st.title("Welcome to My Streamlit App! 👋")

# Add a sidebar
st.sidebar.header("Dashboard")
selected_page = st.sidebar.selectbox(
    "Select a page",
    ["Home", "Data Analysis", "About"]
)

# Main content based on selection
if selected_page == "Home":
    st.write("## Home Page")
    st.write("This is a simple Streamlit app created in minutes!")
    
    # Add some interactive elements
    name = st.text_input("Enter your name")
    if name:
        st.write(f"Hello, {name}!")
    
    # Add a chart
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)

elif selected_page == "Data Analysis":
    st.write("## Data Analysis")
    
    # Upload file feature
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Your Data")
        st.dataframe(df)
        
        st.write("### Basic Statistics")
        st.write(df.describe())

else:
    st.write("## About")
    st.write("""
    This is a demo Streamlit application showing how quickly you can create
    interactive web applications using Python and Streamlit.
    
    Features include:
    - Multiple pages
    - Interactive charts
    - File upload and analysis
    - Real-time updates
    """)

# Add a footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")

