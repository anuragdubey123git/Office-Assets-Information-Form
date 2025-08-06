import streamlit as st
import mysql.connector
from datetime import datetime

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anurag",  # change this
    database="office_assets_db"
)
cursor = conn.cursor()

st.title("Office Assets Information Form")

# Form
with st.form("asset_form"):
    asset_type = st.selectbox("Asset Type", ["Laptop", "Mouse", "Extension Box", "TV", "Monitor", "Keyboard", "Projector"])
    serial_number = st.text_input("Serial Number")
    branch = st.text_input("Branch (e.g., Kalyan Nagar, Bangalore)")
    purchase_year = st.number_input("Year of Purchase", min_value=2000, max_value=2099, step=1)
    condition = st.selectbox("Condition", ["Good", "Needs Repair", "Bad"])
    remarks = st.text_area("Remarks (optional)", placeholder="Any additional notes...")

    submitted = st.form_submit_button("Submit")
    if submitted:
        query = """
            INSERT INTO assets (asset_type, serial_number, branch, purchase_year, `condition`, remarks)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (asset_type, serial_number, branch, purchase_year, condition, remarks)
        cursor.execute(query, data)
        conn.commit()
        st.success("✅ Asset information submitted successfully!")
