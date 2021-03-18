import pyperclip
import PySimpleGUI as sg


def initialize():
    """
    Initializes GUI application layout and instanciates the window.
    Returns a PySimpleGUI window object to the calling routine.
    """
    layout = [[sg.Text("Hello, Dr. Bobberts!")], [sg.Button("Boop")]]
    new_window = sg.Window("AutoBob SideKick", layout)

    return new_window


def format_text():
    """
    Formats the text for output however Rob needs it for his program.
    Returns the correct string
    """
    pass


def main_loop(window):
    """
    Main routine for AutoBob SideKick.
    Responds to window events
    """
    while True:
        event, values = window.read()

        if event == "Boop" or event == sg.WIN_CLOSED:
            break

        # pyperclip.copy()


if __name__ == "__main__":
    app_window = initialize()
    main_loop(app_window)
    app_window.close()
