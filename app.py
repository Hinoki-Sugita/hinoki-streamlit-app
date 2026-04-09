import streamlit as st

st.title("はじめてのStreamlitアプリ")
st.write("こんにちは！")

name = st.text_input("名前を入力してください")
if name:
    st.write(f"こんにちは、{name}さん！")

present_students = []
students = ["佐藤", "鈴木", "高橋", "田中", "伊藤"]

for student in students:
    if st.checkbox(student):
        present_students.append(student)

st.write("出席者:", present_students)