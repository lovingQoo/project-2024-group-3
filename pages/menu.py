import streamlit as st

def menu():
    st.sidebar.page_link("pages/homepage.py", label="Home", icon="🏠", )
    st.sidebar.page_link("pages/1_TxtAnalysis.py", label="Analysis", icon="⛰️")
    st.sidebar.page_link("pages/2_map.py", label="Map", icon="🌞")
    st.sidebar.page_link("pages/3_Categorization.py", label="Categorization", icon="⛰️")
