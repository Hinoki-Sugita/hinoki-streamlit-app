import pandas as pd
import streamlit as st
import random as rd

st.title("松浦優勝")

# pandasで名簿作成
df = pd.read_excel("members.xlsx", engine = "openpyxl")

# 出席確認
selected = st.multiselect("出席者", options=df["name"])

# 確定ボタン
if st.button("OK"):
    attendance = [name in selected for name in df["name"]]
    df = df[attendance]

#順位付け
def skill(sex, team):
    if   team == "A":
        return 10 + 0.1 * rd.gauss()
    elif team == "B":
        return  8 + 0.2 * rd.gauss()
    elif team == "C":
        return  6 + 0.5 * rd.gauss()
    elif team == "D":
        return  3 + 0.8 * rd.gauss()
    elif team == "E":
        return  1 + 0.5 * rd.gauss()
    else:
        return      0.3 * rd.gauss()

df["power"] = df.apply(lambda row: skill(row["sex"], row["team"]), axis=1)
df.sort_values(by="power", ascending=False, inplace=True)

print(df)

