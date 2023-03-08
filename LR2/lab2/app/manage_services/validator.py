import re

class Validator:
    def __init__(self, data) -> None:
        self.data = data
    
    def validate(self):
        valid_list = [self.valid_name(), self.valid_course(), self.valid_group(),
                      self.valid_all_work(), self.valid_do_work(), self.valid_lang()]
        return all(valid_list)
        
    def valid_name(self):
        pattern = re.compile("^[a-zA-Zа-яА-ЯёЁ]+$")
        if len(self.data['name'].split()) == 3:
            for i in self.data['name'].split():
                if not (pattern.search(i) is not None):
                    return False
        else:
            return False
        return True
    
    def valid_course(self):
        if not self.data['course'].isdigit():
            return False
        return True
    
    def valid_group(self):
        if not self.data['group'].isdigit():
            return False
        return True
    
    def valid_all_work(self):
        if not self.data['all_work'].isdigit():
            return False
        return True
    
    def valid_do_work(self):
        if not self.data['do_work'].isdigit():
            return False
        return True
    
    def valid_lang(self):
        return len(self.data['lang']) > 0