
# Import des librairies
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel


### CONFIG
st.set_page_config(
    page_title="Delays analysis",
    page_icon="💸",
    layout="wide"
  )

### TITLE AND TEXT
st.title("Delays impact on cancelations")
st.divider()

st.markdown("""
Data insights to make a decision about your following marketing params:
1. threshold: how long should the minimum delay be?
2. scope: should we enable the feature for all cars?, only Connect cars?

""")
st.divider()


### LOAD AND CACHE DATA
def load_data():
    data = pd.read_csv('src/retards.csv', thousands=None)
    return data
commandes = load_data()

# Contenu
st.subheader('Share of our owner’s revenue would potentially be affected by the feature')
st.markdown("""
Measure the impact of the threshold on owners and their revenues.
""")
col1,col2,col3 = st.columns(3, gap="small")

delay_threshold = col1.slider('Indicate the threshold in hours :', 0, 12, 2)
delay_threshold_minutes = delay_threshold * 60
threshold_mask = (commandes['time_delta_with_previous_rental_in_minutes'] > delay_threshold_minutes)
rent_cancel_late = commandes[threshold_mask]
total_owners = len(commandes['car_id'].unique())
threshold_result = len(rent_cancel_late['car_id'].unique())
pourcent_owners = (threshold_result*100)/total_owners
pourcent_owners = round(pourcent_owners, 2)

#col4.metric('Lost orders',int(nb_annulations))
#col2.write("")
#col2.metric(f'Threshold',delay_threshold)
col2.metric(f'Impacted owners',threshold_result)
col3.metric(f'Impacted revenue (%)',pourcent_owners)
st.divider()


st.subheader('Rentals affected by the feature depending on the threshold and scope')
st.markdown("""
Measure the impact of the threshold and scope on owners and their revenues.
""")
col4,col5,col6,col7 = st.columns(4, gap="small")

delay_threshold_scope = col4.slider('Choose your threshold:', 0, 12, 2)
delay_threshold_minutes = delay_threshold_scope * 60
option_checkin = col5.selectbox(
    'Choose your scope',
    ('mobile', 'connect'))

threshold_scope_mask = (commandes['time_delta_with_previous_rental_in_minutes'] > delay_threshold_minutes) & (commandes['checkin_type'] == option_checkin)
rent_cancel_late = commandes[threshold_scope_mask]
total_owners = len(commandes['car_id'].unique())
threshold_result = len(rent_cancel_late['car_id'].unique())
pourcent_owners = (threshold_result*100)/total_owners
pourcent_owners = round(pourcent_owners, 2)

col6.metric(f'Impacted owners',threshold_result)
col7.metric(f'Impacted revenue (%)',pourcent_owners)
st.divider()


st.subheader('How often are drivers late for the next check-in? How does it impact the next driver?')
st.markdown("""
Impact of late checkout on next cancelation and next ended.
""")

mask_late = (commandes['time_delta_with_previous_rental_in_minutes'] > 0)
rent_late = len(commandes[mask_late])

mask_canceled = (commandes['time_delta_with_previous_rental_in_minutes'] > 0) & (commandes['state'] == 'canceled')
rent_late_canceled = len(commandes[mask_canceled])

mask_ended = (commandes['time_delta_with_previous_rental_in_minutes'] > 0) & (commandes['state'] == 'ended')
rent_late_ended = len(commandes[mask_ended])

# affiche les résultats
col8,col9,col10 = st.columns(3)
col8.metric("Late checkout", rent_late)
col9.metric("Next canceled", rent_late_canceled)
col10.metric('Next ended', rent_late_ended)
st.divider()


st.subheader('How many problematic cases will it solve depending on the chosen threshold and scope?')
st.markdown("""
Measure the actual canceled rentals that could be saved thanks to threshold and scope.
""")
col11,col12,col13 = st.columns(3)

delay_threshold_scope = col11.slider('Choose your threshold :', 0, 12, 2)
delay_threshold_minutes = delay_threshold_scope * 60
option_checkin = col11.selectbox(
    'Choose your scope:',
    ('mobile', 'connect'))

threshold_scope_mask_canceled = (commandes['time_delta_with_previous_rental_in_minutes'] > delay_threshold_minutes) & (commandes['checkin_type'] == option_checkin) & (commandes['state'] == 'canceled')
rent_saved = len(commandes[threshold_scope_mask_canceled])

# affiche les résultats
col12.metric("Actual rentals canceled", rent_late_canceled)
col13.metric('Rentals saved', rent_saved)
st.divider()