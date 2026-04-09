import pandas as pd
import streamlit as st
import random as rd

#順位付け
def skill(sex, team):
    if   team == "A":
        return 10 + 1.0 * rd.gauss()
    elif team == "B":
        return  8 + 1.0 * rd.gauss()
    elif team == "C":
        return  6 + 1.0 * rd.gauss()
    elif team == "D":
        return  3 + 1.3 * rd.gauss()
    elif team == "E":
        return  1 + 1.0 * rd.gauss()
    else:
        return      0.8 * rd.gauss()

# 1~30 の整数を入力
num = st.number_input("台数", value=1, step=1)
t = int(num)

# pandasで名簿作成
df = pd.read_excel("members.xlsx", engine = "openpyxl")

# 出席確認
selected = st.multiselect("出席者", options=df["name"])

# 確定ボタン
if st.button("OK"):
    attendance = [name in selected for name in df["name"]]
    df = df[attendance]
    df["power"] = df.apply(lambda row: skill(row["sex"], row["team"]), axis=1)
    df.sort_values(by="power", ascending=False, inplace=True)
    present = list(df["name"])
    n = len(present)
    a = n // t
    b = n  % t
    table = [a] * (t-b) + [a+1] * b

    #表示
    start = 0
    for ai in table:
      row_elements = present[start:start+ai]
      st.write(*row_elements)
      start += ai