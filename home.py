import PySimpleGUI as sg
from database import authenticate

sg.theme("Black")


def create_login_window():
    layout = [
        [sg.Text("Welcome Back.", size=20)],
        [sg.Text('Username:'), sg.Input(key='username')],
        [sg.Text('Password:'), sg.Input(key='password', password_char='*')],
        [sg.Button('Login')], [sg.Button('Exit')]
    ]

    return sg.Window("Movie Recommendation System", layout, finalize=True, size=(400, 200), resizable=True)


def create_main_page(username):
    navbar = [
        sg.Button('Home'),
        sg.Button('Page 1'),
        sg.Button('Page 2'),
        sg.Button('Page 3'),
        sg.Button('Settings'),
        sg.Button('Logout'),
        sg.Button('Exit')
    ]
    layout = [
        [sg.Text(f'Welcome, {username}!')],
        [sg.Column([navbar], justification='center', element_justification='center', size=(400, 50), expand_x=True)],
        [sg.Text('')],
        [sg.Button('Button 1', size=(10, 1)), sg.Button('Button 2', size=(10, 1)), sg.Button('Button 3', size=(10, 1))],
        [sg.Button('Button 4', size=(10, 1)), sg.Button('Button 5', size=(10, 1)), sg.Button('Button 6', size=(10, 1))],
        [sg.Button('Button 7', size=(10, 1)), sg.Button('Button 8', size=(10, 1)), sg.Button('Button 9', size=(10, 1))],
        [sg.Button('Logout')], [sg.Button('Exit')]

    ]

    return sg.Window('Main Page', layout, finalize=True, size=(400, 200), resizable=True)


def main():
    login_window = create_login_window()
    main_page_window = None

    while True:
        window, event, values = sg.read_all_windows()

        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break

        if window == login_window and event == 'Login':
            username = values['username']
            password = values['password']

            # Check the login credentials against the database
            if authenticate(username, password):
                sg.popup('Login successful!')
                login_window.hide()
                main_page_window = create_main_page(username)


        elif window == main_page_window:
            if event == 'Logout':
                main_page_window.close()
                login_window.un_hide()
            elif event == 'Exit':
                break

    sg.popup('Goodbye!')
    login_window.close()
    if main_page_window:
        main_page_window.close()


if __name__ == '__main__':
    main()
