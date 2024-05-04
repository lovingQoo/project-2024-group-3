###############################################################
# import python libraries
###############################################################
import streamlit as st
import pandas as pd
import plotly.express as px
import base64

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Categorization of Mythical Creatures -  HUMA5630-Digital Humanities - project-2024-group-3",
    page_icon="⛰️", 
    layout="wide",
    initial_sidebar_state="expanded", 
)
st.caption("HUMA5630 Digital Humanities - Group 3")
###############################################################
# Background Image
###############################################################
def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(https://pic.ntimg.cn/file/20231128/18232014_114808225102_2.jpg);
            background-size: cover;
            filter: contrast(0.8);
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()

# 设置页面背景图层
st.markdown(
    """
    <style>
    .header-container {
        background-image: url(https://img95.699pic.com/photo/40193/0245.jpg_wh300.jpg);
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

# 显示标题文字和副标题
st.markdown('<div class="header-container"><h1>ShanHai BaiLin《山海百靈》</h1><p>The book "Shanhai Bailin: Divine Birds, Beasts, and Fish in the Shanhai Jing" includes a collection of one hundred original national treasure-level color illustrations from the Edo period\'s "Kaiqi Niaoshou Tujuan" and the Qing Dynasty\'s "Shanhai Jing Tujian." The illustrations are accompanied by supplementary texts that provide information on the habitat, appearance, behavior, and corresponding original texts from the Shanhai Jing.</p></div>', unsafe_allow_html=True)


###############################################################
# page content
###############################################################
st.title("Let's Explore Different Types of Mythical Creatures in the Classic of Mountains and Rivers!")
###############################################################
# Data
###############################################################
filepath = './data/mythical_creatures.xlsx'
data = pd.read_excel(filepath, sheet_name='Sheet1')
###############################################################
# Book Information
###############################################################
expander = st.expander("Click here to see more information about the Book", expanded=False)

with expander:
    expander.write("Book Title: ShanHai BaiLin《山海百靈》")
    expander.write("Book SubTitle: 'ShanHai BaiLin' - Divine Humanoid Birds, Beasts, and Fish in the Shanhai Jing《山海百靈》 —— 山海經裡的神人鳥獸魚")
    expander.write("Writer: Wang Xinxi 王新禧")
    expander.write("Publisher: Beijing Shidai Huawen Shuju 北京時代華文書局")
    expander.write("Page Number: 320 pages")

    # 创建两列
    col1, col2 = st.columns([1, 1])

    # 在第一列添加第一张图片
    image_path1 = './images/山海百靈.png'
    col1.image(image_path1, use_column_width=True)

    # 在第二列添加第二张图片
    image_path2 = './images/山海百靈2.jpeg'
    col2.image(image_path2, use_column_width=True)
    #image_path = f'./images/山海百靈.png'  # 根据索引值构建图片文件路径
    #expander.image(image_path)

###############################################################
# Guess Numer of Mythical Creatures in the Book
###############################################################
st.markdown("---")
st.markdown("## Can You Guess How Mmany Mythical Creatures in the Book?")

correct_number = 100
user_guess = st.number_input("Let's Guess Now: ", min_value=1, max_value=1000, step=1)

if user_guess < correct_number:
    st.write("Too few~")
elif user_guess > correct_number:
    st.write("Too many~")
else:
    st.write("Congratulations, you guessed it right!")

expander = st.expander("Click here to see the correct number", expanded=False)
creaturesnum = len(data)
with expander:
    expander.write(f'There are a total of {creaturesnum} mythical creatures in this book')
st.markdown("---")
###############################################################
# Chart - Chapters & Origins
###############################################################
st.markdown("## Pie Chart Showing the Distribution of Mythical Creatures in the Book")

# Count the occurrences of each language
origins_counts = data['篇章'].value_counts()

# Create a DataFrame from the counts
df_origins = pd.DataFrame({'篇章': origins_counts.index, 'Count': origins_counts.values})

# Create a pie chart using Plotly Express -- Based on Origins
fig_origin = px.pie(df_origins, values='Count', names='篇章',title= 'Distribution of Mythical Creatures Based on Origins')
# Count the occurrences of each origin
origin_counts = data['出處'].value_counts()

# Create a DataFrame from the counts
df_chapter = pd.DataFrame({'出處': origin_counts.index, 'Count': origin_counts.values})

# Create a pie chart for the origin using Plotly Express -- Based on Chapters
fig_chapter = px.pie(df_chapter, values='Count', names='出處', title='Distribution of Mythical Creatures Based on Chapters')
# Create two columns
col1, col2 = st.columns([1, 1])

# Set the background color of the pie chart to transparent
fig_origin.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # 设置背景颜色为透明
    plot_bgcolor='rgba(0,0,0,0)'  # 设置绘图区域背景颜色为透明
)

# Display the first pie chart in the first column - Origins
col1.plotly_chart(fig_origin, use_container_width=True)

# Set the background color of the pie chart to transparent
fig_chapter.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # 设置背景颜色为透明
    plot_bgcolor='rgba(0,0,0,0)'  # 设置绘图区域背景颜色为透明
)

# Display the second pie chart in the second column - Chapters
col2.plotly_chart(fig_chapter, use_container_width=True)

# Display the first pie chart in the first column - Origins
#col1.plotly_chart(fig_origin, use_container_width=True)

# Display the second pie chart in the second column - Chapters
#col2.plotly_chart(fig_chapter, use_container_width=True)
st.markdown("---")

###############################################################
# Categorization
###############################################################
st.markdown("## Categorization of Mythical Creatures in the Book")

# 读取Excel文件
filepath = './data/mythical_creatures.xlsx'
df = pd.read_excel(filepath, sheet_name='Sheet1')

# 按篇章分组
grouped = df.groupby('篇章')

# 获取所有篇章
origins = df['篇章'].unique()

# 创建一个下拉菜单，用于选择篇章
selected_origins = st.selectbox('Select Origin', origins)
    
# 根据选择的篇章显示对应的異獸
selected_df = grouped.get_group(selected_origins)
for index, row in selected_df.iterrows():
    # use column layout for better layout
    colcount = st.columns([3, 7]) 
    count = 200
    with colcount[0]: 
        st.subheader(row['名字'])
        image_path = f'./images/creatures_images/{index+1}.png'  # 根据索引值构建图片文件路径
        st.image(image_path, width=150)
        st.write( row['形容'])
    with colcount[1]:
        st.write('原文：', row['原文'])
        st.write('譯釋：', row['譯釋'])
    st.write('---')

# FYI, you can customize the style of text
#customStyleTitle = '<h1 style="font-family: serif; color:#684905; font-size: 50px;">Let\'s Explore Different Types of Mythical Creatures in the Classic of Mountains and Rivers!</h1>'
#st.markdown(customStyleTitle, unsafe_allow_html=True)
