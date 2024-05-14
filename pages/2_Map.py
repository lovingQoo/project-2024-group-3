###############################################################
# import python libraries
###############################################################
import streamlit as st
from streamlit_image_comparison import image_comparison
import base64

# Rest of your Streamlit code
###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Map -  HUMA5630-Digital Humanities - project-2024-group-3",
    page_icon="🌍", 
  
)
def add_bg_from_local():
    image_path = "./images/background.jpg"  # 根据实际文件路径进行修改
    with open(image_path, 'rb') as f:
        image_data = f.read()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{base64.b64encode(image_data).decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


add_bg_from_local()
st.caption("HUMA5630 Digital Humanities - Group 3")

###############################################################
# page content
###############################################################

st.header("Comparison Between Maps")


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
st.header("Introduction")
st.markdown("“The Classic of Mountains and Seas” is an important ancient Chinese geographical and cultural work that records a vast amount of mythological legends, geographical information, and ancient people's understanding of the natural environment.") 
st.markdown("The correspondence between the geographical records in this book and modern geography can be attributed to the following reasons:")
st.markdown('<p style="color: blue;">（1）Correspondence of geographical features</p>', unsafe_allow_html=True)
st.markdown('<p style="color: blue;">（2）Correspondence of place names</p>', unsafe_allow_html=True)
st.markdown('<p style="color: blue;">（3）Correspondence to the perception of the natural environment</p>', unsafe_allow_html=True)
st.markdown("It’s important to note that the geographical descriptions in the “The Classic of Mountains and Seas” are not entirely accurate or scientific. They include a significant amount of mythology, legends, and allegorical elements.")
st.markdown("Therefore, when correlating the “The Classic of Mountains and Seas” with modern geography, it is necessary to interpret and select the information appropriately, distinguishing the real geographical information from the mythological elements.")
st.markdown("---")
st.header('The correspondence between the three locations in two maps')
st.markdown('<p style="color: blue;"> (1) Qingqiu: present-day Heze, Shandong </p>', unsafe_allow_html=True)
st.markdown('<p style="color: blue;"> (2) Da Ren Guo: present-day Dawenkou Site，which in Tai’an, Shandong </p>', unsafe_allow_html=True)
st.markdown('<p style="color: blue;"> (3) Bohai Sea: present-day Bohai Bay </p>', unsafe_allow_html=True)
st.markdown("---")
st.header("References")
st.markdown("王恢. 太平寰宇記索引. 影印版. 臺北: 文海出版社, 1975.")
st.markdown("劉宗迪.《山海經》的尺度[J].讀書,2019(06):3-13.")
st.markdown ("劉宗迪.海上有一個大人國[J].讀書,2020(12):113-121.")
st.markdown("《山海經》地圖，取自https://www.bilibili.com/video/BV1bu411b7q5/?spm_id_from=333.337.search-card.all.click&vd_source=6ef399ad76fd342687e206adca6b4d8f")
st.markdown("背景插圖:https://img.zcool.cn/community/01f8905d3ac544a80120695c7fce56.jpg@2o.jpg")


