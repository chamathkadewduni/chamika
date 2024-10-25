import streamlit as st
import pandas as pd
from xamp import engine  # Import the SQLAlchemy engine from xamp.py

# Function to fetch data from a specified table
@st.cache_data
def load_data(table_name):
    try:
        # Query the table
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, con=engine)
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# Streamlit Interface
st.title("MySQL Database Viewer")

# Dropdown to select a table to view
table_option = st.selectbox("Select Table", options=["customers", "orders"])

# Load data based on the selected table
if table_option:
    data = load_data(table_option)
    if data is not None:
        st.write(f"Data from {table_option} table:")
        st.dataframe(data)

# Additional feature: Adding a view of table structure
st.write("Table Structure Information")
if table_option == "customers":
    st.write({
        "customer_id": "Integer, Primary Key, Autoincrement",
        "customer_name": "String(255), Not Null"
    })
elif table_option == "orders":
    st.write({
        "order_id": "Integer, Primary Key, Autoincrement",
        "customer_id": "Integer, Foreign Key, Not Null",
        "total_amount": "Float, Not Null",
        "order_date": "DateTime, Not Null"
    })

