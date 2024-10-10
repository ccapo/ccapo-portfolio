import streamlit as st
import pandas as pd
import pickle
import sklearn
from PIL import Image

@st.cache_resource
def load_model():
    model_file = open('./models/weather_prediction_model.pkl', 'rb')
    rfc = pickle.load(model_file)
    oe = pickle.load(model_file)
    sc = pickle.load(model_file)
    images = pickle.load(model_file)
    model_file.close()
    return rfc, oe, sc, images

@st.cache_resource
def load_icons():
    dz = Image.open("assets/drizzle.png")
    rn = Image.open("assets/rain.png")
    sn = Image.open("assets/sun.png")
    sw = Image.open("assets/snow.png")
    fg = Image.open("assets/fog.png")
    return dz, rn, sn, sw, fg

@st.cache_data
def get_prediction(input):
    if len(input) != 4:
        return None
    input = pd.DataFrame([input], columns = ['precipitation', 'temp_max', 'temp_min', 'wind'])
    X_predict = sc.transform(input)
    y_predict = [rfc.predict(X_predict)]
    weather_predict = oe.inverse_transform(y_predict)[0]
    return weather_predict[0]

# Load the Model
rfc, oe, sc, images = load_model()

# Load the Icons
dz, rn, sn, sw, fg = load_icons()

st.header('Weather Classification', divider='green')

st.markdown("Change the sliders below to see the classification")

# Get input parameters
precipitation = st.slider('Precipitation (mm)', 0.0, 100.0, 0.0, 1.0)
temp_min = st.slider('Minimum Temperature (C)', -10.0, 20.0, 8.0, 1.0)
temp_max = st.slider('Maximum Temperature (C)', -2.0, 40.0, 15.0, 1.0)
wind = st.slider('Wind Speed (m/s)', 0.0, 10.0, 3.0, 1.0)

# Get weather prediction
weather = get_prediction([precipitation, temp_min, temp_max, wind])
if weather == None:
    st.warning("Unknown Weather Classification")
else:
    icon = Image.open(images[weather])

st.info("Weather Classification:")
st.image(icon, caption = weather, width = 250)