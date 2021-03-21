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

AUXILLARY_CODE_PRINT_LAYOUT = [
    "95999",
    "97535",
    "97750",
    "70336",
    "72141",
    "72146",
    "72148",
    "72195",
    "73221",
    "73723",
]

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
