import streamlit as st 
from PIL import Image

im = Image.open('')
st.set_page_config( page_title="IemCrp Result", page_icon = im ,layout="wide")  


new_image = im.resize((150, 100))
   


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)  
  
