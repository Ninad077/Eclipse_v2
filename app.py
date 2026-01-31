import streamlit as st
import webbrowser as web
import streamlit.components.v1 as components
from st_pages import Page, Section, show_pages, add_page_title
from streamlit_option_menu import option_menu

from sidebar_logo import add_sidebar_logo, load_css

# Set page configuration
st.set_page_config(
    page_title=":violet[Eclipse]",layout="wide",
    initial_sidebar_state="expanded"
)

add_sidebar_logo()
load_css()

# Add custom CSS for enhanced styling
st.markdown("""
<style>
    /* Fix blurry widgets - Remove backdrop blur and improve text rendering */
    * {
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
        text-rendering: optimizeLegibility !important;
    }
    
    /* Hide default Streamlit header */
    header {
        visibility: hidden;
    }
    
    /* Navigation Bar Styling */
    .nav-container {
        position: sticky;
        top: 0;
        z-index: 999;
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 2px solid rgba(139, 92, 246, 0.3);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        padding: 0;
        margin: -5rem -5rem 2rem -5rem;
    }
    
    /* Hero Section Styling - Crisp and clear */
    .main-header {
        text-align: center;
        padding: 2.5rem 0;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 50%, rgba(240, 147, 251, 0.15) 100%);
        border-radius: 24px;
        margin-bottom: 2rem;
        border: 2px solid rgba(139, 92, 246, 0.4);
        box-shadow: 0 12px 40px rgba(139, 92, 246, 0.3);
        backdrop-filter: none;
    }
    
    .main-header h1 {
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none;
    }
    
    .main-header p {
        font-size: 1.4rem;
        color: #CBD5E1;
        margin-top: 1rem;
        font-weight: 500;
    }
    
    /* Welcome Card */
    .welcome-card {
        background: rgba(30, 41, 59, 0.8);
        padding: 2.5rem;
        border-radius: 24px;
        border: 2px solid rgba(139, 92, 246, 0.3);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
        margin: 2rem 0;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .welcome-card:hover {
        border-color: rgba(139, 92, 246, 0.6);
        box-shadow: 0 20px 60px rgba(139, 92, 246, 0.3);
        transform: translateY(-5px);
    }
    
    /* Link Cards */
    .link-card {
        display: inline-block;
        padding: 1rem 2rem;
        margin: 0.5rem;
        background: rgba(30, 41, 59, 0.8);
        border-radius: 16px;
        border: 2px solid rgba(139, 92, 246, 0.3);
        transition: all 0.3s ease;
        text-decoration: none;
        color: #F1F5F9;
        font-weight: 600;
    }
    
    .link-card:hover {
        border-color: rgba(139, 92, 246, 0.8);
        background: rgba(139, 92, 246, 0.2);
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.4);
    }
    
    /* Query Box Styling */
    .query-box-container {
        background: rgba(30, 41, 59, 0.8);
        padding: 2.5rem;
        border-radius: 24px;
        border: 2px solid rgba(139, 92, 246, 0.3);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
        margin: 2rem 0;
        backdrop-filter: blur(10px);
    }
    
    /* Social Icons Container */
    .social-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    
    /* Floating Animation */
    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    
    /* Glow Effect - Reduced for clarity */
    .glow {
        text-shadow: 0 0 8px rgba(139, 92, 246, 0.3);
    }
    
    /* Sidebar Logo Styling */
    [data-testid="stSidebar"] {
        position: relative;
    }
    
    /* Add logo to sidebar top */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0 !important;
    }
    
    /* Sidebar content alignment */
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        padding: 0 1rem;
    }
    
    /* Better content alignment - use more screen space */
    .main .block-container {
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 98% !important;
    }
    
    /* Better alignment for wide layout */
    .main {
        padding-left: 0.5rem;
        padding-right: 0.5rem;
    }
    
    /* Make content fill screen better */
    @media (min-width: 1200px) {
        .main .block-container {
            max-width: 97% !important;
        }
    }
    
    /* Fix option menu blur */
    [data-baseweb="select"] {
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
    }
    
    /* Ensure all text is crisp */
    body, .stApp {
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
        text-rendering: optimizeLegibility !important;
    }
</style>
""", unsafe_allow_html=True)

