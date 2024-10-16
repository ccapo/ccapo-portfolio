import streamlit as st
import pickle

st.header('Movie Recommendation', divider='green')

@st.cache_resource
def load_model():
    model_file = open('./models/movie_recommendation_model.pkl', 'rb')
    movies_df = pickle.load(model_file)
    cosine_sim = pickle.load(model_file)
    indices = pickle.load(model_file)
    model_file.close()
    return movies_df, cosine_sim, indices

# Load the Model
movies_df, cosine_sim, indices = load_model()

@st.cache_data
def get_recommendations(title, cosine_sim = cosine_sim):
    if title in indices:
        idx = indices[title]
    else:
        print(f"Unable to find a matching movie title: {title}")
        return []
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key = lambda x: x[1], reverse = True)
    similarity_scores = similarity_scores[1:11]
    # (a, b) where a is id of movie, b is similarity_scores
    movies_indices = [ind[0] for ind in similarity_scores]
    movies = movies_df["title"].iloc[movies_indices]
    return movies

# Get movie recommendations
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
if title != "":
    movies = get_recommendations(title)
    if len(movies) > 0:
        output = ''
        count = 1
        for m in movies:
            output += f"{count}. {m}\n"
            count += 1
        st.markdown(output)
    else:
        st.warning(f"Unable to find a movie matching title: {title}")