import streamlit as st

st.title("はじめてのStreamlitアプリ")
st.write("こんにちは！")

name = st.text_input("名前を入力してください")
if name:
    st.write(f"こんにちは、{name}さん！")