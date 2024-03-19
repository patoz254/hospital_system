class Patient:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, patient, doctor, date, time):
        appointment = Appointment(patient, doctor, date, time)
        self.appointments.append(appointment)

# Usage example
hospital = Hospital("ABC Hospital")

patient1 = Patient("John Doe", 30, "Male", "123 Main St")
hospital.add_patient(patient1)

doctor1 = Doctor("Dr. Smith", "Cardiologist")
hospital.add_doctor(doctor1)

hospital.schedule_appointment(patient1, doctor1, "2024-02-28", "10:00 AM")
