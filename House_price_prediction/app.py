import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

model_path = os.path.join("House_price_prediction", "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title=" House Price Predictor", layout="centered")

st.title(" House Price Predictor")

st.markdown("Get an instant valuation for your property based on its features.")

def bin_encode(val):
    return 1 if val == "Yes" else 0

def furnish_encode(val):
    return {"Unfurnished": 0, "Semi-Furnished": 1, "Furnished": 2}[val]

with st.form("prediction_form"):
    st.subheader("Property Details")

    col1, col2 = st.columns(2)
    with col1:
        area = st.number_input("Area (sq ft)", min_value=500, max_value=20000, step=100, value=2000)
        bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5, 6], index=2)
        bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4, 5], index=1)
    with col2:
        stories = st.selectbox("Stories", [1, 2, 3, 4], index=1)
        parking = st.selectbox("Parking Spaces", [0, 1, 2, 3, 4], index=1)
        furnishingstatus = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"], index=2)

    st.markdown("---")
    st.subheader("Amenities")

    col3, col4 = st.columns(2)
    with col3:
        mainroad = st.radio("Main Road Access ", ["Yes", "No"], horizontal=True)
        guestroom = st.radio("Guest Room ", ["Yes", "No"], horizontal=True)
        basement = st.radio("Basement ", ["Yes", "No"], horizontal=True)
    with col4:
        hotwaterheating = st.radio("Hot Water Heating ", ["Yes", "No"], horizontal=True)
        airconditioning = st.radio("Air Conditioning ", ["Yes", "No"], horizontal=True)
        prefarea = st.radio("Preferred Area ", ["Yes", "No"], horizontal=True)

    submit = st.form_submit_button("Predict Property Value ")

if submit:
    try:
        input_data = np.array([[float(area), float(bedrooms), float(bathrooms), float(stories),
                                bin_encode(mainroad), bin_encode(guestroom), bin_encode(basement),
                                bin_encode(hotwaterheating), bin_encode(airconditioning),
                                float(parking), bin_encode(prefarea), furnish_encode(furnishingstatus)]])

        feature_names = ["area", "bedrooms", "bathrooms", "stories", "mainroad", "guestroom",
                         "basement", "hotwaterheating", "airconditioning", "parking", "prefarea", "furnishingstatus"]
        input_df = pd.DataFrame(input_data, columns=feature_names)

        prediction = model.predict(input_df)[0]

        with st.spinner("Calculating..."):
            st.success(f" **Estimated Property Value:** $ {prediction:,.2f}")

    except Exception as e:
        st.error(f" Error: {str(e)}")
