import streamlit as st




def welcome():
    st.write('Hello World!')

    st.image('https://images.unsplash.com/photo-1734532873375-574fd74045c5?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')






pg = st.navigation([
    st.Page(welcome, title="Welcome", icon=":material/favorite:"),
    st.Page("./pages/page1.py", title="First page", icon="🔥"),
    
])
pg.run()
