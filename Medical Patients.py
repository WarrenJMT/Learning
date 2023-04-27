import pickle


class Patient:    # A patient class with all the patient's attributes.
    def __init__(self,first_name, last_name, dob, gender, allergy):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.allergy = allergy
        self.gender = gender

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.dob} {self.allergy}"

    def fnln(self):     # First name Last name object method.
        return f"{self.first_name} {self.last_name}"


patient_first_name = input('Patients first name: ')
patient_last_name = input('Patients last name: ')
dob = int(input('Date of birth (d/m/y): '))
gender = input('Gender m or f: ')
allergies = {'celery', 'eggs', 'fish', 'milk', 'peanuts', 'sesame', 'soybeans', 'pollen', 'dust', 'mould',
             'latex', 'penicillin', 'aspirin', 'chickpea', 'walnuts', 'tree nuts'}
            # Add as many specific allergies as possible. (Not the type of allergy)

allergy = input(f'Does {patient_first_name} {patient_last_name} have any allergies? ')
male = []
female = []
prescriptions = []
patients_with_no_allergies = []
patients_with_allergies = []
patient = Patient(patient_first_name, patient_last_name, dob, gender, allergy)
patients = []



def initialize_add_new_patient(new_patients):    # initialize new patient function
    try:    # Tries to read the Medical Patients.txt, that stores all patients.
        with open('Medical Patients.txt', 'rb') as file:
            patients = pickle.load(file)
            if new_patients in patients:
                print('This patient is already in the system')
                return
    except:
        patients = []

    if new_patients.gender == 'm':
        male.append(new_patients)
        patients.append(new_patients)

        print(new_patients.fnln())
        print('has been added to the list of males')

    if new_patients.gender == 'f':
        female.append(new_patients)
        patients.append(new_patients)

        print(f'{new_patients.fnln()} has been added to the list of females')

    if new_patients.allergy in allergies:
        patients_with_allergies.append(new_patients)

        print(new_patients.fnln() + ' has been added to the list of patients with allergies')

    if new_patients.allergy not in allergies:
        patients_with_no_allergies.append(new_patients)

        print(new_patients.fnln() + ' has no known allergies')

    with open('Medical Patients.txt', 'ab') as fp:    # Dumps (stores) the new patient into the Medical Patients.txt.
        pickle.dump(new_patients, fp)


initialize_add_new_patient(patient)

