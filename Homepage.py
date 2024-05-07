###############################################################
# import python libraries
###############################################################
import streamlit as st
###############################################################
# page information
###############################################################
st.set_page_config(
    page_title="Homepage -  HUMA5630-Digital Humanities - project-2024-group-3",
    page_icon="🏠",
)

###############################################################
# Background Image
###############################################################
def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(https://p7.itc.cn/q_70/images03/20211111/de94dd6a91af4bf49bcc95630b14d55d.jpeg);
            background-size: cover;
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()

#SideBar color
st.markdown(
        """
        <style>
[data-testid=stSidebar] {
        background-color: #9dc098;
    }
        </style>
        """,
        unsafe_allow_html=True
    )

###############################################################
# page content
###############################################################
st.caption("HUMA5630 Digital Humanities - Group 3")
st.image('./images/homepagepic.jpg')
st.title("A Study of  “The Classic of Mountains and Seas”《山海经》")
st.title('About the Project')
st.markdown(" The primary objective of this project is to utilize modern technology to present the classic Chinese text 'The Classic of Mountains and Sea'. Throughout the spring semester of 2024, the project team employed a diverse range of methods, including but not limited to text analysis, spatial mapping, and data analysis, with the ultimate aim of unraveling the enigmatic tales, intricate river and mountain distributions, and various types of mythical creatures depicted in mysterious work. The ultimate goal of the project is to vividly present these ancient Chinese myths using modern technology, thereby showcasing the captivating allure of China's ancient mythology.")
st.title('Findings')
st.markdown("The research findings of this project demonstrate how modern visualization techniques can be used to explore the content of classic works of Chinese literature. ")
st.markdown("Firstly, by creating maps of the geographical locations mentioned in the text, the project team was able to conduct a more in-depth analysis of the complex river and mountain distributions described in the text, providing a glimpse into the world of ancient mythology. In addition, the team conducted a frequency analysis of the text to identify high-frequency words, which were then visually presented to provide a more intuitive understanding of the text's content.Furthermore, the project team classified and summarized the various types of mythical creatures depicted in this mythological story, providing a unique and captivating way to explore the text's content.  Overall, these findings provide a fresh perspective on classic works of literature through the lens of modern visualization techniques, and make a valuable contribution to the study of Chinese mythology and literature. ")
st.markdown("*The following section presents the maps, high-frequency words, and the  classification of mythical creatures, allowing you to explore the world of Chinese mythology in a more vivid and complete way.* **Start your adventure now, don't hesitate!**.")
st.title('Group Members and Task Assignment')
st.markdown(" Introduction and Conclusion of the Project--YUAN Yuchen （yyuanbg@connect.ust.hk）")
st.markdown(" Part 1: Textual Analysis--SHEN Xiaohan （xshenas@connect.ust.hk）")
st.markdown(" Part 2: Geographical Analysis--WU Yutong （ywuge@connect.ust.hk）")
st.markdown(" Part 3: Categorization of Mythical Creatures--HAN Xuan （xhanap@connect.ust.hk）")


st.page_link("./Homepage.py", label="Home", icon="🏠", )
st.page_link("./pages/1_TxtAnalysis.py", label="Analysis", icon="📖")
st.page_link("./pages/2_Map.py", label="Map", icon="🗺️")
st.page_link("./pages/3_Categorization.py", label="Categorization", icon="⛰️")
