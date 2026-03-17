import streamlit as st
import streamlit.components.v1 as components
import os

html_file_path = 'target/static_index.html'

# ファイルが存在するか確認
if not os.path.exists(html_file_path):
    st.error(f"エラー: ファイルが見つかりません: {os.path.abspath(html_file_path)}")
else:
    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        components.html(html_content, height=1024, scrolling=False)
    except Exception as e:
        st.error(f"ファイル読み込みエラー: {type(e).__name__} - {e}")