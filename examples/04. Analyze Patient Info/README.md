# Patient Info

This example is about filtering a huge list of `patients` by their treatment type.

## Files

### `patients.json`

`patients.json` contains a list of 1000 mock patients in `JSON` format.

(See [JSON - Introduction | W3Schools](https://www.w3schools.com/js/js_json_intro.asp))

#### Patient data model

Each patient in the list is a `JSON object` and looks like the below [example](#json-example).

The `diagnosis` list, within each `patient object`, may have 0-5 diagnosis `objects`, inside of those `objects` is a `key` called `diagnosis_code` that uses a "ICD10 diagnosis code". (See [cms.gov](https://www.cms.gov/))

##### JSON Example

```json
{
  "patient_id": 1,
  "first_name": "Corenda",
  "last_name": "Hernik",
  "age": 107,
  "gender": "Female",
  "diagnosis": [
    {
      "diagnosis_code": "S52272C", 
      "diagnosis_desc": "Monteggia's fracture of left ulna, initial encounter for open fracture type IIIA, IIIB, or IIIC",
      "diagnosis_date": "10/26/2008",
      "treatment": "surgery",
      "doctor_name": "Damian Brooking"
    }
  ]
}
```

### `app.py`

In `app.py` We import the `json` library so we can read the data from the `patients.json` file. We then open the json file, parse the data from the file and store it as a variable called `patents`, this is our huge list imported and ready to filter.

```python
import json

patients_json = open("./patients.json")
patients = json.load(patients_json)
```

We then define a function to filter patient records by what treatments they have been given/waiting for, to do this we define an empty list inside the function to fill with patients that meet our critera.
We loop with a `for` loop through each `patient` in the list of `patients` and check each of the diagnosis' treatment, if the treatment on the patient is the same as what we are looking for then we add the `patient`` the list of filtered patients.
When we have finished the big list of patients we return the filtered patients.

```python
def filterPatients(treatment: str, patients: list) -> list:
    patientsList = []
    for patient in patients:
        for diag in patient["diagnosis"]:
            if diag["treatment"] == treatment:
                patientsList.append(patient)
    return patientsList
```

With the above function setup we can store 2 types of queries as variables:
- patients that have had/need Surgery
- patients that have had/need Therapy

```python
patientsThatNeedTherapy = filterPatients("therapy", patients)
patientsThatNeedSurgery = filterPatients("surgery", patients)
```

By checking the length of the 2 filtered lists, using the `len()` function built into python, we can print the number of patients for each type of treatment.

```python
print(f"{len(patientsThatNeedTherapy)} need Therapy")
print(f"{len(patientsThatNeedSurgery)} need Surgery")
```