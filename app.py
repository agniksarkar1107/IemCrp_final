import streamlit as st 
from PIL import Image

im = Image.open('earth-icon-world-symbol-thin-line-icon-on-white-background-for-graphics-and-web-design-illustration-free-vector.jpg')
im1 = Image.open('earth-icon-world-symbol-thin-line-icon-on-white-background-for-graphics-and-web-design-illustration-free-vector.jpg')
st.set_page_config( page_title="IemCrp Result", page_icon = im ,layout="wide")  


new_image = im1.resize((150, 100))
   


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)  
  
