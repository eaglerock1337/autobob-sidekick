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
    ["98960", "97024", "90901"],
    ["S9090"],
]

TREATMENT_CODE_PRINT_LAYOUT = [
    "98940",
    "98941",
    "98942",
    "98943",
    "97010",
    "97012",
    "97014",
    "G0283",
    "97016",
    "97018",
    "97022",
    "97026",
    "97032",
    "97033",
    "97035",
    "97039",
    "97110",
    "97112",
    "97113",
    "97116",
    "97124",
    "97140",
    "97530",
    "99072",
    "98960",
    "97024",
    "90901",
    "S9090",
]

TREATMENT_CODES = {
    "98940": "CMT Spine 1-2 regions",
    "98941": "CMT Spine 3-4 regions",
    "98942": "CMT Spine 5 regions",
    "98943": "CMT Extraspinal",
    "97010": "Hot/Cold Packs",
    "97012": "Mechanical Traction",
    "97014": "Electrical Stimulation",
    "G0283": "Electrical Stimulation",
    "97016": "Vasopneumatic Devices",
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
    "98960": "Education & Training Self-Mgmt",
    "97024": "Diathermy",
    "90901": "Biofeedback Training",
    "S9090": "VAX Decompression",
}


# List and dicts for auxillary codes
AUXILLARY_CODE_DISPLAY_LAYOUT = [
    ["95999", "70336"],
    ["97535", "72141"],
    ["97750", "72146"],
    ["97110", "72148"],
    ["A4556", "72195"],
    ["A9150", "73221"],
    ["E0190", "73721"],
    ["L0631", "70551"],
    ["E0855", "A4595"],
]

AUXILLARY_CODE_PRINT_LAYOUT = [
    "95999",
    "97535",
    "97750",
    "97110",
    "A4556",
    "A9150",
    "E0190",
    "L0631",
    "E0855",
    "70336",
    "72141",
    "72146",
    "72148",
    "72195",
    "73221",
    "73721",
    "70551",
    "A4595",
]

AUXILLARY_CODES = {
    "95999": "PF-NCS testing",
    "97535": "Self Care/Home Management Training",
    "97750": "Physical Performance Test",
    "97110": "Therapeutic Exercise",
    "A4556": "Electrodes",
    "A9150": "Non-Prescription Drug",
    "E0190": "Positioning Pillow",
    "L0631": "LSO Brace",
    "E0855": "Cervical Traction Equipment",
    "70336": "MRI TMJ without contrast",
    "72141": "MRI cervical spine without contrast",
    "72146": "MRI thoracic spine without contrast",
    "72148": "MRI lumbar spine without contrast",
    "72195": "MRI pelvis without contrast",
    "73221": "MRI upper extremity joint without contrast",
    "73721": "MRI lower extremity joint without contrast",
    "70551": "MRI brain without contrast",
    "A4595": "Electrical Stimulator Leads",
}
