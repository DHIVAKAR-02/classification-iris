# Iris Flower Prediction App
## This app predicts the species type of Iris Flower by the inputs given by user.
We have developed an app predicts the species type of Iris Flower by the inputs given by user using RandomForestClassifier for the round-2 of Daisi Hackathon (via Hackerearth)
### Team Details:
#### Team Name: MIDNIGHT HACKER
#### Team Leader: NANDHAKUMAR S 
#### Members: SUJITH V, MOHAMED RAFEEK S
#### Designation: Student at BANNARI AMMAN INSTITUTE OF TECHNOLOGY, SATHYAMANGALAM.
#### Contact: +919488393947
#### Mail: nandhakumarshanmugam.udt.4757@gmail.com

## What we used......
• Daisi


• Streamlit UI


• pandas


• sklearn


#### We have done our project in the daisi platform (https://app.daisi.io/) using Streamlit UI. We used RandomForestClassifier from sklearn module to predict the Iris Flower Species.
## Features
• Predicting Iris flower species from the given input.


• Probability of the flower being a species.


## Usage of Daisi

It is recommended to use this application on the daisi platform itself using the link https://app.daisi.io/daisies/nandhakumar/Iris%20Flower%20Prediction%20App/app
However, you can still use your own editor using the below method:
## Python
### First, load the Packages:
See the docs for pyDaisi installation and authentication.
```
import pydaisi as pyd
iris_flower_prediction_app = pyd.Daisi("nandhakumar/Iris Flower Prediction App")
```
### Now, connect to Daisi and access the functions using:
### Documented endpoints
#### iris_flower_prediction_app
```
iris_flower_prediction_app.iris_flower_prediction_app().value
```
#### iris_flower_prediction_app_using_RandomForestClassifier
```
iris_flower_prediction_app.iris_flower_prediction_app_using_RandomForestClassifier().value
```

## R
```
library(rdaisi)
configure_daisi(python_path="/usr/local/bin/python3")
iris_flower_prediction_app <- Daisi("nandhakumar/Iris Flower Prediction App")
```
### Endpoints
#### iris_flower_prediction_app
```
iris_flower_prediction_app$iris_flower_prediction_app()$value()
```

#### iris_flower_prediction_app_using_RandomForestClassifier
```
iris_flower_prediction_app$iris_flower_prediction_app_using_RandomForestClassifier()$value()
```
