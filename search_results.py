import streamlit as st
from database import get_movies_by_genre


def create_search_results(placeholder, selected_genres, movies_by_genre):
    st.title('Search Results Page')
    # Use the placeholder to dynamically update the content
    placeholder.text('')
    placeholder.subheader(' ')
    selected_genres = st.experimental_get_query_params().get('selected_genres', [])

    if selected_genres:
        st.write('Selected Genres:', ', '.join(selected_genres))

        st.write('Movies to Watch:')
        for genre in selected_genres:
            movies = get_movies_by_genre(genre)
            if movies:
                st.write(f'{genre}: {", ".join(movies)}')
            else:
                st.write(f'No movies found for {genre}')
    else:
        st.warning('No genres selected for search.')