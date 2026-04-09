import pandas as pd
import streamlit as st
import random as rd

st.title("出席チェック")

# pandasで名簿作成
df = pd.read_excel("member.xlsx")

selected = st.multiselect("出席者", options=df["名前"])

if st.button("OK"):
    attendance = [name in selected for name in df["名前"]]
    df = df[attendance]

st.write(df)

