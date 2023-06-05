class Person:
    
    def __init__(self):
        self.full_name = ""
        self.birth_date = ""
        self.club = ""
        self.home_city = ""
        self.compound = ""
        self.position = ""
        
    def __del__(self):
        print("Пользователь был удалён")    
