# Notes

## Accident Information

Provided text - "The review is for patient {full name}, {DOB}, who was involved in an automobile on {date},"

Needed: "wherein the claimant was the {restrained/unrestrained/neither - checkboxes} {driver/front seat passenger/LR/RR/rear seat passenger} of a vehicle that was {struck/rear-ended on the front driver's side - text box}"

## Clinical Summary

### Treatment Codes

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
- 97016 - Diathermy
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

### Auxillary Codes

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

### Request/Approval Details

Three rows: PT, Chiropractic, Acupuncture

Each row:

- Text box for number of units (check for integer)
- From date (check for date)
- To date (check for date)

For each row:

- If number of units is nonzero, and both dates are blank:
  - "It is noted that the claimant has been approved for `units` `type` visits to date.

- If to date is filled but from date is blank:
  - "It is noted that the claimant has been approved for `units` `type` visits through `to date`.

- If both dates are filled out:
  - "It is noted that the claimant has been approved for `units` `type` visits from `from date` to `to date`.

- If more than one treatment is filled in above:
  - "It is noted that the claimant has been approved for `x chiropractic visits <date stuff>` and `y acupuncture visits to date`.

Contingency for initial requests and denied:

- Each row gets a `not approved` checkbox
- Would gray out the row
- Changes wording to "It is noted that the claimant has been approved for `0` `type` visits to date.

### Final Sentence

"It is noted that the body parts being requested for treatment are {text field}"

## New Idea

- On the top - Date field for date of Accident
  - Based upon this, automatically calculate how long it's been since the accident's FROM date in half-month intervals
  - e.g. Accident, 3/1/22, First treatment date - 3/22/22
  - Whole months +
    - < 1 week: "More than X months"
    - 1-2 weeks: "Nearly X 1/2 months"
    - 2-3 weeks: "More than X 1/2 months"
    - more: "Nearly X+1 months"
    - "It has been {interval} since the accident."
  - All he wants is a date picker and a display that says that text
- Depending on the TREATMENT codes are selected, certain sentences to get generated:
  - If 9894x codes, generate the sentence:
    - "The submitted documentation does not substantiate that chiropractic treatment is medically necessary with respect to the motor vehicle accident of {date of accident}."
  - If 97112, generate the sentence:
    - "The submitted documentation does not substantiate that neuromuscular re-education is medically necessary with respect to the motor vehicle accident of {date of accident}."
  - If 99072, generate the sentence:
    - "The submitted documentation does not substantiate that the service is medically necessary with respect to the motor vehicle accident of {date of accident}."
  - If any of the other treatment codes:
    - "The submitted documentation does not substantiate that therapy is medically necessary with respect to the motor vehicle accident of {date of accident}."

### My Own Ideas

- Create a tabbing interface at the top to create multiple sections for different tasks
- Create a spiffy header with a lulzy picture of Rob as an easter egg
- See if I can do a stupid animation on the picture too
- See if I can speed up the start time by parallelizing the loading tasks
