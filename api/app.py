import uvicorn
import pandas as pd 
from pydantic import BaseModel
from fastapi import FastAPI
import numpy as np
import joblib
from typing import List
import json
from xmlrpc.client import Boolean

description = """"
The Getaround prices API is online service which helps you to calculate the ideal price according the caracteristics of a car and its services.

This service calculates the price thanks to a model applied to the prices of our owners and proposed to rental on our application.

## Endpoint Prediction

* `/predict` This endpoint accepts POST method with JSON input data and it should return the predictions. We assume inputs will be always well formatted. It means you do not have to manage errors. We leave the error handling as a bonus.

Check out documentation for more information.
"""

# tags
tags_metadata = [
    {
        "name": "Prediction",
        "description": "Endpoint to predict the rental price for 1 day"
    }
]


# API object
app = FastAPI(title="GETAROUND API",
    description=description,
    version="1.0",
    openapi_tags=tags_metadata)


# Define features
class PredictionFeatures(BaseModel):
    model_key: str
    mileage: int
    engine_power: int
    fuel: str
    paint_color: str
    car_type: str
    private_parking_available: str
    has_gps: str
    has_air_conditioning: str
    automatic_car: str
    has_getaround_connect: str
    has_speed_regulator: str
    winter_tires: str


# endpoint predict (model and preprocessor generated in the notebook 03_Price_optimization.ipynb)
# Les input seront toujours correctement formatés

@app.post("/predict", tags=["Prediction"])
async def predict(predictionFeatures: PredictionFeatures):

    # Read data
    prices_input = pd.DataFrame(dict(predictionFeatures), index=[0])
    
    # Preprocessing
    preprocessor = joblib.load('preprocessor.joblib')

    # apply preprocessing
    prices_transform = preprocessor.transform(prices_input)

    # Load the models from local
    model_price  = 'getaround_price_model.joblib'
    regressor = joblib.load(model_price)
    prediction = regressor.predict(prices_transform)

    # Format response
    response = {"prediction": prediction.tolist()[0]}
    return response

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000, debug=True, reload=True)