import json

class Leaderboard_Record():
    def __init__(self, name : str, score):
        self.name:str = name
        self.score = score

    @staticmethod
    def read_records_from_json(file_path):
        records_to_return = []
        records = json.load(open(file_path, 'r'))
        for record in records['records']:
            lb_record = Leaderboard_Record(**record)
            records_to_return.append(lb_record)
        return records_to_return



