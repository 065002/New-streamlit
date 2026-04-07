
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 Live Google Sheet Dashboard")

url = "https://docs.google.com/spreadsheets/d/1F9lqy8PT5xgI1YZ-W2PWT5FQhde8hmWLpR1zdVyCX9M/export?format=csv"
df = pd.read_csv(url)

st.subheader("Dataset")
st.dataframe(df)

st.subheader("Summary")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

column = st.selectbox("Select Column", df.columns)
value = st.selectbox("Select Value", df[column].dropna().unique())

filtered_df = df[df[column] == value]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

numeric_df = df.select_dtypes(include=["number"])

if not numeric_df.empty:
    st.subheader("Chart")
    st.bar_chart(numeric_df)
