import streamlit as st


def create_user_profile(username, user_details):
    st.subheader(' ')
    st.subheader('Your Profile')
    st.title(f'Hello, {username}!')
    st.image('https://www.dualmonitorbackgrounds.com/albums/JCSK/ecosia_.png', caption='Cover', use_column_width=True)
    pfp = st.image('https://i.imgur.com/BIaMF6m.jpeg', caption='Cat', width=300)

    # Display additional user details
    st.subheader('User Details:')
    for key, value in user_details.items():
        st.write(f'{key}: {value}')