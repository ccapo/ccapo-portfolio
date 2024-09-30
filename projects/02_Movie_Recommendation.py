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
st.markdown("Enter the title of a movie to see a list of 10 recommendations")
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