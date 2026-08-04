import streamlit as st

st.set_page_config(page_title="Customer Segmentation", layout="wide")

st.title("🛍 Customer Segmentation using K-Means")

st.write("Welcome to the Customer Segmentation Project.")

st.success("Deployment Successful!")

st.markdown("""
# Project Overview
This project uses the K-Means clustering algorithm to segment customers based on:
- Age
- Annual Income
- Spending Score

The notebook contains preprocessing, clustering, visualization, and evaluation.
""")
