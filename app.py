import streamlit as st

st.title("はじめてのStreamlitアプリ")
st.write("こんにちは！")

name = st.text_input("名前を入力してください")
if name:
    st.write(f"こんにちは、{name}さん！")

# 左右2列に分割
col1, col2 = st.columns(2)

students = [f"学生{i}" for i in range(1, 71)]
selected_students = []


for student in students[:35]:
    if col1.checkbox(student):
        selected_students.append(student)

for student in students[35:]:
    if col2.checkbox(student):
        selected_students.append(student)

st.write(f"出席者（人数: {len(selected_students)}）:")