"""
Sidebar Logo Helper for Eclipse ML Platform
Add this to all your pages to show the Eclipse logo in the sidebar
"""

import streamlit as st
import os

# Map of page names to their emoji (descriptions removed)
PAGE_CONFIG = {
    # Preprocessing
    "Jupyter notebook Introduction": {"emoji": "📓"},
    "Python basics": {"emoji": "🐍"},
    "Null value treatment": {"emoji": "🧹"},
    "Exploratory Data Analysis": {"emoji": "📊"},
    "Outliers & Correlation": {"emoji": "📉"},
    
    # Supervised ML
    "Linear Regression": {"emoji": "📈"},
    "Logistic Regression": {"emoji": "📊"},
    "KNN": {"emoji": "🎯"},
    "Support Vector Machine": {"emoji": "🤖"},
    "Decision Tree": {"emoji": "🌳"},
    
    # Unsupervised ML
    "K means clustering": {"emoji": "🧿"},
    "Hierarchical clustering": {"emoji": "🔮"},
    
    # Reinforcement ML
    "Time Series Analysis": {"emoji": "📈"},
    
    # Deep Learning
    "Artificial Neural Networks": {"emoji": "🧠"},
    "Convolutional Neural Networks": {"emoji": "🖼️"},
    "NLP-TFIDF": {"emoji": "📝"},
    "NLP-RASA": {"emoji": "💬"},
    "NLP-Sentiment Analysis": {"emoji": "😊"},
    
    # Default
    "Eclipse": {"emoji": "🌙"},
    "Contact Me": {"emoji": "📧"},
}


def add_sidebar_logo():
    """
    Adds the Eclipse logo to the sidebar at the top.
    Call this function at the beginning of each page file.
    """
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


def get_current_page_info():
    import sys
    import os

    try:
        page_path = sys.modules["__main__"].__file__
        page_name = os.path.basename(page_path).replace(".py", "")
        page_name = page_name.replace("_", " ").strip().title()
    except Exception:
        page_name = "Eclipse"

    config = PAGE_CONFIG.get(page_name, {"emoji": "🌙"})

    return {
        "title": page_name,
        "emoji": config.get("emoji", "🌙")
    }



def add_page_title_auto():
    page_info = get_current_page_info()

    st.markdown(
        f"""
        <div style="
            position: relative;
            z-index: 10;
            margin: 1.5rem 0 2rem 0;
            padding: 1rem 1.5rem;
            border-radius: 12px;
            background: linear-gradient(
                135deg,
                rgba(30, 41, 59, 0.9),
                rgba(15, 23, 42, 0.9)
            );
            border-left: 4px solid #8b5cf6;
            display: inline-block;
        ">
            <h1 style="
                font-size: 1.9rem;
                font-weight: 800;
                margin: 0;
                background: linear-gradient(
                    135deg,
                    #a78bfa,
                    #818cf8,
                    #f472b6
                );
                background-clip: text;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: 'Poppins', sans-serif;
            ">
                {page_info['emoji']} {page_info['title']}
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )




def add_page_title(emoji, title):
    """
    Adds a beautiful gradient title to the page (manual version).
    Use this if you want to customize the title.
    
    Args:
        emoji: Icon/emoji for the page (e.g., "📓", "🐍", "📈")
        title: Main title of the page
    
    Example:
        add_page_title("📓", "Jupyter Notebook Introduction")
    """
    st.markdown(f"""
    <div style="text-align: center; padding: 1.5rem 1rem; margin: 2rem auto 2rem auto; max-width: 600px;
                background: rgba(30, 41, 59, 0.6);
                border-radius: 12px; 
                border: 1px solid rgba(139, 92, 246, 0.4);
                box-shadow: 0 4px 20px rgba(139, 92, 246, 0.2);">
        <h1 style="font-size: 2rem; font-weight: 800; margin: 0;
                   color: transparent;
                   background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;
                   background-clip: text;
                   font-family: 'Poppins', sans-serif;">
            {emoji} {title}
        </h1>
    </div>
    """, unsafe_allow_html=True)


def add_section_header(emoji, title, description=""):
    """
    Adds a smaller section header within a page.
    
    Args:
        emoji: Icon/emoji for the section
        title: Section title
        description: Optional description
    
    Example:
        add_section_header("🎯", "Getting Started", "Let's dive into the basics")
    """
    st.markdown(f"""
    <div style="padding: 1.5rem; margin: 2rem 0 1.5rem 0;
                background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
                border-radius: 16px; border-left: 4px solid rgba(139, 92, 246, 0.8);
                box-shadow: 0 4px 15px rgba(139, 92, 246, 0.2);">
        <h2 style="font-size: 1.8rem; font-weight: 700; margin-bottom: 0.25rem;
                   color: transparent;
                   background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
                   -webkit-background-clip: text; 
                   -webkit-text-fill-color: transparent;
                   background-clip: text; 
                   font-family: 'Poppins', sans-serif;">
            {emoji} {title}
        </h2>
        {f'<p style="font-size: 1rem; color: #CBD5E1; margin-top: 0.5rem;">{description}</p>' if description else ''}
    </div>
    """, unsafe_allow_html=True)


def load_css():
    """
    Load the custom CSS for Eclipse theme.
    Correct fix: override Streamlit theme variable for download button text.
    """
    try:
        with open("style/style.css.txt") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.markdown("""
        <style>
            /* ===============================
               Fonts
               =============================== */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

            /* ===============================
               Sidebar Styling
               =============================== */
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
                border-right: 2px solid rgba(139, 92, 246, 0.3);
                box-shadow: 4px 0 20px rgba(0, 0, 0, 0.3);
            }

            [data-testid="stSidebar"] > div:first-child {
                padding-top: 0 !important;
            }

            .sidebar-logo-fixed {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                width: 21rem !important;
                height: 140px !important;
                background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%) !important;
                border-bottom: 2px solid rgba(139, 92, 246, 0.3) !important;
                z-index: 999 !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                padding: 1rem !important;
            }

            [data-testid="stSidebarNav"] {
                margin-top: 140px !important;
                padding-top: 1rem !important;
            }

            /* Hide sidebar scrollbar */
            [data-testid="stSidebar"] ::-webkit-scrollbar {
                display: none;
            }

            [data-testid="stSidebar"] {
                -ms-overflow-style: none;
                scrollbar-width: none;
            }

            /* ===============================
               Typography
               =============================== */
            h1, h2, h3, p, span, div {
                font-family: 'Poppins', sans-serif !important;
            }

            /* ===============================
               Eclipse Download Button
               =============================== */
            div[data-testid="stDownloadButton"] {
                /* 🔥 THIS IS THE ACTUAL FIX */
                --primary-color: #ffffff;
            }

            div[data-testid="stDownloadButton"] > button {
                background: linear-gradient(
                    135deg,
                    #8b5cf6 0%,
                    #7c3aed 45%,
                    #ec4899 100%
                ) !important;

                border: none !important;
                border-radius: 12px !important;

                padding: 0.7rem 1.8rem !important;
                box-shadow: 0 6px 20px rgba(139, 92, 246, 0.55) !important;

                font-weight: 800 !important;
                font-size: 1rem !important;

                transition: all 0.25s ease-in-out !important;
            }

            div[data-testid="stDownloadButton"] > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 30px rgba(236, 72, 153, 0.65) !important;
            }

            div[data-testid="stDownloadButton"] > button:focus {
                outline: none !important;
                box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.45) !important;
            }
        </style>
        """, unsafe_allow_html=True)