# Navigation Bar at the top
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
selected_page = option_menu(
    menu_title=None,
    options=["Preprocessing", "Supervised ML", "Unsupervised ML", 
             "Reinforcement ML", "Deep Learning", "Pytorch"],
    icons=["🐍", "📈", "🧿", "⏰", "🧠", "🔮"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0", "background-color": "transparent"},
        "icon": {"color": "#C4B5FD", "font-size": "1.2rem"},
        "nav-link": {
            "font-size": "1rem",
            "text-align": "center",
            "margin": "0",
            "padding": "1rem 1.5rem",
            "color": "#CBD5E1",
            "font-weight": "600",
            "border-radius": "0",
            "transition": "all 0.3s ease",
        },
        "nav-link-selected": {
            "background": "linear-gradient(135deg, rgba(139, 92, 246, 0.3) 0%, rgba(59, 130, 246, 0.3) 100%)",
            "color": "#F1F5F9",
            "border-bottom": "3px solid #8B5CF6",
        },
    }
)
st.markdown('</div>', unsafe_allow_html=True)

# Add ONLY text-based logo to sidebar - NO IMAGE
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo-fixed">
        <div style="font-size: 2.8rem; font-weight: 800;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                    background-clip: text; font-family: 'Poppins', sans-serif;">
            🌙 Eclipse
        </div>
    </div>
    """, unsafe_allow_html=True)

# Hero Section - Crisp and Clear with Better Appeal
st.markdown("""
<div class="main-header" style="margin: 0 auto; max-width: 100%;">
    <h1 style="margin-bottom: 0.5rem;">🚀 Welcome to Eclipse</h1>
    <p style="font-size: 1.4rem; margin-top: 0.5rem;">Learn Machine Learning with Fun & Ease! 🎓✨</p>
    <div style="margin-top: 1.5rem; display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <span style="background: rgba(139, 92, 246, 0.2); padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; color: #C4B5FD;">
            🎯 Step-by-Step Learning
        </span>
        <span style="background: rgba(59, 130, 246, 0.2); padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; color: #93C5FD;">
            📚 Free Resources
        </span>
        <span style="background: rgba(236, 72, 153, 0.2); padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; color: #F9A8D4;">
            💡 Hands-On Practice
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Show pages based on selection
if selected_page == "Preprocessing":
    show_pages([
        Page("app.py", "Eclipse",""),

        # Preprocessing Section
        Page("pages/1_Jupyter_Notebook_Introduction.py","Jupyter notebook Introduction", icon="🐍"),
        Page("pages/2_Python_basics.py","Python basics", icon="🐍"),
        Page("pages/3_Null_value_treatment.py","Null value treatment", icon="🐍"),
        Page("pages/4_EDA.py","Exploratory Data Analysis", icon="🐍"),
        Page("pages/5_Outliers_and_Correlation.py","Outliers & Correlation", icon="🐍"),

        Page("pages/Contact_me.py", in_section=False),
    ])

elif selected_page == "Supervised ML":
    show_pages([
        Page("app.py", "Eclipse",""),

        # Supervised ML section
        Page("pages/6_Linear_Regression.py","Linear Regression", icon="📈"),
        Page("pages/7_Logistic_Regression.py","Logistic Regression", icon="📈"),
        Page("pages/8_KNN.py","KNN", icon="📈"),
        Page("pages/9_Support_Vector_Machine.py","Support Vector Machine", icon="📈"),
        Page("pages/10_Decision_Tree.py","Decision Tree", icon="📈"),

        Page("pages/Contact_me.py", in_section=False),
    ])

elif selected_page == "Unsupervised ML":
    show_pages([
        Page("app.py", "Eclipse",""),

         # Unsupervised ML section
        Page("pages/11_K_means_clustering.py","K means clustering", icon="🧿"),
        Page("pages/12_Hierarchical_clustering.py","Hierarchical clustering", icon="🧿"),

        Page("pages/Contact_me.py", in_section=False),
    ])

elif selected_page == "Reinforcement ML":
    show_pages([
        Page("app.py", "Eclipse",""),

         # Reinforcement ML section
        Page("pages/13_Time_series_analysis.py","Time Series Analysis", icon="🧿"),

        Page("pages/Contact_me.py", in_section=False),
    ])

