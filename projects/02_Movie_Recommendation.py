import streamlit as st

st.header('Movie Recommendation', divider='green')

st.warning("This model is now hosted on [Huggingface](https://huggingface.co/spaces/ccapo/portfolio)")

st.markdown("#### What is a Recommendation System?")
st.markdown("Recommendation systems suggest recommendations to users depending on a variety of criteria.")
st.markdown('''There are 3 types of recommendation systems:
1. Demographic Filtering: The recommendations are the same for every user. They are generalized, not personalized. These types of systems are behind sections like *Top Trending*.
2. Content-based Filtering: These suggest recommendations based on the item metadata (movie, product, song, etc). Here, the main idea is if a user likes an item, then the user will also like items similar to it.
3. Collaboration-based Filtering: These systems make recommendations by grouping the users with similar interests. For this system, metadata of the item is not required.
''')
st.markdown("In this project, we are building a **Content-based** recommendation engine for movies titles.")
tmdb_data_url = "https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata"
st.markdown("To build this recommendation system, we will be using almost 5k movies and credits from the TMDB dataset available at [Kaggle](%s)" % tmdb_data_url)

st.divider()

st.markdown("Enter the title of a movie to see a list of 10 recommendations (e.g. The Dark Knight Rises, The Avengers, etc)")
title = st.text_input("Movie Title")