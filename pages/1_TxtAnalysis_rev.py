###############################################################
# import python libraries
###############################################################
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np
import streamlit as st
import pandas as pd
from annotated_text import annotated_text
import re
import ast
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
        background-image: url(https://img95.699pic.com/photo/40195/1356.jpg_wh300.jpg);
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

    div[data-testid="stMarkdownContainer"] p {
        font-size: 20px;
        line-height: 2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示标题文字和副标题
st.markdown('<div class="header-container"><h1>About This Text</h1>', unsafe_allow_html=True)
###############################################################
# page content
###############################################################

st.markdown("")
st.markdown("The 'Classic of Mountains and Seas' is a renowned ancient Chinese text that delves into the rich tapestry of mythical geography, creatures, and cultures. Compiled over centuries, it stands as a testament to the profound imagination and curiosity of ancient Chinese scholars. Within its pages lie a mesmerizing blend of folklore, cosmology, and geography, offering readers a window into the imaginative worldviews of ancient China.")
st.markdown("The book has more than 38,000 words in total and is divided into eighteen sections; it describes over 550 mountains and 300 channels.")
st.markdown("---")


##############################################################
# Data --TextCategory

st.title("Annotation on full text")

st.markdown(""" Annotation color: 
            <span style='background-color:#90b2ca;padding:5px 10px; border-radius:8px;'>Character</span>
            <span style='background-color:#e3bece;padding:5px 10px; border-radius:8px;'>Monster</span>
            <span style='background-color:#ead46f;padding:5px 10px; border-radius:8px;'>Treasure</span>
            <span style='background-color:#b2d9cb;padding:5px 10px; border-radius:8px;'>Location</span>
            """, unsafe_allow_html=True)


def highlight_name(text, cList, monsterList, tList, placeList):
    for word in cList:
        regex = re.compile(word)
        text = regex.sub('",("' + word + '", "Character", "#90b2ca"),"', text)
    for word in monsterList:
        regex = re.compile(word)
        text= regex.sub('",("' + word + '", "Monster", "#e3bece"),"', text)
    for word in tList:
        regex = re.compile(word)
        text= regex.sub('",("' + word + '", "Treasure", "#ead46f"),"', text)
    for word in placeList:
        regex = re.compile(word)
        text = regex.sub('",("' + word + '", "Location", "#b2d9cb"),"', text)
    return text


filepath = './data/shanhaijing.xlsx'
df = pd.read_excel(filepath, sheet_name='Sheet1')


cList = [name.strip() for name in df['Character'].astype(str).str.split('、').explode() if isinstance(name, str) and name.strip() and name.strip() != "nan" and len(name.strip()) > 1]
cList = list(set(cList)) #remove duplicates within the list
cList.sort(key=lambda x: len(x))
if "禺彊" in cList:
    cList.remove("禺彊") # remove to avoid conflict, monster list also have 禺彊
if "顓頊" in cList:
    cList.remove("顓頊") # remove to avoid conflict with 帝顓頊
if "赤水女子獻" in cList:
    cList.remove("赤水女子獻") # remove to avoid conflict with the location 赤水
# check---- st.markdown(cList)

mList = [name.strip() for name in df['Monster'].astype(str).str.split('、').explode() if isinstance(name, str) and name.strip() and name.strip() != "nan"]
mList = list(set(mList)) #remove duplicates within the list
mList.sort(key=lambda x: len(x))

tList = [name.strip() for name in df['Treasure'].astype(str).str.split('、').explode() if isinstance(name, str) and name.strip() and name.strip() != "nan"]
tList = list(set(tList)) #remove duplicates within the list
tList.sort(key=lambda x: len(x))

placeList = [name.strip() for name in df['Location'].astype(str).str.split('、').explode() if isinstance(name, str) and name.strip() and name.strip() != "nan" and len(name.strip()) > 1]
placeList = list(set(placeList)) #remove duplicates within the list
placeList.sort(key=lambda x: len(x))
if "顓頊" in placeList:
    placeList.remove("顓頊") # remove to avoid conflict with 帝顓頊



tab_hill, tab_sea = st.tabs(["山經", "海经"])

with tab_hill:
    tab_names = df.loc[df["分類"] == "山經", "卷宗"].unique().tolist()
    # Create tabs based on the unique values
    tabs = st.tabs(tab_names)
    # Display the content of each tab
    for i, tab in enumerate(tabs):
        with tab:
            fulltext = df.loc[df["卷宗"] == tab_names[i], "文本"].values[0]
            fulltext = fulltext.replace("\n", "")
            # annotate    
            highlighted_text = '"' + highlight_name(fulltext, cList, mList, tList, placeList) + '"'
            highlighted_text = ast.literal_eval(highlighted_text) # Convert string to a list
            annotated_text(*highlighted_text)



with tab_sea:
    tab_names = df.loc[df["分類"] == "海经", "卷宗"].unique().tolist()
    # Create tabs based on the unique values
    tabs = st.tabs(tab_names)
    # Display the content of each tab
    for i, tab in enumerate(tabs):
        with tab:
            fulltext = df.loc[df["卷宗"] == tab_names[i], "文本"].values[0]
            fulltext = fulltext.replace("\n", "")
            # annotate    
            highlighted_text = '"' + highlight_name(fulltext, cList, mList, tList, placeList) + '"'
            highlighted_text = ast.literal_eval(highlighted_text) # Convert string to a list
            annotated_text(*highlighted_text)
