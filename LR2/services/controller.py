
from .patients import *
from view.view import *



class Controller:
    def __init__(self, repository: Patients):
        self.repository = repository
        self.view = View(self)

    def get_root_view(self):
        return self.view.root

    def close_dialog(self):
        self.view.close_dialog()

    def add_patient(self):
        data = self.view.dialog.content_cls.ids

        patient = Patient(data.patient_fio.text,
                          data.residence_place.text,
                          data.birthday.text,
                          data.date_receipt.text,
                          data.doctor_fio.text,
                          data.conclusion.text)

        self.repository.add_to_patients_list(patient)

        self.view.close_dialog()
        self.view.update_table()

    def delete_patient(self):
        data = self.view.dialog.content_cls.ids
        opts = PatientOptions(patient_fio=data.patient_fio.text,
                              residence_place=data.residence_place.text,
                              birthday=data.birthday.text,
                              date_receipt=data.date_receipt.text,
                              doctor_fio=data.doctor_fio.text,
                              conclusion=data.conclusion.text
                              )

        self.repository.delete_patient(opts)

        self.view.close_dialog()
        self.view.update_table()

    def filter_patient(self):
        data = self.view.dialog.content_cls.ids
        opts = PatientOptions(patient_fio=data.patient_fio.text,
                              residence_place=data.residence_place.text,
                              birthday=data.birthday.text,
                              date_receipt=data.date_receipt.text,
                              doctor_fio=data.doctor_fio.text,
                              conclusion=data.conclusion.text
                              )
        self.repository.filter_patient(opts)

        self.view.close_dialog()
        self.view.update_table()
        self.repository.load_info()

    def get_patient(self):
        return self.repository.get_patients()

    def open_add_dialog(self):
        self.view.open_add_patient_dialog()

    def open_delete_dialog(self):
        self.view.open_delete_patient_dialog()

    def open_filter_dialog(self):
        self.view.open_filter_patient_dialog()
