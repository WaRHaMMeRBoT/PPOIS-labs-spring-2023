from Model import XmlRecordRepository
from Model import Record
class Controller:
    def __init__(self,path):
        self.model=XmlRecordRepository(path)

    def change_model(self,path):
        self.model=XmlRecordRepository(path)

    def make_record(self,name,rank,sport,position,squad,titles):
        new_rec = Record(name,rank,sport,position,squad,titles)
        self.model.add_record(new_rec)

    def get_records(self):
        return self.model.get_all()

    def get_record_list(self):
        record_list=[]
        for record in self.model.get_all():
            record_list.append(record.to_list())
        return record_list    

    def get_ranks(self) -> list[str]:
        result = self.model.storage
        result = map(lambda x: x.rank, result)
        return set(result)

    def get_sports(self) -> set[str]:
        result = self.model.storage
        result = map(lambda x: x.sport, result)
        return set(result)
    
    def get_title_values(self) -> set[int]:
        result= self.model.storage
        result=map(lambda x: len(x.titles), result)
        return set(result)

    def filter_sports(self,filter_sport:str,filtered_records:list = None):
        result = []
        if not filtered_records:
            for record in self.model.storage:
                if record.sport == filter_sport:
                    result.append(record)
        else: 
            for record in filtered_records:
                if record.sport == filter_sport:
                    result.append(record)
        return result
    
    def filter_rank(self,filter_rank:str,filtered_records:list = None):
        result = []
        if not filtered_records:
            for record in self.model.storage:
                if record.rank == filter_rank:
                    result.append(record)
        else: 
            for record in filtered_records:
                if record.rank == filter_rank:
                    result.append(record)
        return result

    def filter_titles_values(self,filter_value,filtered_records:list = None):
        result= []
        if not filtered_records:
            for record in self.model.storage:
                if len(record.titles) == int(filter_value):
                    result.append(record)
        else: 
            for record in filtered_records:
                if len(record.titles) == int(filter_value):
                    result.append(record)
        return result

    def search_by_name(self,search_name,filtered_records:list = None):
        result = []
        if not filtered_records:
            for record in self.model.storage:
                if search_name in record.fullName:
                    result.append(record)
        else:
            for record in filtered_records:
                if search_name in record.fullName:
                    result.append(record)
        return result

    def convert_records_to_list(self,records) -> list[str]:
        record_list=[]
        for record in records:
            record_list.append(record.to_list())
        return record_list   

    def remove_elm(self,key:str):
        self.model.remove_record(key)
    
    def save(self):
        self.model.save_records()
    

