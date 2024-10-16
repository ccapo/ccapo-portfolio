import streamlit as st

# Page title
st.set_page_config(page_title="Chris Capobianco's Profile", page_icon=':rocket:', layout='wide')

home = st.Page('Intro.py', title = 'Home')

movie_recommendation = st.Page('projects/02_Movie_Recommendation.py', title='Movie Recommendation')
# weather_classification = st.Page('projects/04_Weather_Classification.py', title='Weather Classification')
stock_market = st.Page('projects/05_Stock_Market.py', title='Stock Market Forecast')
generative_music = st.Page('projects/06_Generative_Music.py', title='Generative Music')
llm_fine_tune = st.Page('projects/07_LLM_Fine_Tuned.py', title='Fine Tuned LLM')

pg = st.navigation(
    {
        'Home': [
            home
        ],
        'Projects': [
            movie_recommendation,
            # weather_classification,
            stock_market,
            generative_music,
            llm_fine_tune
        ]
    }
)
    
pg.run()
