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
📓 1. Artificial Neural Networks
</div>
""", unsafe_allow_html=True)

# Define the file path with regular spaces
path_to_html = "Artificial_Neural_Networks.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Artificial Neural Networks]")
    st.markdown("""Hi guys. Welcome to the first lecture of Deep Learning series. We are going to start right from the 
                   basics which brings us to 'Artificial Neural Networks (ANN)'. Today we are going to understand how to 
                   create a ANN model, how to compile, fit & evaluate it subsequently. 
                    We are going to work on 'pima-indians-diabetes' dataset and hence I would request you guys to download 
                    it to get started. Click on the button below to download the csv file.
                    In the notebook below I have used a link to fetch the dataset, alternatively you can copy the link as well.
                    Right click on the Download link button and click on 'Copy Link'.""")
    
    df = pd.read_csv("pima-indians-diabetes.csv")
    
    def download_csv():
        df.to_csv("pima-indians-diabetes.csv", index=False)
        with open("pima-indians-diabetes.csv", "rb") as f:
            data = f.read()
        return data

    # Create a download button
    button_label = ":violet[Download CSV]"
    button_download = st.download_button(label=button_label, data=download_csv(), file_name='pima-indians-diabetes.csv', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    st.write("[:violet[Download link >]](https://raw.githubusercontent.com/slmsshk/pima-indians-diabetes.data.csv/main/pima-indians-diabetes.csv)")

    st.write("---")
    st.components.v1.html(html_data, width=1000, height=23285)

    def download_notebook():
        with open("Artificial_Neural_Networks.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Artificial Neural Networks' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Artificial_Neural_Networks.ipynb", mime='application/x-ipynb+json')
    