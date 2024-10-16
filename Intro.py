import streamlit as st
from PIL import Image

# Page title
st.title("Chris Capobianco's Profile")

st.markdown('Hello, welcome to my ML portfolio.')
st.markdown('Please have a look at the descriptions below, and select a project from the sidebar.')

st.header('Projects', divider='red')

mv = Image.open("assets/movie.jpg")
# wp = Image.open("assets/weather.png")
sm = Image.open("assets/stock-market.png")
mu = Image.open("assets/music.jpg")

with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Movie Recommendation", divider="green")
        st.markdown("""
            - Created a content based recommendation system using cosine similarity
            - Trained on almost 5k movies and credits from the TMDB dataset available at Kaggle
        """)
    with image_column:
        st.image(mv)

# with st.container():
#     text_column, image_column = st.columns((3,1))
#     with text_column:
#         st.subheader("Weather Classification", divider="green")
#         st.markdown("""
#             - Created a Random Forest classification model to predict the weather
#             - Trained on three years of data for the city of Seattle, Washington
#         """)
#     with image_column:
#         st.image(wp)

with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Stock Market Forecast", divider="green")
        st.markdown("""
            - Created a two layer GRU model to forecast of stock prices
            - Trained on 2006-2018 closing prices of four well known stocks
        """)
    with image_column:
        st.image(sm)

with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Generative Music", divider="green")
        st.markdown("""
            - Created a LSTM model to generate music
            - Trained on MIDI files from Final Fantasy series
        """)
    with image_column:
        st.image(mu)
