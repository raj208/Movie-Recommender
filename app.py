import pandas as pd
import pickle
import streamlit as st

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))
#similarity=pd.DataFrame(similarity)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index
    if len(movie_index) == 0:
        print("Movie not found in the dataset.")
        return
    movie_index = movie_index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie = []
    for i in movie_list:
        movie_id = i[0]
        #fetch poster from api of tmdb .
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie



#print(movies_dict.keys())

st.title('Movies Recommender System')

selected_movie_name = st.selectbox('Which movie you have watched earlier?'
            , movies["title"].values )

if st.button('Recommend'):
    recommendations= recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
