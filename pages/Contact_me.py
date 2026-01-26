import requests
import streamlit as st
from PIL import Image
import webbrowser as web
import streamlit.components.v1 as components

from sidebar_logo import add_sidebar_logo, load_css

# Set page configuration
st.set_page_config(
    layout="wide"
)

add_sidebar_logo()
load_css()

st.markdown("""
<div style="
    font-size: 1.9rem;
    font-weight: 800;
    background: linear-gradient(135deg, #a78bfa, #818cf8, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Poppins', sans-serif;
">
👤 About Me
</div>
""", unsafe_allow_html=True)


# ---- HEADER SECTION ----
st.markdown("""
<div class="main-header">
    <h1 class="glow">👋 Howdy, I'm Ninad!</h1>
    <p style="font-size: 1.2rem; color: #CBD5E1; margin-top: 1rem;">
        Weirdly passionate about Maths, Machine Learning & programming 🚀
    </p>
    <a href="https://www.linkedin.com/in/ninad-s-mandavkar-12328715b/" target="_blank" class="link-card" style="margin-top: 1rem;">
        Learn More About Me →
    </a>
</div>
""", unsafe_allow_html=True)
    

# ---- ABOUT ME ----
st.write("---")

left_column, right_column = st.columns(2)

with left_column:
    st.markdown('<div class="welcome-card">', unsafe_allow_html=True)
    st.markdown("### 👨‍💻 About Me")
    st.markdown("""
    Let me give a brief introduction of myself. I am **Ninad**. A Master's graduate from **TU Ilmenau, Germany**. 
    
    I love to code, deploy ML algorithms and play around with data. Maths is something that I was always enamoured by and apparently the prime reason for my inclination towards Data Science as a field. 
    
    I am equally curious about leveraging Deep Learning, NLPs & AI as a tool to enhance productivity in the workforce. 
    
    **I strongly believe in being passionate, curious & resilient.** 
    
    Nuf' said, to know more about me do visit my social media handles below. Also, for official queries one can drop me a mail.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 🌐 Check out my profile")
    components.html("""
    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
        <a href="https://github.com/Ninad077" target="_blank" style="transition: transform 0.3s ease;">
            <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" 
                 onmouseover="this.style.transform='scale(1.1)'" 
                 onmouseout="this.style.transform='scale(1)'"
                 style="border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
        </a>
        <a href="https://www.linkedin.com/in/ninad-s-mandavkar-12328715b" target="_blank" style="transition: transform 0.3s ease;">
            <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" 
                 onmouseover="this.style.transform='scale(1.1)'" 
                 onmouseout="this.style.transform='scale(1)'"
                 style="border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
        </a>
        <a href="https://medium.com/@ninadmandavkar28" target="_blank" style="transition: transform 0.3s ease;">
            <img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" 
                 onmouseover="this.style.transform='scale(1.1)'" 
                 onmouseout="this.style.transform='scale(1)'"
                 style="border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
        </a>
    </div>
    """, height=60)

with right_column:
    st.markdown('<div class="floating">', unsafe_allow_html=True)
    st.image('Ninad_photo.jpeg')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown('<div class="query-box-container">', unsafe_allow_html=True)
    st.markdown("### 💬 Get in touch with me!")
    st.markdown("Have a question or want to collaborate? Feel free to reach out! 🚀")
    
    contact_form = """<form action="https://formsubmit.co/ninadmandavkar28@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder= "Your name" required>
    <input type="email" name="email" placeholder= "Your email" required>
    <textarea name="message" placeholder="Your message"></textarea>
    <button type="submit">Send Message</button>
    </form>"""

    st.markdown(contact_form,unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css.txt")