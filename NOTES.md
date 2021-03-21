# Accident Information

Provided text - "The review is for patient {full name}, {DOB}, who was involved in an automobile on {date},"

Needed: "wherein the claimant was the {restrained/unrestrained/neither - checkboxes} {driver/front seat passenger/LR/RR/rear seat passenger} of a vehicle that was {struck/rear-ended on the front driver's side - text box}"

# Clinical Summary

## Treatment Codes

Text needed: "The provider is requesting {CPT Code} - {CPT Code Name},
{CPT Code} - {CPT Code Name}, {CPT Code} - {CPT Code Name}, and
{CPT Code} - {CPT Code Name} at a frequency of {x} visits per week for
{y} weeks for the period of {start-date} through {end-date}."

The application needs to generate text in a text box dynamically from a form.

The form will have the following buttons:

- 98940 - CMT Spine 1-2 regions
- 98941 - CMT Spine 3-4 regions
- 98942 - CMT Spine 5 regions
- 98943 - CMT Extraspinal
- 97010 - Hot/Cold Packs
- 97012 - Mechanical Traction
- 97014 - Electrical Stimulation
- G0283 - Electrical Stimulation
- 97016 -  Diathermy
- 97018 - Paraffin Bath
- 97022 - Whirlpool Therapy
- 97026 - Infrared
- 97032 - Attended Electrical Stimulation
- 97033 - Iontophoresis
- 97035 - Ultrasound
- 97039 - Unlisted Procedure
- 97110 - Therapeutic Exercise
- 97112 - Neuromuscular Re-education
- 97113 - Aquatic Exercise
- 97116 - Gait Training
- 97124 - Massage Therapy
- 97140 - Manual Therapy
- 97530 - Therapeutic Activities
- 99072 - Additional Supplies/Staff Time

There will be a text field labeled “frequency” and another text field labeled “duration”.

There will be two date fields, a “from date” and a “to date”

Clicking each button will add this text to a list that will be in the form of a sentence as follows:

"The provider is requesting x, y, and z, at a frequency of (frequency) visits per week for (duration) weeks for the period of (from date) through (to date)."

## Auxillary Codes

There will then be a second list of codes:

- 95999 - PF-NCS testing
- 97535 - Self Care/Home Management Training
- 97750 - Physical Performance Test
- 70336 - MRI TMJ without contrast
- 72141 - MRI cervical spine without contrast
- 72146 - MRI thoracic spine without contrast
- 72148 - MRI lumbar spine without contrast
- 72195 - MRI pelvis without contrast
- 73221 - MRI upper extremity joint without contrast
- 73723 - MRI lower extremity joint without contrast

Each of these codes will have a text field next to it specifying the number of units.

The text box will then generate the sentence “Additionally, the provider is requesting x, y, and z for the same time period.” If the number of units for the code is blank, it will not specify a number of units, otherwise, it will generate the sentence as “Additionally, the provider is requesting x (q units), y and z for the same time period”.

## Request/Approval Details

There are three checkboxes: {PT, chiropractic, acupuncture}

Text to generate: "It is noted that the claimant has been approved for {x} PT visits from {start date} to {end date} and {y} chiropractic visits"

If date field is empty, substitute start/end date with "to present"

Checkbox: "initial request" Change text to:
"It is noted that this is the initial request for {PT XOR chiropractic - dropdown}." - substitutes above sentence

Checkbox: "denied" Change text to:
"It is noted that the claimant has not been approved for any {PT xor chiropractic - dropdown} units to date."

Last sentence:
"It is noted that the body parts being requested for treatment are {text field}"
