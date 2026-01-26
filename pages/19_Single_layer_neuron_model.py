import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

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
📓 1. Single Layer Neuron Model
</div>
""", unsafe_allow_html=True)


# Define the file path with regular spaces
path_to_html = "C1_code.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Getting familar with Jupyter notebook]")
    st.markdown("""Now that you know how fundamentally Deep Learning works, let us deep dive into one of the most 
                   popular DL frameworks: Pytorch. Pytorch is widely popular Python based framework which heavily focuses on building 
                   Deep Learning applications.
                   Pytorch make use of 'torch' library to perform operations. To make it more precise, today we are going to 
                   understand how we make use of 'nn' & 'optim' methods to train, estimate loss parameters & compute optimizer.
                   This would help us to first traina Single layer neuron model and then help us to predict output based on any 
                   input value. So let us get started!""")
    st.write("---")
    st.components.v1.html(html_data, width=1000, height=3300)

    def download_notebook():
        with open("C1_code.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Jupyter introduction' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Single_layer_neuron_model.ipynb", mime='application/x-ipynb+json')