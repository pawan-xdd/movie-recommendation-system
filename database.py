import sqlite3

DATABASE_FILE = 'user_credentials.db'


def create_tables():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Create a users table with columns: id, username, password
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def insert_user(username, password):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Insert a new user into the users table
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

    conn.commit()
    conn.close()


def authenticate(username, password):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Check if the provided username and password match a user in the database
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user_data = cursor.fetchone()

    conn.close()

    return user_data is not None


movie_database = {
    'Action': ['Die Hard', 'Mad Max: Fury Road', 'John Wick'],
    'Comedy': ['Superbad', 'Anchorman', 'Bridesmaids'],
    'Drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather'],
    'Sci-Fi': ['Blade Runner', 'The Matrix', 'Interstellar'],
    'Horror': ['The Shining', 'Get Out', 'A Quiet Place'],
    'Romance': ['The Notebook', 'Pride and Prejudice', 'La La Land'],
    'Thriller': ['Se7en', 'Gone Girl', 'The Silence of the Lambs'],
    'Fantasy': ['The Lord of the Rings', 'Harry Potter series', 'The Chronicles of Narnia'],
    'Animation': ['Toy Story', 'Finding Nemo', 'The Lion King']
}


def get_movies_by_genre(genre):
    return movie_database.get(genre, [])
