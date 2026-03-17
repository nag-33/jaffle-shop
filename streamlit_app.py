import streamlit as st
import streamlit.components.v1 as components

html_file_path = 'target/static_index.html'

st.set_page_config(
    page_title="dbt Docs Viewer",
    layout="wide",
    initial_sidebar_state="collapsed"
)

try:
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    components.html(html_content, height=1200, scrolling=True)
except FileNotFoundError:
    st.error(f"ファイルが見つかりません: {html_file_path}")