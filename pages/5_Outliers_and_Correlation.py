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
📓 5. Outliers & Correlation
</div>
""", unsafe_allow_html=True)

# Define the file path with regular spaces
path_to_html = "Outliers_and_Correlation.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Outliers & Correlation]")
    st.markdown("""Hi guys. As of now we have understood how to do Null Value Treatment & how to perform EDA, now let us move on to the next step of Preprocessing which is checking 'Outliers' & 'Correlation'.
                   Before performing Machine Learning, it is important to make sure we have no outliers in data and one has to check dependency in columns to avoid any bias. So checking correlations and 
                   eliminating Outliers is one of the crucial parts of Data preprocessing. Data Scientists normally make use of boxplot and heatmap to check Outliers & Correlations respectively. Now let us
                   see how one does it practically using libraries. Before that, please download 'advertising.csv' dataset. Having said that, let us start with the session.""")
    
    df = pd.read_csv("advertising.csv")
    
    def download_csv():
        df.to_csv("advertising.csv", index=False)
        with open("advertising.csv", "rb") as f:
            data = f.read()
        return data

    # Create a download button
    button_label = ":violet[Download CSV]"
    button_download = st.download_button(label=button_label, data=download_csv(), file_name='advertising.csv', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    st.write("---")
    st.components.v1.html(html_data, width=1000, height=8500)

    def download_notebook():
        with open("Outliers_and_Correlation.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Outliers & Correlation' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Outliers_and_Correlation.ipynb", mime='application/x-ipynb+json')
    
