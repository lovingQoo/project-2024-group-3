###############################################################
# import python libraries
###############################################################
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Text Analysis -  HUMA5630-Digital Humanities - project-2024-group-3",
    page_icon="⛰️", 
    layout="wide",
    initial_sidebar_state="expanded", 
)
st.caption("HUMA5630 Digital Humanities - Group 3")
###############################################################
# Background Image
###############################################################
# 设置页面背景图层
st.markdown(
    """
    <style>
    .header-container {
        background-image: url(https://cdn.shuge.org/uploads/2016/05/shan-hai-jing01-640x350.jpg);
        background-size: cover;
        background-repeat: no-repeat;
        padding: 20px;
        color: white;
        text-align: center;
    }
    .header-container h1 {
        font-size: 40px;
        color: white;
        margin-bottom: 10px;
    }
    .header-container p {
        font-size: 20px;
        color: white;
        text-align: center;
        display: inline-block;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# 显示标题文字和副标題
st.markdown('<div class="header-container"><h1>Full text of each chapter</h1>', unsafe_allow_html=True)
###############################################################
# Full text of each chapter
###############################################################

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

###############################################################
# Data --TextCategory
##############################################################
st.markdown("##Full text of each chapter")
filepath = './data/shanhaijing.xlsx'
df = pd.read_excel(filepath, sheet_name ='Sheet1')

grouped=df.groupby('卷宗')
juanzong=df['卷宗'].unique()

selected_juanzong = st.selectbox('Select 卷宗', juanzong)
selected_df = grouped.get_group(selected_juanzong)
for index, row in selected_df.iterrows():
    st.write('Text:', row['文本'])
    st.write('Location:',row['Location'])
    st.write('Character:', row['Character'])
    st.write('Monster:', row['Monster'])
    st.write('Treasure:', row['Treasure'])
