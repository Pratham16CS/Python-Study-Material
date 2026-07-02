import streamlit as st
import pandas as pd

st.title("IPL Matches Dashboard")

file = st.file_uploader("UPload your csv file",type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    city = df["city"].unique()
    selected_city = st.selectbox("Filter by city",city)
    filtered_data = df[df['city'] == selected_city]
    st.dataframe(filtered_data)
