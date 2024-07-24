import streamlit as st


#st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("data/images/Cem.jpeg")
    
with col2:
    st.title("Cem Akgul")
    content = """
    Hello, I am Cem! I am a Python developer with focus on Machine Learning/Deep Learning. I have done variety of
    AI projects mainly in the domain of Computer Vision. I graduated in 2020 with a degree of Photonics Engineering at Mechatronics Faculty in WUT.
    """
    st.info(content)
    
content2 = """
Below you an find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)