elif selected_page == "Deep Learning":
    show_pages([
        Page("app.py", "Eclipse",""),

        # Deep Learning section
        Page("pages/14_Artificial_Neural_Networks.py","Artificial Neural Networks", icon="🧠"),
        Page("pages/15_CNN.py","Convolutional Neural Networks", icon="🧠"),
        Page("pages/16_TFIDF.py","NLP-TFIDF", icon="🧠"),
        Page("pages/17_RASA.py","NLP-RASA", icon="🧠"),
        Page("pages/18_Sentiment_analysis.py","NLP-Sentiment Analysis", icon="🧠"),

        Page("pages/Contact_me.py", in_section=False),
    ])

elif selected_page == "Pytorch":
    show_pages([
        Page("app.py", "Eclipse",""),

        # Deep Learning section
        Page("pages/19_Single_layer_neuron_model.py","Single layer neuron model", icon="🔮"),

         Page("pages/20_Tensor_operations.py","Tensor operations", icon="🔮"),

        Page("pages/Contact_me.py", in_section=False),
    ])

st.write("---")
# Welcome Card
st.markdown("""
Hi, Ninad here!

**Eclipse** is an open source web application designed by me to teach Machine Learning. It spans through core Python
                Preprocessing, Machine Learning & Deep Learning models step by step in a way that even a layman would understand. Rest assured, I have tried to 
                break down complex concepts with simple examples so that the user gets a clear picture of everything. I would recommend the user 
                to start following the course from the first session and follow it religiously till the last one. To make things easy for the user, 
                I have divided the lecture series into multiple sections namely Python Preprocessing, Supervised ML, Unsupervised ML, Reinforcement
                ML, Deep Learning & Pytorch.
                I have enclosed the essential datasets and Jupyter notebooks in every session so that people can refer and practice at their own comfort 
                at home. We would be using Jupyter notebooks to code and the language used is Python. I would give you a brief introduction to Jupyter notebbok 
                and get you familiar with Jupyter notebook environment on Anaconda navigator. For the entire lecture series, I would recommend you to download 
                Anaconda environment & Jupyter notebook on your local PC first. I have enclosed some installation blogs in the links down below, please go through
                them and install the setup first. Other non-technical prerequisites you need are: **Passion & curiosity**. Be passionate & be curious about the
                things to learn & don't be intimidated if you don't understand something. Machine learning requires practice and with time you would be proficient. 
                My only advice to you is that, make your foundations about the core concepts very clear which would prepare you to learn more advanced concepts in 
                future with ease. The entire Machine Learning is taught using several libraries most important being scikit learn, pandas, numpy, matplotlib, seaborn & most
                importantly torch. 
                On the other hand, the most important Library used in Deep Learning is tensorflow/torch. So once you learn the basics well, try implementing projects using these 
                libraries so that you get well versed in them with time. Also, I am of the opinion that learning something is no less than implementing a Machine 
                Learning algorithm, the more you train, the better would be results. So keep practicing every day.
                I have kept this application open source because in the era of MOOCs which do charge subscription, I  don't want to make money an impediment for someone
                who has the zeal within him or her to learn something new. 
                For any query related to Machine Learning feel free to text me in the Query box below. To get started, select a Section from the navigation bar above and 
                follow the lecture series listed in the sidebar (extreme left of your screen).
                Hope you will have fun!
                Happy Learning! 🎉✨""")

st.write("---")

# Installation Links with Cards
st.markdown("### 📥 Installation Guides")
st.markdown("""
<div style="display: flex; justify-content: center; gap: 1rem; margin: 1rem 0; flex-wrap: wrap;">
    <a href="https://www.geeksforgeeks.org/how-to-install-anaconda-on-windows/" target="_blank" class="link-card">
        📦 Install Anaconda
    </a>
    <a href="https://www.geeksforgeeks.org/install-jupyter-notebook-in-windows/" target="_blank" class="link-card">
        📓 Install Jupyter Notebook
    </a>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Query Box with Enhanced Styling
st.markdown("### 💬 Query Box")
st.markdown("Have questions? Drop me a message! Would love to help you on your ML journey! 🚀") 
contact_form = """<form action="https://formsubmit.co/ninadmandavkar28@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder= "Your name" required>
    <input type="email" name="email" placeholder= "Your email" required>
    <textarea name="message" placeholder="Your message"></textarea>
    <button type="submit">Send</button>
    </form>"""

st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css.txt")

# Social Media Links with Enhanced Styling
st.write("---")
st.markdown("### 🌐 Connect with Me")
st.markdown('<div class="social-container">', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)