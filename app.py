import streamlit as st
import pandas as pd

# Title and description
st.title("Hello, Streamlit!")
st.write("This is a simple example of using Streamlit to display text and data.")

# Display a message
st.write("Welcome to your Streamlit app!")

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Display the DataFrame
st.write("Here is a sample DataFrame:")
st.dataframe(df)
