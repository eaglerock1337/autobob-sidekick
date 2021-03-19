import pyperclip
import PySimpleGUI as sg


# Set theme for GUI before defining layouts
# GUI_THEME = "LightBlue" # Light mode
GUI_THEME = "DarkBlue14"  # Dark mode
sg.theme(GUI_THEME)


BELT = {
    "-BELTED-": "Restrained",
    "-UNBELT-": "Unrestrained",
    "-NOBELT-": "Neither",
}


ROLE = {
    "-DRIVER-": "Driver",
    "-PASSENGER-": "Passenger",
}


SEAT = {
    "-FSEAT-": "Front Seat",
    "-RSEAT-": "Rear Seat",
    "-LRSEAT-": "Left Rear Seat",
    "-RRSEAT-": "Right Rear Seat",
}


ACCIDENT_INFO_LAYOUT = [
    [sg.Text("Accident Information", font=("Helvetica", 18))],
    [
        sg.Text("Seat Belt", size=(24, 1)),
        sg.Text("Role", size=(23, 1)),
        sg.Text("Seat"),
    ],
    [
        sg.Radio(BELT["-BELTED-"], "belt", key="-BELTED-", size=(20, 1)),
        sg.Radio(ROLE["-DRIVER-"], "role", key="-DRIVER-", default=True, size=(20, 1)),
        sg.Radio(SEAT["-FSEAT-"], "seat", key="-FSEAT-", size=(20, 1), disabled=True),
        sg.Radio(SEAT["-LRSEAT-"], "seat", key="-LRSEAT-", disabled=True),
    ],
    [
        sg.Radio(BELT["-UNBELT-"], "belt", key="-UNBELT-", size=(20, 1)),
        sg.Radio(ROLE["-PASSENGER-"], "role", key="-PASSENGER-", size=(20, 1)),
        sg.Radio(SEAT["-RSEAT-"], "seat", key="-RSEAT-", size=(20, 1), disabled=True),
        sg.Radio(SEAT["-RRSEAT-"], "seat", key="-RRSEAT-", disabled=True),
    ],
    [
        sg.Radio(BELT["-NOBELT-"], "belt", key="-NOBELT-", default=True, size=(45, 1)),
        sg.Button("Clear Seat Choice", key="-CLRSEAT-", disabled=True),
    ],
    [
        sg.Text("Accident description:"),
        sg.InputText(key="-ACC-DESC-", size=(60, 1)),
        sg.Button("Generate", key="-GEN-AINFO-"),
        sg.Button("Reset", key="-RESET-AINFO-"),
    ],
    [sg.Text("", key="-AINFO-TEXT-", size=(80, 2))],
]


TEST_SPACE_LAYOUT = [
    [sg.Text("Test Space", font=("Helvetica", 18))],
    [sg.Multiline(key="test_space", size=(100, 5))],
    [sg.Text("", size=(80, 1)), sg.Button("Clear Text"), sg.Button("Quit")],
]


def initialize():
    """
    Initializes GUI application layout and instanciates the window.
    Returns a PySimpleGUI window object to the calling routine.
    """
    choices = ["your", "mom"]
    layout = (
        ACCIDENT_INFO_LAYOUT
        + [
            [sg.Text("", size=(80, 12))],
        ]
        + TEST_SPACE_LAYOUT
    )

    new_window = sg.Window("AutoBob SideKick", layout, font=("Helvetica", 14))

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
    Responds to window events and routes
    """
    while True:
        event, values = window.read()

        if event == "Quit" or event == sg.WIN_CLOSED:
            break

        # pyperclip.copy()


if __name__ == "__main__":
    app_window = initialize()
    main_loop(app_window)
    app_window.close()
