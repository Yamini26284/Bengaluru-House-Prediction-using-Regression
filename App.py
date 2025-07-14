import pandas as pd
import pickle as pk
import streamlit as st
model = pk.load(open('House_Prediction.pkl','rb'))
st.header('Banglore House Prices Predictor')
data = pd.read_csv('Cleaned_data.csv')
#data = pd.read_csv('/workspaces/Bengaluru-House-Prediction-using-Regression/Cleaned_data.csv')
loc = st.selectbox('Choose the location',data['location'].unique())
sqft = st.number_input('Enter total sqft')
beds = st.number_input('Enter No of bedrooms')
bath = st.number_input('Enter No of bathrooms')
balc = st.number_input('Enter No of balconies')

input = pd.DataFrame([[loc,sqft,beds,bath,balc]],columns=['location','total_sqft','bath','balcony','bedrooms'])
if st.button('Predict Price'):
    output = model.predict(input)
    out_str = 'Price of the House (In Lakhs) ' + str(int(output[0]*100000))
    st.success(out_str)