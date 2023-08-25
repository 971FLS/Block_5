# Import des librairies
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel



### CONFIG
st.set_page_config(
    page_title="Getaround Dashboad",
    page_icon="🚗",
    layout="wide"
  )

### TITLE AND TEXT
st.title("Dashboard")
st.markdown("This dashboard allows you to have wide view on your activity. You can use as an help to decision making.")
# Logo avant le menu
logo = "https://lever-client-logos.s3.amazonaws.com/2bd4cdf9-37f2-497f-9096-c2793296a75f-1568844229943.png"
st.sidebar.image(logo)

### LOAD AND CACHE DATA
@st.cache_data
def load_data():
    data = pd.read_csv('src/retards.csv', thousands=None)
    return data

commandes = load_data()
st.divider()

st.markdown('''
<style>
            div.element-container:nth-child(6){background-color:green; border-radius:10px; padding-left:20px;padding-bottom:10px;}
            #activity span.css-10trblm.e1nzilvr0, #cancelations span.css-10trblm.e1nzilvr0{color:#ffffff}
            div.element-container:nth-child(9){background-color:orange; border-radius:10px; padding-left:20px;padding-bottom:10px;}</style>
'''
, unsafe_allow_html=True)
st.markdown('## Activity')

nb_commandes = commandes.shape[0]
clients_connect = commandes[commandes['checkin_type'] == 'connect'].shape[0]
clients_mobile = commandes[commandes['checkin_type'] == 'mobile'].shape[0]
pourcent_connect = (clients_connect / nb_commandes) * 100
nb_annulations = commandes[commandes['state'] == 'canceled'].shape[0]
pourcent_canceled = nb_annulations*100 / nb_commandes

col1,col2,col3 = st.columns(3)

col1.metric('Orders',int(nb_commandes))
col2.metric('Connect customers',int(clients_connect))
col3.metric('Mobile customers',int(clients_mobile))
st.divider()


st.markdown('## Cancelations')

annulations = commandes[commandes['state'] == 'canceled']
nb_annulations = len(annulations)
annulations_connect = annulations[annulations['checkin_type'] == 'connect'].shape[0]
annulations_mobile = annulations[annulations['checkin_type'] == 'mobile'].shape[0]
pourcent_connect = (clients_connect / nb_commandes) * 100
nb_annulations = commandes[commandes['state'] == 'canceled'].shape[0]
pourcent_canceled = nb_annulations*100 / nb_commandes

col4,col5,col6 = st.columns(3)

col4.metric('Lost orders',int(nb_annulations))
col5.metric('Connect cancelations',int(annulations_connect))
col6.metric('Mobile cancelations',int(annulations_mobile))
st.divider()

st.markdown('<style>#root{background-color:#000000;}.css-u0yi3i{background-color:#86e3e9;border-radius:30px;padding:30px;text-align:center;}div.css-16idsys.e1nzilvr4 p{text-align:center;font-weight:bold;}</style>', unsafe_allow_html=True)
