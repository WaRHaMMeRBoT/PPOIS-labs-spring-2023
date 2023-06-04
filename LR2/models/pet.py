class Pet:
    name = ''
    birth_date = ''
    date_of_last_admission = ''
    veterinarians_name = ''
    diagnosis = ''

    def __str__(self) -> str:
        return "Name: "+self.name+", Birth date: "+self.birth_date+", Veterinarians name: "+self.veterinarians_name+\
                ", Date of last admission: "+self.date_of_last_admission+", Diagnosis: "+self.diagnosis
    