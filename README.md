# House-Price-Predictor
House Price Prediction using Machine Learning (Linear Regression ). Includes EDA, feature engineering, model training, and a Streamlit web app for real-time property price estimation.
# House Price Predictor

A machine learning project that predicts the price of a house based on its features.  
The project includes **EDA**, **model training**, and a **Streamlit frontend** for real-time property price predictions.

## Live Demo: https://ms-house-price-predictor.streamlit.app/

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Dataset](#dataset)  
- [Model Training](#model-training)  
- [Streamlit App](#streamlit-app)  
- [Project Structure](#project-structure)  


---

## Project Overview

This project aims to:

- Analyze the housing dataset to identify key factors affecting house prices.  
- Train a machine learning model to predict house prices.  
- Provide an interactive web application using **Streamlit**.  

The model uses features such as:  
**Area, Bedrooms, Bathrooms, Stories, Parking, Furnishing Status, and Amenities (Main Road, Guest Room, Basement, Hot Water Heating, Air Conditioning, Preferred Area).**

---

##  Dataset

The dataset is **Housing.csv** and contains features like:

- `price` (target variable)  
- `area` (square feet)  
- `bedrooms`, `bathrooms`, `stories`  
- `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`  
- `parking`, `prefarea`, `furnishingstatus`

---


## Model Training

- **Algorithm Used**:  Linear Regression  
- **Target Variable**: `price`  
- Model saved as **`model.pkl`** for deployment.

---

---
## Streamlit App

The project includes a **Streamlit-based frontend** for an interactive House Price Predictor. 



**Streamlit frontend**  


![streamlit-app](/House_price_prediction/screenshots/image.png)


---

---

## Project Structure

- House_Price_Prediction/

- ├── eda.ipynb                  
- ├── app.py                   
- ├── model.pkl                
- ├── Housing.csv             
- ├── requirements.txt       
- ├── screenshots/             
- │           - └── image.png
- └── README.md               



---
