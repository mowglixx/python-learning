# import json so we can read the data from the 'patients.json' file
import json

# open the json file
patients_json = open("./patients.json")

# we parse the data from the file
patients = json.load(patients_json)


# we define a function to filter patient records by what treatments they have been given/waiting for
def filterPatients(treatment: str, patients: list) -> list:
    # define an empty list to fill with patients that meet our critera
    patientsList = []
    # for each patient in the list of patients
    for patient in patients:
        # check each of the diagnosis
        for diag in patient["diagnosis"]:
            # if the treatment on the patient is the same as what we are looking for
            if diag["treatment"] == treatment:
                # add the patient the list of filtered patients
                patientsList.append(patient)
    # return the filtered patients when all of the above has run
    return patientsList


# storing 2 types of queries in these variables
# patients that need surgery
patientsThatNeedTherapy = filterPatients("therapy", patients)
# patients that need therapy
patientsThatNeedSurgery = filterPatients("surgery", patients)


# printing the number of patients for each
print(
    # patientsThatNeedTherapy,
    f"{len(patientsThatNeedTherapy)} need Therapy"
)
print(
    # patientsThatNeedSurgery,
    f"{len(patientsThatNeedSurgery)} need Surgery"
)
