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
📓 2. Tensor Operations
</div>
""", unsafe_allow_html=True)


# Define the file path with regular spaces
path_to_html = "C3_Tensor_operations.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Getting familar with Jupyter notebook]")
    st.markdown("""Before we get down to train some more neuron models, let us first get the hang of basic Tensor 
                   operations.
                   Some of the major operations being Indexing, Slicing, Reshaping, Squeezing/Unsqueezing, concatenating a tensor
                   and much more. Now that I am skimmimg the operations above, it does sound look I am metaphoring tensor as a fruit. :)
                   Wasn't that funny right? Anyways, moving on! So guys if you could recollect we used Data prepocessing as precursor to
                   ML, similarly in Pytorch for ML we consider Tensor operations as a preprocessing step. So it is very important that you 
                   deeply understand the concepts taught today and get your foundations clear.
                   Goes without saying, you could find the notebook with the entire code once you click on Download button, but before that
                   lets understand the anatomy of a Tensor well.""")
    st.write("---")
    st.components.v1.html(html_data, width=1000, height=11500)

    def download_notebook():
        with open("C3_Tensor_operations.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download the 'Tensor Operations' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Tensor_operations.ipynb", mime='application/x-ipynb+json')