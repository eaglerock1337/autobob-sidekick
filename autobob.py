import pyperclip
import PySimpleGUI as sg


# Set theme for GUI before defining layouts
# GUI_THEME = "LightBlue" # Light mode
GUI_THEME = "DarkBlue14"  # Dark mode
sg.theme(GUI_THEME)


# Dicts for accident info layout
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
        sg.Radio(
            ROLE["-DRIVER-"],
            "role",
            key="-DRIVER-",
            default=True,
            enable_events=True,
            size=(20, 1),
        ),
        sg.Radio(SEAT["-FSEAT-"], "seat", key="-FSEAT-", size=(20, 1), disabled=True),
        sg.Radio(SEAT["-LRSEAT-"], "seat", key="-LRSEAT-", disabled=True),
    ],
    [
        sg.Radio(BELT["-UNBELT-"], "belt", key="-UNBELT-", size=(20, 1)),
        sg.Radio(
            ROLE["-PASSENGER-"],
            "role",
            key="-PASSENGER-",
            enable_events=True,
            size=(20, 1),
        ),
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
        sg.Button("Generate", key="-AINFO-GEN-"),
        sg.Button("Reset", key="-AINFO-RESET-"),
    ],
    [sg.Text("", key="-AINFO-DIALOG-", size=(80, 3))],
]


# Dicts for clinical summary layout
CLINICAL_SUMMARY_LAYOUT = [[sg.Text("", size=(80, 12))]]


TEST_SPACE_LAYOUT = [
    [sg.Text("Test Space", font=("Helvetica", 18))],
    [sg.Multiline(key="test_space", size=(100, 5))],
    [sg.Text("", size=(80, 1)), sg.Button("Clear Text"), sg.Button("Quit")],
]


class AutoBob:
    """
    AutoBob SideKick's got class!

    AutoBob is a class that encapsulates a PySimpleGUI window and all of
    the necessary routines for instanciating the class, handling all user
    input, handling all window events, and performing all necessary text
    and string formatting for outputting to the window and clipboard.

    Declaring the object will instanciate the window and initialize the
    variables. The main_loop() function passes control to the object for
    controlling the main routine of the window, and the close() function
    will close the window and perform any necessary cleanup.
    """

    def __init__(self):
        """
        Initializes GUI application layout and instanciates the window.
        Sets self.window as the PySimpleGUI object to control the window and
        to provide easy access of all events and values by member functions.
        """
        layout = ACCIDENT_INFO_LAYOUT + CLINICAL_SUMMARY_LAYOUT + TEST_SPACE_LAYOUT
        self.window = sg.Window("AutoBob SideKick", layout, font=("Helvetica", 14))

    def _clear_dialogs(self):
        """
        Clears all dialog text windows under all sections of the window.
        """
        self.window.Element("-AINFO-DIALOG-").Update(value="")

    def _handle_seat_choices(self, disabled=False):
        """
        Handles seat choice field behavior based on button events.
        Will clear values of all radio buttons on any run. By default, the
        function will enable the seat radio buttons and the Clear Seat button.
        If disabled=True is specified, it will disabled the above elements.
        """
        self.window.Element("-FSEAT-").Update(value=False, disabled=disabled)
        self.window.Element("-RSEAT-").Update(value=False, disabled=disabled)
        self.window.Element("-LRSEAT-").Update(value=False, disabled=disabled)
        self.window.Element("-RRSEAT-").Update(value=False, disabled=disabled)
        self.window.Element("-CLRSEAT-").Update(disabled=disabled)

    def _select_role(self, role):
        """
        Peforms the necessary routines for selecting a role for accident info.
        If -PASSENGER-, the passenger seat fields are activated.
        If -DRIVER-, the passenger seat fields are cleared and grayed out.
        """
        if role == "-PASSENGER-":
            self._handle_seat_choices()
        elif role == "-DRIVER-":
            self._handle_seat_choices(disabled=True)

    def _gen_accident_info(self):
        """
        Generates the accident info text, updates the window, and copies
        the resulting data to the clipboard.
        """
        # pyperclip.copy()
        pass

    def _reset_accident_info(self):
        """
        Reset all fields under the accident info section back to 
        """
        self.window.Element("-NOBELT-").Update(value=True)
        self.window.Element("-DRIVER-").Update(value=True)
        self.window.Element("-ACC-DESC-").Update(value="")
        self._handle_seat_choices(disabled=True)

        dialog = "Accident Info section reset to defaults."
        self.window.Element("-AINFO-DIALOG-").Update(value=dialog)

    def main_loop(self):
        """
        Main routine for AutoBob SideKick.
        Responds to window events and routes
        """
        while True:
            event, values = self.window.read()

            if event == "Quit" or event == sg.WIN_CLOSED:
                break

            self._clear_dialogs()

            if event == "-DRIVER-" or event == "-PASSENGER-":
                self._select_role(event)
            elif event == "-CLRSEAT-":
                self._handle_seat_choices()
            elif event == "-AINFO-RESET-":
                self._reset_accident_info()
            elif event == "-AINFO-GEN-":
                self._gen_accident_info()

    def close(self):
        """
        Closes the window and cleans up the program.
        """
        self.window.close()


if __name__ == "__main__":
    autobob = AutoBob()
    autobob.main_loop()
    autobob.close()
