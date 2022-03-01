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
from .fields import (
    BELT,
    ROLE,
    SEAT,
    TREATMENT_TYPE_LAYOUT,
    TREATMENT_TYPES,
    TREATMENT_TYPE_DENIALS,
)
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
        column_layout = ACCIDENT_INFO_LAYOUT + clinical_summary_layout + OUTPUT_LAYOUT
        layout = [
            [sg.Column(column_layout, scrollable=True, expand_x=True, expand_y=True)]
        ]
        self.window = sg.Window(
            "AutoBob SideKick",
            layout,
            font=("Helvetica", 14),
            resizable=True,
            size=(1130, 850),
        )

    def _gen_treatment_code_layout(self):
        """
        Generate the treatment code layout for the GUI and return to the calling function.
        """
        code_layout = []

        for code_row in TREATMENT_CODE_DISPLAY_LAYOUT:
            row = []
            for code in code_row:
                row.append(
                    sg.Checkbox(
                        code,
                        size=(8, 1),
                        key=f"-TC-{code}-",
                        font=("Helvetica", 14, "bold"),
                    )
                )
                row.append(
                    sg.Text(TREATMENT_CODES[code], size=(25, 1), font=("Helvetica", 12))
                )
            code_layout.append(row)

        return code_layout

    def _gen_auxillary_code_layout(self):
        """
        Generate the treatment code layout for the GUI and return to the calling function.
        """
        aux_layout = []

        for code_row in AUXILLARY_CODE_DISPLAY_LAYOUT:
            row = []
            for not_first, code in enumerate(code_row):
                if not_first:
                    row.append(sg.Text("", size=(8, 1)))
                row.append(
                    sg.Checkbox(
                        code,
                        size=(8, 1),
                        key=f"-AC-{code}-",
                        font=("Helvetica", 14, "bold"),
                    )
                )
                row.append(
                    sg.Text(AUXILLARY_CODES[code], size=(35, 1), font=("Helvetica", 12))
                )
                row.append(sg.InputText(key=f"-AC-{code}-UNITS-", size=(2, 1)))
            aux_layout.append(row)

        return aux_layout

    def _gen_treatment_type_layout(self):
        """
        Generate the layout for the treatment types and return to the calling function.
        """
        type_layout = []

        for treatment in TREATMENT_TYPE_LAYOUT:
            row = [
                sg.Text(
                    TREATMENT_TYPES[treatment],
                    size=(15, 1),
                    font=("Helvetica", 12, "bold"),
                ),
                sg.InputText(key=f"-{treatment}-UNITS-", size=(4, 1)),
                sg.Text("", size=(1, 1)),
                sg.Text("From Date", size=(9, 1)),
                sg.InputText(key=f"-{treatment}-FDATE-", size=(10, 1)),
                sg.CalendarButton(
                    "Calendar",
                    key=f"-{treatment}-FCAL-",
                    close_when_date_chosen=True,
                    target=f"-{treatment}-FDATE-",
                    no_titlebar=False,
                    format="%m/%d/%Y",
                ),
                sg.Text("", size=(1, 1)),
                sg.Text("To Date", size=(7, 1)),
                sg.InputText(key=f"-{treatment}-TDATE-", size=(10, 1)),
                sg.CalendarButton(
                    "Calendar",
                    key=f"-{treatment}-TCAL-",
                    close_when_date_chosen=True,
                    target=f"-{treatment}-TDATE-",
                    no_titlebar=False,
                    format="%m/%d/%Y",
                ),
                sg.Text("", size=(1, 1)),
                sg.Checkbox(
                    "Not Approved",
                    size=(12, 1),
                    key=f"-{treatment}-DENY-",
                    enable_events=True,
                ),
            ]
            type_layout.append(row)

        return type_layout

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

        layout += self._gen_treatment_code_layout() + TREATMENT_DATE_LAYOUT

        layout += [
            [sg.HorizontalSeparator()],
            [sg.Text("Accessory Codes", font=("Helvetica", 14, "bold"))],
        ]

        layout += self._gen_auxillary_code_layout()

        layout += [
            [sg.HorizontalSeparator()],
            [sg.Text("Treatment Types", font=("Helvetica", 14, "bold"))],
        ]

        layout += self._gen_treatment_type_layout() + CLIENT_SUMMARY_FOOTER

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

        self._clear_dialogs()
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
            if values[f"-TC-{code}-"]:
                checked_treatement_codes.append(code)

        # Process auxillary code text if necessary
        checked_auxillary_codes = []
        for code in AUXILLARY_CODE_PRINT_LAYOUT:
            if values[f"-AC-{code}-"]:
                checked_auxillary_codes.append(code)

        # Verify at least one code is checked
        num_of_codes = len(checked_treatement_codes)
        num_of_aux_codes = len(checked_auxillary_codes)
        if num_of_codes == 0 and num_of_aux_codes == 0:
            dialog = "Error: no treatment codes were selected!"
            self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
            return

        if num_of_codes > 0 and (not frequency.isdigit() or not duration.isdigit()):
            dialog = "Error: invalid treatment code frequency or duration!"
            self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
            return

        # Parse and validate treatment types
        selected_treatments = []
        for treatment in TREATMENT_TYPE_LAYOUT:
            units = values[f"-{treatment}-UNITS-"]
            treatment_from = values[f"-{treatment}-FDATE-"]
            treatment_to = values[f"-{treatment}-TDATE-"]
            not_approved = values[f"-{treatment}-DENY-"]
            treatment_text = TREATMENT_TYPES[treatment].lower()

            if units:
                if not units.isdigit():
                    dialog = f"Error: invalid {treatment_text} frequency!"
                    self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
                    return
                selected_treatments.append(treatment)

                if treatment_from:
                    if not self._is_valid_date(treatment_from):
                        dialog = f"Error: invalid {treatment_text} from date!"
                        self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
                        return

                    if not treatment_to:
                        dialog = f"Error: {treatment_text} from date specified without to date!"
                        self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
                        return

                if treatment_to and not self._is_valid_date(treatment_to):
                    dialog = f"Error: invalid {treatment_text} to date!"
                    self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
                    return

            elif not_approved:
                selected_treatments.append(treatment)

            elif treatment_from or treatment_to:
                dialog = f"Error: {treatment_text} dates specified without units!"
                self.window.Element("-CSUM-DIALOG-").Update(value=dialog)
                return

        # Clear dialogs since function has passed error handling
        self._clear_dialogs()

        # Process treatment code text
        if num_of_codes > 0:
            treatment_code_text = ""
            for count, code in enumerate(checked_treatement_codes):
                if count != 0:
                    if num_of_codes > 2:
                        treatment_code_text += ","
                    treatment_code_text += " "

                if count == num_of_codes - 1 and count > 0:
                    treatment_code_text += "and "

                treatment_code_text += f"{code} - {TREATMENT_CODES[code]}"

            if int(frequency) == 1:
                f_plural = ""
            else:
                f_plural = "s"

            if int(duration) == 1:
                d_plural = ""
            else:
                d_plural = "s"

            statement = (
                f"The provider is requesting {treatment_code_text} at a frequency "
                + f"of {frequency} visit{f_plural} per week for {duration} week{d_plural} "
                + f"for the period of {from_date} through {to_date}."
            )

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

                if values[f"-AC-{code}-UNITS-"]:
                    auxillary_code_text += f" ({values[f'-AC-{code}-UNITS-']} units)"

            if num_of_codes == 0:
                statement = (
                    f"The provider is requesting {auxillary_code_text} "
                    + f"for the period of {from_date} through {to_date}."
                )

            else:
                statement += (
                    f" Additionally, the provider is requesting {auxillary_code_text} "
                    + f"for the same time period."
                )

        # Process treatment type text
        num_of_treatments = len(selected_treatments)
        if num_of_treatments > 0:
            treatments = ""
            for count, treatment in enumerate(selected_treatments):
                if count != 0:
                    if num_of_treatments > 2:
                        treatments += ","
                    treatments += " "

                if count == num_of_treatments - 1 and count > 0:
                    treatments += "and "

                if values[f"-{treatment}-DENY-"]:
                    units = 0
                else:
                    units = values[f"-{treatment}-UNITS-"]

                if int(units) == 1:
                    plural = ""
                else:
                    plural = "s"

                from_date = values[f"-{treatment}-FDATE-"]
                to_date = values[f"-{treatment}-TDATE-"]

                if from_date and to_date:
                    time_period =  f"from {from_date} to {to_date}"
                elif to_date:
                    time_period = f"through {to_date}"
                else:
                    time_period = "to date"

                treatments += (
                    f"{units} {TREATMENT_TYPES[treatment]} unit{plural} {time_period}"
                )

            statement += (
                f" It is noted that the claimant has been approved for {treatments}."
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

    def _handle_treatment_type(self, treatment_type, disabled=False):
        """
        Handle the enabling or disabling of the treatment type.
        """
        self.window.Element(f"-{treatment_type}-UNITS-").Update(disabled=disabled)
        self.window.Element(f"-{treatment_type}-FDATE-").Update(disabled=disabled)
        self.window.Element(f"-{treatment_type}-FCAL-").Update(disabled=disabled)
        self.window.Element(f"-{treatment_type}-TDATE-").Update(disabled=disabled)
        self.window.Element(f"-{treatment_type}-TCAL-").Update(disabled=disabled)

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
        self.window.Element("-CSUM-BPARTS-").Update(value="")

        for code in AUXILLARY_CODE_PRINT_LAYOUT:
            self.window.Element(f"-{code}-").Update(value=False)
            self.window.Element(f"-{code}-UNITS-").Update(value="")

        for treatment_type in TREATMENT_TYPE_LAYOUT:
            self.window.Element(f"-{treatment_type}-UNITS-").Update(
                value="", disabled=False
            )
            self.window.Element(f"-{treatment_type}-FDATE-").Update(
                value="", disabled=False
            )
            self.window.Element(f"-{treatment_type}-FCAL-").Update(disabled=False)
            self.window.Element(f"-{treatment_type}-TDATE-").Update(
                value="", disabled=False
            )
            self.window.Element(f"-{treatment_type}-TCAL-").Update(disabled=False)
            self.window.Element(f"-{treatment_type}-DENY-").Update(value=False)

        self._clear_dialogs()
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
            elif event in TREATMENT_TYPE_DENIALS:
                self._handle_treatment_type(
                    TREATMENT_TYPE_DENIALS[event], values[event]
                )
            elif event == "-CLR-TEXT-":
                self.window.Element("-OUTPUT-").Update(value="")

    def close(self):
        """
        Closes the window and cleans up the program.
        """
        self.window.close()
