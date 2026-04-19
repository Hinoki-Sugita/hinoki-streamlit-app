import pandas as pd
import streamlit as st
import random as rd

#順位付け
def skill(sex, team):
    if   team == "A" and sex == "M":
        return 10 + sigma * rd.gauss()
    elif team == "B" and sex == "M":
        return  8 + sigma * rd.gauss()
    elif team == "C" and sex == "M":
        return  6 + sigma * rd.gauss()
    elif team == "D" and sex == "M":
        return  3 + sigma * rd.gauss()
    elif team == "E" and sex == "M":
        return  1 + sigma * rd.gauss()
    elif                 sex == "M":
        return      sigma * rd.gauss()
    elif team == "A" and sex == "F":
        return 10 + sigma * rd.gauss()
    elif team == "B" and sex == "F":
        return  7 + sigma * rd.gauss()
    elif team == "C" and sex == "F":
        return  5 + sigma * rd.gauss()
    elif team == "D" and sex == "F":
        return  2 + sigma * rd.gauss()
    elif team == "E" and sex == "F":
        return  1 + sigma * rd.gauss()    
    else:
        return      sigma * rd.gauss()

#台数
num = st.number_input("台数", value=1, step=1)
t = int(num)

#標準偏差
sigma = st.number_input("σ", value = 1.0, step = 0.1)

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
    rd.shuffle(table)

    #表示
    start = 0
    for ai in table:
      row_elements = present[start:start+ai]
      st.write(*row_elements)
      start += ai

