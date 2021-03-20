import datetime
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
    [sg.Text("Accident Information", font=("Helvetica", 18, "bold"))],
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
        sg.InputText(key="-ACC-DESC-", size=(64, 1)),
        sg.Button("Generate", key="-AINFO-GEN-"),
        sg.Button("Reset", key="-AINFO-RESET-"),
    ],
    [sg.Text("", size=(40, 1)), sg.Text("", key="-AINFO-DIALOG-", size=(60, 1))],
]


# Lists and dicts for treatment codes
TREATMENT_CODE_DISPLAY_LAYOUT = [
    ["98940", "97016", "97110"],
    ["98941", "97018", "97112"],
    ["98942", "97022", "97113"],
    ["98943", "97026", "97116"],
    ["97010", "97032", "97124"],
    ["97012", "97033", "97140"],
    ["97014", "97035", "97530"],
    ["G0283", "97039", "99072"],
]
# fmt: off
TREATMENT_CODE_PRINT_LAYOUT = [
    "98940", "98941", "98942", "98943", "97010", "97012", "97014", "G0283",
    "97016", "97018", "97022", "97026", "97032", "97033", "97035", "97039",
    "97110", "97112", "97113", "97116", "97124", "97140", "97530", "99072",
]
# fmt: on
TREATMENT_CODES = {
    "98940": "CMT Spine 1-2 regions",
    "98941": "CMT Spine 3-4 regions",
    "98942": "CMT Spine 5 regions",
    "98943": "CMT Extraspinal",
    "97010": "Hot/Cold Packs",
    "97012": "Mechanical Traction",
    "97014": "Electrical Stimulation",
    "G0283": "Electrical Stimulation",
    "97016": "Diathermy",
    "97018": "Paraffin Bath",
    "97022": "Whirlpool Therapy",
    "97026": "Infrared",
    "97032": "Attended Electrical Stimulation",
    "97033": "Iontophoresis",
    "97035": "Ultrasound",
    "97039": "Unlisted Procedure",
    "97110": "Therapeutic Exercise",
    "97112": "Neuromuscular Re-education",
    "97113": "Aquatic Exercise",
    "97116": "Gait Training",
    "97124": "Massage Therapy",
    "97140": "Manual Therapy",
    "97530": "Therapeutic Activities",
    "99072": "Additional Supplies/Staff Time",
}


# List and dicts for auxillary codes
AUXILLARY_CODE_DISPLAY_LAYOUT = [
    ["95999", "72146"],
    ["97535", "72148"],
    ["97750", "72195"],
    ["70336", "73221"],
    ["72141", "73723"],
]
# fmt: off
AUXILLARY_CODE_PRINT_LAYOUT = [
    "95999", "97535", "97750", "70336", "72141",
    "72146", "72148", "72195", "73221", "73723",
]
# fmt: on
AUXILLARY_CODES = {
    "95999": "PF-NCS testing",
    "97535": "Self Care/Home Management Training",
    "97750": "Physical Performance Test",
    "70336": "MRI TMJ without contrast",
    "72141": "MRI cervical spine without contrast",
    "72146": "MRI thoracic spine without contrast",
    "72148": "MRI lumbar spine without contrast",
    "72195": "MRI pelvis without contrast",
    "73221": "MRI upper extremity joint without contrast",
    "73723": "MRI lower extremity joint without contrast",
}


