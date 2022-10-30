import streamlit as st
import os
from io import BytesIO
from io import StringIO
from io import TextIOWrapper
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import math



def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")
    
def ePCR():
    st.markdown("# ePCR viewer ❄️")
    st.sidebar.markdown("# ePCR viewer ❄️")
    
def Araya():
    st.markdown("# Araya calibration 🎉")
    st.sidebar.markdown("# Araya verification 🎉")
    
    
page_names_to_funcs = {
    "Main Page": main_page,
    "ePCR_viewer": ePCR,
    "Araya_comparison": Araya,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
