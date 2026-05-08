import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# PAGE CONFIG

st.set_page_config(
    page_title='Movie Recommender',
    page_icon='🎬',
    layout='centered'
)


# LOAD DATA


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

vectors = pickle.load(open('vectors.pkl', 'rb'))


# RECOMMEND FUNCTION

def recommend(movie):
    similarity = cosine_similarity(vectors)

    movie = movie.lower()

    movie_index = movies[movies['title_lower'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies



# UI DESIGN
st.markdown(
    """
    <h1 style='text-align:center; color:#E50914;'>
    🎬 Movie Recommendation System
    </h1>
    """,
    unsafe_allow_html=True
)
st.write(
    'Select a movie and get 5 similar movie recommendations.'
)


# MOVIE DROPDOWN

selected_movie = st.selectbox(
    'Choose a movie',
    movies['title'].values
)



# BUTTON
if st.button('Recommend Movies'):
    recommendations = recommend(selected_movie)

    st.subheader('Recommended Movies')

    for movie in recommendations:

        st.write('✅', movie)

