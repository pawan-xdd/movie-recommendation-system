import streamlit as st
# from PIL import Image
from database import authenticate, insert_user, get_movies_by_genre
from homepage import create_homepage
from search_results import create_search_results
from user_profile import create_user_profile
from settings import create_settings_page


def create_login_form():
    st.title('Welcome Back.')

    with st.form(key='login_form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        login_button_clicked = st.form_submit_button('Login')

        if login_button_clicked:
            if authenticate(username, password):
                st.success(f'Login successful, Welcome {username}!')
                st.session_state.logged_in = True
                st.session_state.username = username

                # Redirect to the main page after successful login
                st.experimental_set_query_params(logged_in=True, username=username)
            else:
                st.error('Invalid username or password')


def create_registration_form():
    st.title('New User? Register here.')

    with st.form(key='register_form'):
        new_username = st.text_input('New Username')
        new_password = st.text_input('New Password', type='password')
        register_button_clicked = st.form_submit_button('Register')

        if register_button_clicked:
            # Check if the username already exists
            if authenticate(new_username, new_password):
                st.error('Username already exists. Please choose a different one.')
            else:
                # Insert the new user into the database
                insert_user(new_username, new_password)
                st.success('Registration successful! Redirecting to login page...')
                st.session_state.logged_in = True
                st.session_state.username = new_username


def main():
    # im = Image.open()
    st.set_page_config(page_title='Movie Recommender', page_icon='🎬', layout='centered')
    st.session_state.logged_in = st.session_state.get('logged_in', False)

    if not st.session_state.logged_in:
        st.sidebar.title('Navigation')
        page = st.sidebar.radio('Select a page', ['Login', 'Register'], key='login_register_navigation_radio')

        if page == 'Login':
            create_login_form()
        elif page == 'Register':
            create_registration_form()
    else:
        st.sidebar.title('Navigation')
        page = st.sidebar.radio('Select a page', ['Home', 'Search Results', 'Your Profile', 'Settings'],
                                key='main_navigation_radio')

        if page == 'Home':
            create_homepage()
        elif page == 'Search Results':
            selected_genres = st.experimental_get_query_params().get('selected_genres', [])
            movies_by_genre = {
                'Action': ['Movie1', 'Movie2', 'Movie3'],
                'Comedy': ['Movie4', 'Movie5', 'Movie6'],
                'Drama': ['Movie7', 'Movie8', 'Movie9'],
                # Add more genres and movies as needed
            }
            create_search_results(st.empty(), selected_genres, movies_by_genre)

        elif page == 'Your Profile':
            user_details = {'Name': 'Pawan Manjhi', 'Email': 'github.com/pawan-xdd', 'Age': 22, 'Location': 'Bhilai'}
            create_user_profile(st.session_state.username, user_details)
        elif page == 'Settings':
            create_settings_page()


if __name__ == '__main__':
    main()
