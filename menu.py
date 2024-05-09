import streamlit as st

def menu(description = None):
    st.sidebar.page_link("pages/5_Homepage.py", label="Home", icon="🏠", )
    st.sidebar.page_link("pages/1_TextAnalysis.py", label="Analysis", icon="📖")
    st.sidebar.page_link("pages/2_Map.py", label="Map", icon="🗺️")
    st.sidebar.page_link("pages/3_Categorization.py", label="Categorization", icon="⛰️")
    st.sidebar.page_link("pages/4_Fulltext.py", label="Full Text", icon="📜")

    if description is not None: 
        st.sidebar.markdown(description)
