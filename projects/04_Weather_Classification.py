import streamlit as st

st.header('Weather Classification', divider='green')

st.warning("This model is now hosted on [Huggingface](https://huggingface.co/spaces/ccapo/portfolio)")

st.markdown("Change the sliders below to see the classification")

# Get input parameters
precipitation = st.slider('Precipitation (mm)', 0.0, 100.0, 0.0, 1.0)
temp_min = st.slider('Minimum Temperature (C)', -10.0, 20.0, 8.0, 1.0)
temp_max = st.slider('Maximum Temperature (C)', -2.0, 40.0, 15.0, 1.0)
wind = st.slider('Wind Speed (m/s)', 0.0, 10.0, 3.0, 1.0)

st.info("Weather Classification:")