TEST_SPACE_LAYOUT = [
    [sg.Text("Clipboard Output and Test Space", font=("Helvetica", 18, "bold"))],
    [sg.Text("", key="-OUTPUT-", size=(80, 5))],
    [sg.Multiline(key="-TEST-SPACE-", size=(100, 5))],
    [
        sg.Text("", size=(80, 1)),
        sg.Button("Clear Text", key="-CLR-TEST-"),
        sg.Button("Quit", key="-QUIT-"),
    ],
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
        clinical_summary_layout = self._gen_clinical_summary_layout()
        layout = ACCIDENT_INFO_LAYOUT + clinical_summary_layout + TEST_SPACE_LAYOUT
        self.window = sg.Window("AutoBob SideKick", layout, font=("Helvetica", 14))

    def _gen_clinical_summary_layout(self):
        """
        Generate the layout for the clinical summary section of the window.
        The layout is generated by parsing the list of treatment codes and
        auxillary codes to generate the list of lists necessary to render the
        screen, adding in the section headers and additional fields and buttons.
        The generated layout is then returned to the calling function.
        """
        layout = [
            [sg.Text("Clinical Summary", font=("Helvetica", 18, "bold"))],
            [sg.Text("Treatment Codes", font=("Helvetica", 14, "bold"))],
        ]

        for code_row in TREATMENT_CODE_DISPLAY_LAYOUT:
            row = []
            for code in code_row:
                row.append(
                    sg.Checkbox(
                        code,
                        size=(6, 1),
                        key=f"-{code}-",
                        font=("Helvetica", 14, "bold"),
                    )
                )
                row.append(
                    sg.Text(TREATMENT_CODES[code], size=(25, 1), font=("Helvetica", 12))
                )
            layout.append(row)

        layout += [
            [
                sg.Text("Frequency", size=(9, 1)),
                sg.InputText(key="-CSUM-FREQ-", size=(4, 1)),
                sg.Text("", size=(1, 1)),
                sg.Text("Duration", size=(8, 1)),
                sg.InputText(key="-CSUM-DUR-", size=(4, 1)),
                sg.Text("", size=(1, 1)),
                sg.Text("From Date", size=(9, 1)),
                sg.InputText(key="-CSUM-FDATE-", size=(10, 1)),
                sg.CalendarButton(
                    "Calendar",
                    close_when_date_chosen=True,
                    target="-CSUM-FDATE-",
                    no_titlebar=False,
                    format="%m/%d/%Y",
                ),
                sg.Text("", size=(1, 1)),
                sg.Text("To Date", size=(7, 1)),
                sg.InputText(key="-CSUM-TDATE-", size=(10, 1)),
                sg.CalendarButton(
                    "Calendar",
                    close_when_date_chosen=True,
                    target="-CSUM-TDATE-",
                    no_titlebar=False,
                    format="%m/%d/%Y",
                ),
            ],
            [sg.Text("")],
            [sg.Text("Accessory Codes", font=("Helvetica", 14, "bold"))],
        ]

        for code_row in AUXILLARY_CODE_DISPLAY_LAYOUT:
            row = []
            for code in code_row:
                row.append(
                    sg.Checkbox(
                        code,
                        size=(6, 1),
                        key=f"-{code}-",
                        font=("Helvetica", 14, "bold"),
                    )
                )
                row.append(
                    sg.Text(AUXILLARY_CODES[code], size=(35, 1), font=("Helvetica", 12))
                )
                row.append(sg.InputText(key=f"-{code}-UNITS-", size=(2, 1)))
                row.append(sg.Text("", size=(5, 1)))
            layout.append(row)

        layout += [
            [
                sg.Text("Body parts to treat:"),
                sg.InputText(key="-CSUM-BPARTS-", size=(64, 1)),
                sg.Button("Generate", key="-CSUM-GEN-"),
                sg.Button("Reset", key="-CSUM-RESET-"),
            ],
            [sg.Text("", size=(40, 1)), sg.Text("", key="-CSUM-DIALOG-", size=(60, 1))],
        ]

        return layout

    def _clear_dialogs(self):
        """
        Clears all dialog text windows under all sections of the window.
        """
        self.window.Element("-AINFO-DIALOG-").Update(value="")
        self.window.Element("-CSUM-DIALOG-").Update(value="")
        self.window.Element("-OUTPUT-").Update(value="")

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

    def _gen_accident_info(self, values):
        """
        Generates the accident info text, updates the window, and copies
        the resulting data to the clipboard.
        """
        if values["-ACC-DESC-"] == "":
            dialog = "Error: accident description is empty!"
            self.window.Element("-AINFO-DIALOG-").Update(value=dialog)
            return

        self._clear_dialogs()
        accident = values["-ACC-DESC-"]
        if not accident.endswith("."):
            accident += "."

        if values["-BELTED-"]:
            seatbelt = f"{BELT['-BELTED-'].lower()} "
        elif values["-UNBELT-"]:
            seatbelt = f"{BELT['-UNBELT-'].lower()} "
        else:
            seatbelt = ""

        if values["-DRIVER-"]:
            role = ROLE["-DRIVER-"].lower()
        else:
            role = ROLE["-PASSENGER-"].lower()
            for seat in SEAT.keys():
                if values[seat]:
                    role = f"{SEAT[seat].lower()} {role}"
                    break

        statement = (
            f"wherein the claimant was the {seatbelt}{role}"
            + f" of a vehicle that was {accident}"
        )

        dialog = "Accident Info text generated and copied to clipboard below."
        self.window.Element("-AINFO-DIALOG-").Update(value=dialog)
        self.window.Element("-OUTPUT-").Update(value=statement)
        pyperclip.copy(statement)

    def _reset_accident_info(self):
        """
        Reset all fields under the accident info section back to defaults.
        """
        self.window.Element("-NOBELT-").Update(value=True)
        self.window.Element("-DRIVER-").Update(value=True)
        self.window.Element("-ACC-DESC-").Update(value="")
        self._handle_seat_choices(disabled=True)

        dialog = "Accident info section reset to defaults."
        self.window.Element("-AINFO-DIALOG-").Update(value=dialog)

    def _is_valid_date(self, datestring):
        """
        Check if the passed string is a valid date and return a boolean of the result.
        """
        try:
            month, day, year = datestring.split("/")
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            return False

        return True

    def _gen_clinical_summary(self, values):
        """
        Generates the clinical summary text, updates the window, and copies
        the resulting data to the clipboard. Performs error-checking to ensure
        all fields are filled out as expected.
        """
        frequency = values["-CSUM-FREQ-"]
        duration = values["-CSUM-DUR-"]
        from_date = values["-CSUM-FDATE-"]
        to_date = values["-CSUM-TDATE-"]

        if not frequency.isdigit() or not duration.isdigit():
            dialog = "Error: invalid treatment code frequency or duration!"
            self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
            return

        if not self._is_valid_date(from_date) or not self._is_valid_date(to_date):
            dialog = "Error: invalid treatment code from or to date!"
            self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
            return

        checked_treatement_codes = []
        for code in TREATMENT_CODE_PRINT_LAYOUT:
            if values[f"-{code}-"]:
                checked_treatement_codes.append(code)

        if len(checked_treatement_codes) == 0:
            dialog = "Error: no treatment codes were selected!"
            self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
            return

        statement = (
            f"The provider is requesting {treatment_code_text} at a "
            + f"frequency of {frequency} visits per week for {duration} "
            + f"weeks for the period of {from_date} through {to_date}."
        )

        checked_auxillary_codes = []
        for code in AUXILLARY_CODE_PRINT_LAYOUT:
            if values[f"-{code}-"]:
                checked_auxillary_codes.append(code)

        dialog = "Clinical summary text generated and copied to clipboard below."
        self.window.Element("-CSUM-DIALOG-").Update(value=dialog)

    def _reset_clinical_summary(self):
        """
        Reset all fields under the clinical summary section back to defaults.
        """
        for code in TREATMENT_CODE_PRINT_LAYOUT:
            self.window.Element(f"-{code}-").Update(value=False)

        self.window.Element("-CSUM-FREQ-").Update(value="")
        self.window.Element("-CSUM-DUR-").Update(value="")
        self.window.Element("-CSUM-FDATE-").Update(value="")
        self.window.Element("-CSUM-TDATE-").Update(value="")

        for code in AUXILLARY_CODE_PRINT_LAYOUT:
            self.window.Element(f"-{code}-").Update(value=False)
            self.window.Element(f"-{code}-UNITS-").Update(value="")

        dialog = "Clinical summary section reset to defaults."
        self.window.Element("-CSUM-DIALOG-").Update(value=dialog)

    def main_loop(self):
        """
        Main routine for AutoBob SideKick.
        Responds to window events and routes all events to the appropriate
        member functions of the AutoBob class.
        """
        while True:
            event, values = self.window.read()

            if event == "-QUIT-" or event == sg.WIN_CLOSED:
                break

            if event == "-DRIVER-" or event == "-PASSENGER-":
                self._select_role(event)
            elif event == "-CLRSEAT-":
                self._handle_seat_choices()
            elif event == "-AINFO-RESET-":
                self._reset_accident_info()
            elif event == "-AINFO-GEN-":
                self._gen_accident_info(values)
            elif event == "-CSUM-RESET-":
                self._reset_clinical_summary()
            elif event == "-CSUM-GEN-":
                self._gen_clinical_summary(values)
            elif event == "-CLR-TEST-":
                self.window.Element("-TEST-SPACE-").Update(value="")

    def close(self):
        """
        Closes the window and cleans up the program.
        """
        self.window.close()


if __name__ == "__main__":
    autobob = AutoBob()
    autobob.main_loop()
    autobob.close()
