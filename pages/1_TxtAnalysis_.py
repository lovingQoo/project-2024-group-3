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

###############################################################
# Data --WordCloud
###############################################################
word_frequencies = {
    '曰': 551,
    '名曰': 309,
    '東': 211,
    '之山': 183,
    '流注': 179,
    '其狀': 174,
    '山': 125,
    '西': 115,
    '鳥': 109,
    '獸': 104,
    '草木': 101,
    '于': 92,
    '北': 92,
    '水出': 90,
    '南': 84,
    '黃': 81,
    '三百里': 74,
    '人面': 74,
    '水': 64,
    '其下': 64,
    '其陽': 63,
    '注于': 62,
    '東南': 61,
    '北流': 59,
    '食': 58,
    '其上': 58,
    '皆': 55,
    '二百里': 51,
    '穀': 50,
    '其木多': 50,
    '其音': 49,
    '出': 44,
    '狀': 43,
    '蛇': 41,
    '金玉': 39,
    '里': 39,
    '草': 39,
    '大荒': 39,
    '金玉其': 38,
    '五百里': 37,
    '西南': 36,
    '之國': 36,
    '至于': 35,
    '二十里': 35,
    '有人': 35,
    '玉': 34,
    '西北': 34,
    '之中': 34,
    '木': 32,
    '赤': 32,
    '之首': 32,
    '于河': 31,
    '有山': 31,
    '見則': 30,
    '出于': 30,
    '三百': 29,
    '五十里': 29,
    '出焉': 28,
    '其獸': 28,
    '尾': 27,
    '爰': 27,
    '七十里': 26,
    '杻': 26,
    '其祠': 26,
    '陰多': 25,
    '多玉': 25,
    '白': 24,
    '東北': 24,
    '四百里': 23,
    '瘞': 23,
    '天下': 23,
    '喙': 23,
    '彘': 22,
    '首': 22,
    '三十里': 22,
    '之水出': 22,
    '臺': 22,
    '流沙': 22,
    '長': 21,
    '山上': 21,
    '崑': 21,
    '崙': 21,
    '牛': 20,
    '赤水': 20,
    '下多': 20,
    '其鳴': 20,
    '其草': 20,
    '居': 20,
    '海': 19,
    '糈': 19,
    '琈': 19,
    '國': 19,
    '白玉': 18,
    '三百五十里': 18,
    '殺': 18,
    '毛': 18,
    '身': 17,
    '有神': 17,
    '生': 17,
    '其東': 17
}



# 加载云朵形状的图片
cloud_mask = np.array(Image.open('./images/shanfeng.png'))

# 创建词云对象并配置相关参数
wordcloud = WordCloud(font_path='./data/NotoSansTCBlack.ttf', background_color='white', mask=cloud_mask)

# 生成词云图
wordcloud.generate_from_frequencies(word_frequencies)

# 根据图片颜色生成词云图的颜色
image_colors = ImageColorGenerator(cloud_mask)
wordcloud.recolor(color_func=image_colors)

# 显示词云图
st.title("Word Cloud")
st.markdown("As a geographical chronicle, there are many high-frequency words which are descriptive, such as \"name as\", as well as east, south, and west which describe geographical directions.")
fig, ax = plt.subplots(figsize=(80, 50), dpi=300)  # Adjust figsize and dpi for clarity
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

##############################################################
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
# 插入图片
image_path = "./images/shanhaitu.jpg"  # 根据实际文件路径进行修改
image = Image.open(image_path)
st.image(image, caption="", use_column_width=True)
st.markdown("<p style='font-size: 14px;'>插圖：《山海經》中的人魚，常被描述为上半身为人、下半身为鱼的形象。在《山經》中的《西山經》、《北山經》、《中山經》裡都曾出現過人魚，在上面的原文中可以找到。</p>", unsafe_allow_html=True)
# 其他内容
###############################################################
# import python libraries
###############################################################

# 在底部加上參考資料
st.markdown("<h2 style='color: black;'>References:</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: black;'>《山海經》（戰國至漢代，公元前475年-220年），取自https://ctext.org/shan-hai-jing/zhs</p>", unsafe_allow_html=True)
st.markdown("<p style='color: black;'>王紅旗：《全本繪圖山海經︰海內外九經》，武漢大學出版社，2011年4月第1版。</p>", unsafe_allow_html=True)
st.markdown("<p style='color: black;'>羅元：《山精海怪：萌系山海經完全圖譜》，人民郵電出版社，2018年6月第1版。</p>", unsafe_allow_html=True)
st.markdown("<p style='color: black;'>劉宗迪：《失落的天書「《山海經》與古代華夏世界觀（增訂本）》，商務印書館，2016年5月第1版。</p>", unsafe_allow_html=True)