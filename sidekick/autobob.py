import datetime
import pyperclip
import PySimpleGUI as sg

from .codes import (
    TREATMENT_CODE_DISPLAY_LAYOUT,
    TREATMENT_CODE_PRINT_LAYOUT,
    TREATMENT_CODES,
    AUXILLARY_CODE_DISPLAY_LAYOUT,
    AUXILLARY_CODE_PRINT_LAYOUT,
    AUXILLARY_CODES,
)
from .fields import BELT, ROLE, SEAT
from .layouts import (
    GUI_THEME,
    ACCIDENT_INFO_LAYOUT,
    TREATMENT_DATE_LAYOUT,
    CLIENT_SUMMARY_FOOTER,
    OUTPUT_LAYOUT,
)


# Set gui theme
sg.theme(GUI_THEME)


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
        layout = ACCIDENT_INFO_LAYOUT + clinical_summary_layout + OUTPUT_LAYOUT
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

        layout += TREATMENT_DATE_LAYOUT + [
            [sg.HorizontalSeparator()],
            [sg.Text("Accessory Codes", font=("Helvetica", 14, "bold"))],
        ]

        for code_row in AUXILLARY_CODE_DISPLAY_LAYOUT:
            row = []
            for not_first, code in enumerate(code_row):
                if not_first:
                    row.append(sg.Text("", size=(5, 1)))
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
            layout.append(row)

        layout += [
            [sg.HorizontalSeparator()],
            [sg.Text("Request/Approval Details", font=("Helvetica", 14, "bold"))],
        ]

        layout += CLIENT_SUMMARY_FOOTER

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

        dialog = (
            "Accident info text generated, copied to clipboard, and displayed below."
        )
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

        # Assign values and perform initial error handling
        frequency = values["-CSUM-FREQ-"]
        duration = values["-CSUM-DUR-"]
        from_date = values["-CSUM-FDATE-"]
        to_date = values["-CSUM-TDATE-"]
        body_parts = values["-CSUM-BPARTS-"]

        if not frequency.isdigit() or not duration.isdigit():
            dialog = "Error: invalid treatment code frequency or duration!"
            self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
            return

        if not self._is_valid_date(from_date) or not self._is_valid_date(to_date):
            dialog = "Error: invalid treatment code from or to date!"
            self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
            return

        if not body_parts:
            dialog = "Error: no body parts specified for treatment!"
            self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
            return

        # Parse checked treatment codes
        checked_treatement_codes = []
        for code in TREATMENT_CODE_PRINT_LAYOUT:
            if values[f"-{code}-"]:
                checked_treatement_codes.append(code)

        # Verify at least one code is checked
        num_of_codes = len(checked_treatement_codes)
        if num_of_codes == 0:
            dialog = "Error: no treatment codes were selected!"
            self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
            return

        # Process treatment code text
        treatment_code_text = ""
        for count, code in enumerate(checked_treatement_codes):
            if count != 0:
                if num_of_codes > 2:
                    treatment_code_text += ","
                treatment_code_text += " "

            if count == num_of_codes - 1 and count > 0:
                treatment_code_text += "and "

            treatment_code_text += f"{code} - {TREATMENT_CODES[code]}"

        if int(duration) == 1:
            plural = "s"
        else:
            plural = ""

        statement = (
            f"The provider is requesting {treatment_code_text} at a frequency "
            + f"of {frequency} visits per week for {duration} week{plural} "
            + f"for the period of {from_date} through {to_date}."
        )

        # Process auxillary code text if necessary
        checked_auxillary_codes = []
        for code in AUXILLARY_CODE_PRINT_LAYOUT:
            if values[f"-{code}-"]:
                checked_auxillary_codes.append(code)

        num_of_aux_codes = len(checked_auxillary_codes)
        if num_of_aux_codes > 0:
            auxillary_code_text = ""
            for count, code in enumerate(checked_auxillary_codes):
                if count != 0:
                    if num_of_aux_codes > 2:
                        auxillary_code_text += ","
                    auxillary_code_text += " "

                if count == num_of_aux_codes - 1 and count > 0:
                    auxillary_code_text += "and "

                auxillary_code_text += f"{code} - {AUXILLARY_CODES[code]}"

                if values[f"-{code}-UNITS-"]:
                    auxillary_code_text += f" ({values[f'-{code}-UNITS-']} units)"

            statement += (
                f" Additionally, the provider is requesting {auxillary_code_text} "
                + f"for the same time period."
            )

        # Process final sentence
        if not body_parts.endswith("."):
            body_parts += "."

        statement += (
            " It is noted that the body parts being requested for "
            + f"treatment are {body_parts}"
        )

        # Display text and copy to clipboard
        dialog = (
            "Clinical summary text generated, copied to clipboard, and displayed below."
        )
        self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
        self.window.Element("-OUTPUT-").Update(value=statement)
        pyperclip.copy(statement)

    """
    three checkboxes: {PT, chiropractic, acupuncture}
    "It is noted that the claimant has been approved for {x} PT visits from {start date}
    to {end date} and {y} chiropractic visits"
    if date field is empty, substitute start/end date with "to present"

    Checkbox: "initial request" Change text to:
    "It is noted that this is the initial request for {PT XOR chiropractic - dropdown}."
    - substitutes above sentence
    Checkbox: "denied" Change text to:
    "It is noted that the claimant has not been approved for any {PT xor chiropractic
    - dropdown} units to date."

    Last sentence:
    "It is noted that the body parts being requested for treatment are {text field}."
    """

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
            elif event == "-CLR-TEXT-":
                self.window.Element("-OUTPUT-").Update(value="")

    def close(self):
        """
        Closes the window and cleans up the program.
        """
        self.window.close()
