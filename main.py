import streamlit as st
import matplotlib.pyplot as plt
import plotly
import pandas as pd
import pyvis
import numpy



st.set_page_config(
    page_title="Nathan's Home",
    page_icon=":pirate_flag:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        # 'Get Help': 'https://www.extremelycoolapp.com/help',
        # 'Emoji': "https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app",
        'About': "# This is a header. This is an *extremely* cool app!",
    }
)


def welcome():
    st.title(":pirate_flag: Welcome :pirate_flag:")

    st.image("https://static.streamlit.io/examples/cat.jpg", width=500)






pg = st.navigation([
    st.Page(welcome, title="Welcome", icon=":material/favorite:"),
    st.Page("./pages/page1.py", title="First page", icon="🔥"),
    
])
pg.run()
