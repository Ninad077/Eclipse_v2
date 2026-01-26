"""
Navbar Helper for Eclipse ML Platform
Add this to all your pages to show the consistent navigation bar
"""

import streamlit as st
from streamlit_option_menu import option_menu
from st_pages import Page, show_pages

def add_navbar():
    """
    Adds the Eclipse navigation bar to the top of any page.
    Call this function at the beginning of each page file.
    Returns the selected page name.
    """
    # Add navbar CSS
    st.markdown("""
    <style>
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
    </style>
    """, unsafe_allow_html=True)
    
    # Navigation Bar at the top
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    selected_page = option_menu(
        menu_title=None,
        options=["Preprocessing", "Supervised ML", "Unsupervised ML", 
                 "Reinforcement ML", "Deep Learning"],
        icons=["🐍", "📈", "🧿", "⏰", "🧠"],
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
    
    # Update pages based on selection
    update_pages(selected_page)
    
    return selected_page


def update_pages(selected_page):
    """
    Updates the sidebar pages based on the selected navbar option.
    """
    if selected_page == "Preprocessing":
        show_pages([
            Page("app.py", "Eclipse", ""),
            Page("pages/1_Jupyter_Notebook_Introduction.py", "Jupyter notebook Introduction", icon="🐍"),
            Page("pages/2_Python_basics.py", "Python basics", icon="🐍"),
            Page("pages/3_Null_value_treatment.py", "Null value treatment", icon="🐍"),
            Page("pages/4_EDA.py", "Exploratory Data Analysis", icon="🐍"),
            Page("pages/5_Outliers_and_Correlation.py", "Outliers & Correlation", icon="🐍"),
            Page("pages/Contact_me.py", in_section=False),
        ])

    elif selected_page == "Supervised ML":
        show_pages([
            Page("app.py", "Eclipse", ""),
            Page("pages/6_Linear_Regression.py", "Linear Regression", icon="📈"),
            Page("pages/7_Logistic_Regression.py", "Logistic Regression", icon="📈"),
            Page("pages/8_KNN.py", "KNN", icon="📈"),
            Page("pages/9_Support_Vector_Machine.py", "Support Vector Machine", icon="📈"),
            Page("pages/10_Decision_Tree.py", "Decision Tree", icon="📈"),
            Page("pages/Contact_me.py", in_section=False),
        ])

    elif selected_page == "Unsupervised ML":
        show_pages([
            Page("app.py", "Eclipse", ""),
            Page("pages/11_K_means_clustering.py", "K means clustering", icon="🧿"),
            Page("pages/12_Hierarchical_clustering.py", "Hierarchical clustering", icon="🧿"),
            Page("pages/Contact_me.py", in_section=False),
        ])

    elif selected_page == "Reinforcement ML":
        show_pages([
            Page("app.py", "Eclipse", ""),
            Page("pages/13_Time_series_analysis.py", "Time Series Analysis", icon="🧿"),
            Page("pages/Contact_me.py", in_section=False),
        ])

    elif selected_page == "Deep Learning":
        show_pages([
            Page("app.py", "Eclipse", ""),
            Page("pages/14_Artificial_Neural_Networks.py", "Artificial Neural Networks", icon="🧠"),
            Page("pages/15_CNN.py", "Convolutional Neural Networks", icon="🧠"),
            Page("pages/16_TFIDF.py", "NLP-TFIDF", icon="🧠"),
            Page("pages/17_RASA.py", "NLP-RASA", icon="🧠"),
            Page("pages/18_Sentiment_analysis.py", "NLP-Sentiment Analysis", icon="🧠"),
            Page("pages/Contact_me.py", in_section=False),
        ])


def get_navbar_category():
    """
    Returns the current navbar category based on the current page.
    Useful for setting the default selection in the navbar.
    """
    try:
        from st_pages import get_current_page
        current_page = get_current_page()
        page_name = current_page.name if hasattr(current_page, 'name') else ""
        
        # Map pages to categories
        if any(p in page_name.lower() for p in ["jupyter", "python", "null", "eda", "outliers", "correlation"]):
            return "Preprocessing"
        elif any(p in page_name.lower() for p in ["linear", "logistic", "knn", "svm", "support", "decision", "tree"]):
            return "Supervised ML"
        elif any(p in page_name.lower() for p in ["k means", "kmeans", "hierarchical", "clustering"]):
            return "Unsupervised ML"
        elif any(p in page_name.lower() for p in ["time series", "reinforcement"]):
            return "Reinforcement ML"
        elif any(p in page_name.lower() for p in ["neural", "cnn", "tfidf", "rasa", "sentiment", "nlp", "deep"]):
            return "Deep Learning"
    except:
        pass
    
    return "Preprocessing"  # Default