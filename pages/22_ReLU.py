import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd
import zipfile

from sidebar_logo import add_sidebar_logo, load_css, add_page_title_auto

# Set page configuration
st.set_page_config(
    layout="wide"
)

add_sidebar_logo()
load_css()
# add_page_title_auto()

st.markdown("""
<div style="
    font-size: 1.9rem;
    font-weight: 800;
    background: linear-gradient(135deg, #a78bfa, #818cf8, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Poppins', sans-serif;
">
📓 4. ReLU (Non Linear Activation function)
</div>
""", unsafe_allow_html=True)



def create_zip():
        with zipfile.ZipFile('helper_ReLU.zip', 'w') as zipf:
            for root, dirs, files in os.walk('helper_ReLU'):
                for file in files:
                    zipf.write(os.path.join(root, file), file)
        with open("helper_ReLU.zip", "rb") as f:
            data = f.read()
        return data


# Define the file path with regular spaces
path_to_html = "C2_ReLU.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Getting familar with Jupyter notebook]")
    st.markdown(""" In our very first lecture we understood how we could train a model on Linear data. Simple and efficient.
                    However, the Single Layer Neuron model would fall short if the data is more non linear. Apparently increasing the number 
                    of neurons won't help much here. The only way out is to train the model on the non linear data with some magic. This missing 
                    piece of magic is what we define as a non linear activation function.
                    ReLU (Rectified Linear Unit) is one of such a non linear activation function that is capable enough to train the 
                    model on data complexities. In real world scenarios, not necessarily we might end up getting a linear 
                    correlation between the i/p and o/p parameters everytime and hence to make the model robust enough to handle 
                    non linear data we make use of an activation function sandwiched between 2 layers. Think of it as a catalyst
                    that helps us to get close to the desired o/p, thus reducing the loss.
                    Lastly, don't forget to download helper utils file so that you could visualise the data while you code.""")

    # Create a download button for the zip file
    button_label_zip = ":violet[Download helper utils]"
    button_download_zip = st.download_button(label=button_label_zip, data=create_zip(), file_name='helper_ReLU.zip', mime='application/zip')

    st.write("---")
    st.components.v1.html(html_data, width=1000, height=6800)

    def download_notebook():
        with open("C2_ReLU.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download the 'ReLU' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="ReLU.ipynb", mime='application/x-ipynb+json')