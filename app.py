import streamlit as st
import pandas as pd

st.title("松浦優勝")

# 名簿
students = [f"学生{i}" for i in range(1, 71)]

# マルチセレクト
selected_students = st.multiselect("出席",options=students)

# 選択人数
st.write(f"出席人数: {len(selected_students)}")