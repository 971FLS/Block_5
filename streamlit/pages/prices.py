
# Import des librairies
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel
import requests
import json

### CONFIG
st.set_page_config(
    page_title="Prices evaluation",
    page_icon="💸",
    layout="wide"
  )

### TITLE AND TEXT
st.title("Prices testing")
st.markdown('View the data used to create the model of price prediction.')
st.markdown('If you want to understand data, visit the topic [Understand Data](/understand_data)')

### LOAD AND CACHE DATA
def load_data():
    data = pd.read_csv('src/get_around_pricing_project.csv', thousands=None)
    return data

prices = load_data()

fuel_options = prices['fuel'].value_counts().index
brands = prices['model_key'].value_counts().index
colors = prices['paint_color'].value_counts().index
type_car = prices['car_type'].value_counts().index
engine_power_max = prices['engine_power'].mean()

with st.form("api_form"):
   st.write("*All informations are needed.*")
   model_key = st.selectbox('model_key',brands)
   mileage = st.slider("Mileage", 0, 200000, 50000)
   engine_power = st.slider("Engine power", 0, 500, 400)
   fuel = st.selectbox('Fuel',fuel_options)
   paint_color = st.selectbox('Color', colors)
   car_type = st.selectbox('Car type', type_car)
   private_parking_available = st.selectbox('Parking available', ('True', 'False'))
   has_gps = st.selectbox('Has GPS', ('True', 'False'))
   has_air_conditioning = st.selectbox('Has air conditioning', ('True', 'False'))
   automatic_car = st.selectbox('Has Automatic car', ('True', 'False'))
   has_getaround_connect = st.selectbox('Has Getaround connect', ('True', 'False'))
   has_speed_regulator = st.selectbox('Has speed regulator', ('True', 'False'))
   winter_tires = st.selectbox('Has winter tires', ('True', 'False'))
   st.form_submit_button(label="Submit")


api_params = {'model_key': model_key, 'mileage': mileage, 'engine_power': engine_power,
              'fuel': fuel, 'paint_color': paint_color, 'car_type': car_type,
              'private_parking_available': private_parking_available, 'has_gps': has_gps,
              'has_air_conditioning': has_air_conditioning, 'automatic_car': automatic_car,
              'has_getaround_connect': has_getaround_connect, 'has_speed_regulator': has_speed_regulator,
              'winter_tires': winter_tires}

r = requests.post('https://getaroundapifls-c0671da11c4c.herokuapp.com/predict', json=api_params)
prediction_live = r.json()
predict_reponse = prediction_live['prediction']
predict_reponse = round(predict_reponse, 2)
st.divider()

st.markdown("Prediction of the price")
st.metric('Prediction', predict_reponse)
st.divider()



## Lien vers l'api en cas de besoin

st.markdown('## API avaible')
st.markdown('You can use an api that implements the best model to predict the rental price for one day.')
st.markdown('To use the api, please click here : https://getaroundapifls-c0671da11c4c.herokuapp.com/docs')
st.divider()
