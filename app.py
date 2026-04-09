import pandas as pd
import streamlit as st
import random as rd

st.title("出席チェック")

# pandasで名簿作成
df = pd.read_excel("members.xlsx")


selected = st.multiselect("出席者", options=df["name"])

if st.button("OK"):
    attendance = [name in selected for name in df["name"]]
    df = df[attendance]

st.write(df)

