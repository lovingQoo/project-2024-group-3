###############################################################
# import python libraries
###############################################################
import streamlit as st
from streamlit_image_comparison import image_comparison

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Image comparison - Demo code",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

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
st.text("The correspondence between the three locations in two maps")
st.text("(1) Qingqiu: present-day Heze, Shandong")
st.text("(2) Da Ren Guo: present-day Dawenkou Site，which in Tai’an, Shandong")
st.text("(3) Bohai Sea: present-day Beibu Gulf")
