import streamlit as st 
from PIL import Image
import base64

st.set_page_config(page_title ="Special Gift 🎉", page_icon = "🎂",layout = "centered")

st.title('✨🎊 Happy Birthday! 🎊✨')

with open("birthday.mp3",'rb') as f:
    audio_bytes = f.read()
audio_base64 = base64.b64encode(audio_bytes).decode()  
audio_html = f"""
<audio autoplay loop>
   <source src = "data:audio/mp3;base64,{audio_base64}" type = "audio/mp3">
   </audio>
   """
st.markdown(audio_html,unsafe_allow_html = True)
image = Image.open("harry.png")
st.image(image,caption = ' # A Good Friend ❤️',use_container_width=True)

st.markdown("""
 ## 🎂 Wishing you a best birthday ever!.\n
     Keep smiling and shining always ❤️.             
            """)

st.markdown('---')
st.markdown("""
### 🎊 'May this year bring you closer to your dreams'. 
 """)


st.balloons() 
