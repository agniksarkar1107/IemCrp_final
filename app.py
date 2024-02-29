import streamlit as st 
from PIL import Image

im = Image.open('earth-icon-world-symbol-thin-line-icon-on-white-background-for-graphics-and-web-design-illustration-free-vector.jpg')
im1 = Image.open('WhatsApp Image 2024-02-29 at 18.53.55.jpeg')
st.set_page_config( page_title="IemCrp Result", page_icon = im ,layout="wide")  


new_image = im1.resize((900, 600))
   


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)  
st.header("GET IEMCRP RESULT LINK")
st.image(new_image, caption='Scan and pay Rs.31 to redirect you to the link')

btn = st.button("Redirect me to the link")

if btn:
       webbrowser.open(f"https://unsplash.com/s/photos/gay-love")
  
