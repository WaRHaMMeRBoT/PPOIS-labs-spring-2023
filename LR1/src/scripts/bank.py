import json
from .interfaces.interfaces import IBank


class Bank(IBank):
    def __init__(self, url):
        self.accounts = None
        self.url = url
        with open(self.url, "r") as file:
            data = json.load(file)
            self.accounts = data if data else list()
        file.close()

    def __del__(self):
        with open(self.url, "w") as file:
            json.dump(self.accounts, file, indent=4)
        file.close()

    def get_account(self, card_number, owner):
        for item in self.accounts:
            for key in item:
                if key == card_number and item[key]['owner'] == owner:
                    return item

    def update_account(self, obj):
        for item in self.accounts:
            for key in item:
                if key == obj:
                    item = obj

    def add_account(self, card_number, owner):
        for account in self.accounts:
            for key in account:
                if account[key] != card_number and account[key]['owner'] != owner:
                    continue
                else:
                    return False

        self.accounts.append(
            {
                card_number: {
                    "pin": "1234",
                    "owner": owner,
                    "balance": 0
                }
            }
        )
        return True
