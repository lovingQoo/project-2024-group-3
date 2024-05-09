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
# page menu and description
###############################################################

from menu import menu
menu(description = """\n\n\nThis page serves as an introduction to the project, showcasing research findings and introducing team members. It also provides access to the menu.
""")
    
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
st.markdown("The research findings of this project demonstrate how modern visualization techniques can be used to explore the content of classic work of Chinese literature. ")
st.markdown("Firstly, this project utilized various techniques, such as word cloud analysis of high-frequency words, annotation on the full text, and full text display, which were visually presented to provide a more intuitive understanding of the text's content. To enhance the reader's comprehension of the Classic, different color blocks were implemented in the text to distinguish attributes of words, such as characters, monsters, treasures, and locations.")
st.markdown("Secondly, the research conducted a more in-depth investigation of the complex distribution of countries and rivers mentioned in the text based on geographical descriptions, thus gaining insight into the ancient mythological world. Furthermore, by drawing maps and comparing them with modern maps, three geographical coordinates were also clarified.")
st.markdown("Thirdly, this project delves into the mythical creatures portrayed in this mythological story, offering a fascinating and distinctive approach to exploring the text's content. This includes examining the quantity and classification of creatures, and utilizing pie charts to illustrate the distribution of creature numbers in each chapter and the proportion of each creature type. Additionally, the page provides original texts and translations of relevant mythical creatures, with the goal of helping readers gain a more vivid comprehension of them.")
st.markdown("*The following section presents the maps, high-frequency words, and the  classification of mythical creatures, allowing you to explore the world of Chinese mythology in a more vivid and complete way.* **Start your adventure now, don't hesitate!**.")
st.title('Group Members and Task Assignment')
st.markdown(" Introduction and Conclusion of the Project--YUAN Yuchen （yyuanbg@connect.ust.hk）")
st.markdown(" Part 1: Textual Analysis--SHEN Xiaohan （xshenas@connect.ust.hk）")
st.markdown(" Part 2: Geographical Analysis--WU Yutong （ywuge@connect.ust.hk）")
st.markdown(" Part 3: Categorization of Mythical Creatures--HAN Xuan （xhanap@connect.ust.hk）")
st.title('References')
st.markdown("Homepage Image:")
st.markdown("1:https://seopic.699pic.com/photo/40216/6112.jpg_wh1200.jpg")
