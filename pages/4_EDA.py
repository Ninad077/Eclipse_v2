import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

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
📓 4. Exploratory Data Analysis (EDA)
</div>
""", unsafe_allow_html=True)


# Define the file path with regular spaces
path_to_html = "EDA.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Exploratory Data Analysis (EDA)]")
    st.markdown("""Hi guys. Today we are going to learn some basic EDA (Exploratory Data Analysis). EDA is generally performed on data to generate visualizations. Today we are going 
                   to see how one can generate line charts, bar plots using seaborn & matplotlib libraries. There would be more EDA in the coming sessions and you will get the hang of 
                   it slowly as we proceed with the algorithms. For now, I just want you guys to be aware of what exactly EDA is and how Data Scientists/ML engineers perform EDA. Please 
                   download 'tips' dataset before we start the session. The entire EDA will be performed on this dataset. So, let's get started.""")
    
    df = pd.read_csv("tips.csv")
    
    def download_csv():
        df.to_csv("tips.csv", index=False)
        with open("tips.csv", "rb") as f:
            data = f.read()
        return data

    # Create a download button
    button_label = ":violet[Download CSV]"
    button_download = st.download_button(label=button_label, data=download_csv(), file_name='tips.csv', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    st.write("---")
    st.components.v1.html(html_data, width=1000, height=7500)

    def download_notebook():
        with open("EDA.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'EDA' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="EDA.ipynb", mime='application/x-ipynb+json')
    
