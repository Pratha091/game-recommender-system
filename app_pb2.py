import streamlit as st
import pickle
import requests

games = pickle.load(open('games.pkl','rb'))
games_list = games['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(game_id):

    url = "https://rawg-video-games-database.p.rapidapi.com/games/{}?key=d40ca49e9c5c4ea7a34592b50ed5cc80"

    headers = {
        'x-rapidapi-key': "e6ef05302emsh9c46dd59d7ac5d1p13a2d8jsneb37aae7d452",
        'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

    response = requests.request("GET", url.format(game_id), headers=headers)
    data = response.json()

    return data['background_image']




def recommend(game):
    game_index = games[games['title'] == game].index[0]
    distances = similarity[game_index]
    games_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:5]

    recommended_games = []
    recommended_games_posters = []

    for i in games_list:
        game_id = games.iloc[i[0]].id
        recommended_games.append(games.iloc[i[0]].title)
        #fetch poster from api
        recommended_games_posters.append(fetch_poster(game_id))

    return recommended_games,recommended_games_posters

st.title('Game Recommender System')

selected_game_name = st.selectbox(
     'Please enter a game:',
     games_list)

if st.button('Recommend'):
    names,posters = recommend(selected_game_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
# import requests
#
# url = "https://rawg-video-games-database.p.rapidapi.com/games/1000?key=17cc32aa68b74431bfec5de6ab5b8c98"
#
# headers = {
# 'x-rapidapi-key': "e6ef05302emsh9c46dd59d7ac5d1p13a2d8jsneb37aae7d452",
# 'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers)
#
# print(response.text)
