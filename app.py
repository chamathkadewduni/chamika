import streamlit as st
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from customers;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.customer_id } has a :{row.customer_name}:")