import streamlit as st
import pickle

model=pickle.load(open('model.pkl','rb'))

st.title('Electricity Price Prediction')

#features = [["Day", "Month", "ForecastWindProduction", "SystemLoadEA", "SMPEA", "ORKTemperature", "ORKWindspeed", "CO2Intensity", "ActualWindProduction", "SystemLoadEP2"]]

col1,col2=st.columns(2)
day=col1.number_input('Enter the Day')
month=col2.number_input('Enter the Month')
forecastWindProduction=col1.number_input('Enter Wind Production')
systemLoadEA=col2.number_input('Enter System Load')
smpea=col1.number_input('Enter SMPEA')
temperature=col2.number_input('Enter ORKTemperature')
windspeed=col1.number_input('Enter ORKWind Speed')
co2intensity=col2.number_input('Enter CO2 Intensity')
actualWindProduction=col1.number_input('Enter Actual Wind Production')
systemLoadEP2=col2.number_input('Enter System Load EP2')

if st.button('Predict Price'):
    data=[[day,month,forecastWindProduction,systemLoadEA,smpea,temperature,windspeed,co2intensity,actualWindProduction,systemLoadEP2]]
    st.success(model.predict(data)[0]+'$')
