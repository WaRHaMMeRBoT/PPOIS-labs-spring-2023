import dataclasses
from typing import Optional
from .utils import FileUtils


class Patients:
    def __init__(self, collection) -> None:
        self.__patients = collection

    def to_dict(self):
        data = dict()
        data["patient"] = [patient.to_dict() for patient in self.__patients]
        return data

    def add_to_patients_list(self, patient):
        if patient not in self.__patients:
            self.__patients.append(patient)
            self.save()

    def get_patients(self):
        patients_data = [patient.get_patient_info() for patient in self.__patients]
        return patients_data

    def load_info(self):
        data = FileUtils.read_from_json("patient.json")
        self.__patients = State.get_patients(data)

    def save(self):
        data = self.to_dict()
        FileUtils.save_in_json(data, "patient.json")

    def delete_patient(self, opts):
        if opts.patient_fio:
            self.delete_by_patient_fio(opts.patient_fio)
        if opts.residence_place:
            self.delete_by_residence_place(opts.residence_place)
        if opts.birthday:
            self.delete_by_birthday(opts.birthday)
        if opts.date_receipt:
            self.delete_by_date_receipt(opts.date_receipt)
        if opts.doctor_fio:
            self.delete_by_doctor_fio(opts.doctor_fio)
        if opts.conclusion:
            self.delete_by_conclusion(opts.conclusion)
        self.save()

    def delete_by_patient_fio(self, patient_fio):
        patients = []
        for patient in self.__patients:
            if patient_fio in patient.patient_fio.split():
                patients.append(patients)
        for patient in patients:
            self.__patients.remove(patient)

    def delete_by_residence_place(self, residence_place):
        patients = []
        for patient in self.__patients:
            if residence_place in patient.residence_place.split():
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def delete_by_birthday(self, birthday):
        patients = []
        for patient in self.__patients:
            if birthday in patient.birthday.split():
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def delete_by_date_receipt(self, date_receipt):
        patients = []
        for patient in self.__patients:
            if date_receipt == patient.date_receipt:
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def delete_by_doctor_fio(self, doctor_fio):
        patients = []
        for patient in self.__patients:
            if doctor_fio == patient.doctor_fio:
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def delete_by_conclusion(self, conclusion):
        patients = []
        for patient in self.__patients:
            if conclusion == patient.conclusion:
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def filter_patient(self, opts):
        self.load_info()
        if opts.patient_fio:
            self.filter_by_patient_fio(opts.patient_fio)
        if opts.residence_place:
            self.filter_by_residence_place(opts.residence_place)
        if opts.birthday:
            self.filter_by_birthday(opts.birthday)
        if opts.doctor_fio:
            self.filter_by_doctor_fio(opts.doctor_fio)
        if opts.date_receipt:
            self.filter_by_date_receipt(opts.date_receipt)

    def filter_by_patient_fio(self, patient_fio):
        patients = []
        for patient in self.__patients:
            if patient_fio not in patient.patient_fio.split():
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def filter_by_residence_place(self, residence_place):
        patients = []
        for patient in self.__patients:
            if residence_place not in patient.residence_place.split():
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def filter_by_birthday(self, birthday):
        patients = []
        for patient in self.__patients:
            if birthday not in patient.birthday.split():
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def filter_by_doctor_fio(self, doctor_fio):
        patients = []
        for patient in self.__patients:
            if not doctor_fio == patient.doctor_fio:
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def filter_by_date_receipt(self, date_receipt):
        patients = []
        for patient in self.__patients:
            if not date_receipt == patient.date_receipt:
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

    def filter_by_conclusion(self, conclusion):
        patients = []
        for patient in self.__patients:
            if not conclusion == patient.conclusion:
                patients.append(patient)
        for patient in patients:
            self.__patients.remove(patient)

class Patient:
    def __init__(self,
                 patient_fio=None,
                 residence_place=None,
                 birthday=None,
                 date_receipt=None,
                 doctor_fio=None,
                 conclusion=None):
        self.patient_fio = patient_fio
        self.residence_place = residence_place
        self.birthday = birthday
        self.date_receipt = date_receipt
        self.doctor_fio = doctor_fio
        self.conclusion = conclusion

    def to_dict(self):
        data = dict()
        data['patient_fio'] = self.patient_fio
        data['residense_place'] = self.residence_place
        data['birthday'] = self.birthday
        data['date_receipt'] = self.date_receipt
        data['doctor_fio'] = self.doctor_fio
        data['conclusion'] = self.conclusion
        return data


    def get_patient_info(self):
        patient_info = self.to_dict()
        return tuple(patient_info.values())


@dataclasses.dataclass
class PatientOptions:
    patient_fio: Optional[str]
    residence_place: Optional[str]
    birthday: Optional[str]
    date_receipt: Optional[float]
    doctor_fio: Optional[float]
    conclusion: Optional[float]


class State:
    @staticmethod
    def get_patients(data: dict):
        patients = []
        for patient in data["patient"]:
            patient_data = Patient(*patient.values())
            patients.append(patient_data)
        return patients
