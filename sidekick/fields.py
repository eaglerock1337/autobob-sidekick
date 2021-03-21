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


# Lists and dicts for treatment type layout
TREATMENT_TYPE_LAYOUT = ["PT", "CHI", "ACU"]

TREATMENT_TYPES = {
    "PT": "PT",
    "CHI": "Chiropractic",
    "ACU": "Acupuncture",
}

TREATMENT_TYPE_DENIALS = {
    "-PT-DENY-": "PT",
    "-CHI-DENY-": "CHI",
    "-ACU-DENY-": "ACU",
}
