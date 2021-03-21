import PySimpleGUI as sg

from .fields import BELT, ROLE, SEAT


# Set gui theme for module
# GUI_THEME = "LightBlue" # Light mode
GUI_THEME = "DarkBlue14"  # Dark mode
sg.theme(GUI_THEME)


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


TREATMENT_DATE_LAYOUT = [
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
    ]
]


CLIENT_SUMMARY_FOOTER = [
    [
        sg.Text("Body parts to treat:"),
        sg.InputText(key="-CSUM-BPARTS-", size=(64, 1)),
        sg.Button("Generate", key="-CSUM-GEN-"),
        sg.Button("Reset", key="-CSUM-RESET-"),
    ],
    [sg.Text("", size=(40, 1)), sg.Text("", key="-CSUM-DIALOG-", size=(60, 1))],
]


OUTPUT_LAYOUT = [
    [sg.Text("Clipboard Output and Test Space", font=("Helvetica", 18, "bold"))],
    [sg.Multiline(key="-OUTPUT-", size=(100, 5))],
    [
        sg.Text("", size=(80, 1)),
        sg.Button("Clear Text", key="-CLR-TEXT-"),
        sg.Button("Quit", key="-QUIT-"),
    ],
]
