import streamlit as st

st.title("はじめてのStreamlitアプリ")
st.write("こんにちは！")

name = st.text_input("名前を入力してください")
if name:
    st.write(f"こんにちは、{name}さん！")

import streamlit as st
import pandas as pd

st.title("出席チェックアプリ（スマホ対応）")

# 名簿作成（学生1～70）
students = [f"学生{i}" for i in range(1, 71)]

# マルチセレクトで出席者を選択
selected_students = st.multiselect(
    "出席した人を選択してください（検索可）",
    options=students
)

# 選択人数を表示
st.write(f"出席人数: {len(selected_students)}")