# Import des librairies
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel

### CONFIG
st.set_page_config(
    page_title="Understand data",
    page_icon="🚗",
    layout="wide"
)

### TITLE AND TEXT
st.title("Understanding your data")
st.markdown("This dashboard allow you to have wide view on your activity. You can use as an help to decision making.")
# Logo avant le menu
logo = "https://lever-client-logos.s3.amazonaws.com/2bd4cdf9-37f2-497f-9096-c2793296a75f-1568844229943.png"
st.sidebar.image(logo)

### LOAD AND CACHE DATA
@st.cache_data
def load_data():
    data = pd.read_csv('src/retards.csv', thousands=None)
    return data

commandes = load_data()

st.markdown('## Data')
st.dataframe(commandes.head())

commandes_doc = pd.read_csv('src/documentation.csv')
st.dataframe(commandes_doc)