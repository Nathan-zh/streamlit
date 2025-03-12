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
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)


def welcome():
    st.write(":pirate_flag: Welcome :pirate_flag:")

    st.image('https://images.unsplash.com/photo-1734532873375-574fd74045c5?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', width=500)






pg = st.navigation([
    st.Page(welcome, title="Welcome", icon=":material/favorite:"),
    st.Page("./pages/page1.py", title="First page", icon="🔥"),
    
])
pg.run()
