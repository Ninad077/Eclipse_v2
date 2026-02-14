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
📓 3. Tensor Arithmetics
</div>
""", unsafe_allow_html=True)


# Define the file path with regular spaces
path_to_html = "C4_Tensor_Arithmetics.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Getting familar with Jupyter notebook]")
    st.markdown("""Now that we know some basic Tensor operations, let us also understand how Tensors compute the values.
                   Computational operators used in torch revolve around Arithmetic & Logical operators. Hence
                   a foundational understanding of both the operators is equally significant. 
                   Additionally, we will also try to understand what Broadcasting is and how it helps in computation,
                   especially in the scenarios where we want to compute values on Tensors with different shapes.
                   Moreover, I have also briefly introduced Statistical operators as well, which will help us in estimating 
                   the statistical means & standard deviations for a tensor with ease. So let's dive into this chapter.""")
    st.write("---")
    st.components.v1.html(html_data, width=1000, height=3400)

    def download_notebook():
        with open("C4_Tensor_Arithmetics.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download the 'Tensor Arithmetics' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Tensor_Arithmetics.ipynb", mime='application/x-ipynb+json')