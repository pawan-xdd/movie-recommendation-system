# homepage.py

import streamlit as st


def create_homepage():
    st.image('https://www.dualmonitorbackgrounds.com/albums/JCSK/ecosia_.png',
             caption='Movie Recommendation System',
             use_column_width=True)
    st.title("Movie Recommendation System")
    st.markdown('<h2>Select your genre.</h2>', unsafe_allow_html=True)

    # Define a 3x3 grid of movie genres
    genres = [
        ['Action'],
        ['Comedy'],
        ['Drama'],
        ['Sci-Fi'],
        ['Horror'],
        ['Romance'],
        ['Thriller'],
        ['Fantasy'],
        ['Animation']
    ]

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        # Create checkboxes for each genre
        for row in genres[:3]:
            genre_row = st.empty()  # Use st.empty() to create a placeholder for dynamic updates

            for genre in row:
                checkbox_state = genre_row.checkbox(genre, key=f"{genre}_checkbox")

                # Do something based on checkbox state (e.g., store selected genres in session state)
                if checkbox_state:
                    st.write(f'Selected {genre}')

    with col2:
        # Create checkboxes for each genre
        for row in genres[3:6]:
            genre_row = st.empty()  # Use st.empty() to create a placeholder for dynamic updates

            for genre in row:
                checkbox_state = genre_row.checkbox(genre, key=f"{genre}_checkbox")

                # Do something based on checkbox state (e.g., store selected genres in session state)
                if checkbox_state:
                    st.write(f'Selected {genre}')

    with col3:
        # Create checkboxes for each genre
        for row in genres[6:10]:
            genre_row = st.empty()  # Use st.empty() to create a placeholder for dynamic updates

            for genre in row:
                checkbox_state = genre_row.checkbox(genre, key=f"{genre}_checkbox")

                # Do something based on checkbox state (e.g., store selected genres in session state)
                if checkbox_state:
                    st.write(f'Selected {genre}')

    # Add a "Search" button
    if st.button('Search', key='search_button'):
        selected_genres = [genre[0] for genre in genres if st.session_state.get(f"{genre[0]}_checkbox")]
        st.write(f'Searching for movies in genres: {", ".join(selected_genres)}')
    else:
        st.warning("Please select at least one genre!")

        # Add a logout button
    if st.button('Logout'):
        # Reset session state and redirect to the login page
        st.experimental_set_query_params(logged_in=False)
        st.experimental_set_query_params(logged_in=False)

        # Optional: You can use st.experimental_rerun to trigger a re-run of the app to update the UI
        st.experimental_rerun()