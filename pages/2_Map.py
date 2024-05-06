###############################################################
# import python libraries
###############################################################
import streamlit as st
from streamlit_image_comparison import image_comparison

# Rest of your Streamlit code
###############################################################
# page info 
###############################################################

def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(https://img.zcool.cn/community/01f8905d3ac544a80120695c7fce56.jpg@2o.jpg);
            background-size: cover;
            filter: contrast(0.8);
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()


###############################################################
# page content
###############################################################

st.header("Comparison between maps")


image_comparison(
    img1="./images/map1.png", # local image 1
    img2="./images/map2.png", # local image 2
    label1="historical map",  
    label2="modern map",
    width=800,
    starting_position=50,
    show_labels=True,
    make_responsive=True,
    in_memory=True,
)

########

st.markdown('<p style="color: blue;">The correspondence between the three locations in two maps：</p>', unsafe_allow_html=True)
st.markdown('<p style="color: blue;">(1) Qingqiu: present-day Heze, Shandong </p>', unsafe_allow_html=True)
st.markdown('<p style="color: blue;">(2) Da Ren Guo: present-day Dawenkou Site，which in Tai’an, Shandong </p>', unsafe_allow_html=True)
st.markdown('<p style="color: blue;">(3) Bohai Sea: present-day Beibu Gulf </p>', unsafe_allow_html=True)
st.markdown("---")
st.header("References")
st.text("王恢. 太平寰宇記索引. 影印版. 台北: 文海出版社, 1975.")
st.text("刘宗迪.海上有一个大人国[J].读书,2020(12):113-121.")
st.text("范晔. 后汉书. 西安: 太白文艺出版社, 2006.")


