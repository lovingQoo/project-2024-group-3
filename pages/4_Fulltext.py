###############################################################
# import python libraries
###############################################################
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd
import base64
from PIL import Image

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


def add_bg_from_local():
    image_path = "./images/shanhaib.jpg"  # 根据实际文件路径进行修改
    with open(image_path, 'rb') as f:
        image_data = f.read()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{base64.b64encode(image_data).decode()});
            background-size: cover;
            filter: contrast(0.8);
            opacity: 0.9;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 调用函数显示背景图像
add_bg_from_local()
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
st.markdown("《山海經》全書一十八篇，其中「山經」五篇，分別是《南山經》、《西山經》、《北山經》、《東山經》、《中山經》；「海經」八篇，分別是《海外南經》、《海外西經》、《海外北經》、《海外東經》、《海內南經》、《海內西經》、《海內北經》、《海內東經》；「大荒經」四篇，分別是《大荒東經》、《大荒南經》、《大荒西經》、《大荒北經》；以及「海內經」一篇。請選擇要閱讀的章節：")
filepath = './data/shanhaijing.xlsx'
df = pd.read_excel(filepath, sheet_name ='Sheet1')

grouped=df.groupby('卷宗')
juanzong=df['卷宗'].unique()

selected_juanzong = st.selectbox('The Classic of Mountains and Seas has a total of eighteen chapters. Please choose the chapter you want to read:', juanzong)
selected_df = grouped.get_group(selected_juanzong)

# 逐行显示文本内容，并修改字体和颜色
for index, row in selected_df.iterrows():
    content = row['文本']
    sentences = content.split('。')  # 分割句子
    paragraphs = [' '.join([s.strip() + '。' for s in sentences[i:i+1]]) for i in range(0, len(sentences), 1)]  # 每句话为一个段落，保留句号
    paragraphs[-1] = paragraphs[-1].rstrip('。')  # 删除最后一个段落末尾的句号
    for paragraph in paragraphs:
        st.markdown(f"<p style='font-family: KaiTi; font-size: 16px; color: black;'>{paragraph}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family: Arial; font-size: 14px; color: #808080;'>地名：{row['Location']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family: Arial; font-size: 14px; color: #808080;'>人物：{row['Character']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family: Arial; font-size: 14px; color: #808080;'>異獸：{row['Monster']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family: Arial; font-size: 14px; color: #808080;'>奇珍：{row['Treasure']}</p>", unsafe_allow_html=True)


# 插入图片
image_path = "./images/shanhaitu.jpg"  # 根据实际文件路径进行修改
image = Image.open(image_path)
st.image(image, caption="", use_column_width=True)
# 其他内容
