from src.card import Card
from src.account import Account
from src.repository import Repository
from src.atm import ATM
from src.bank import Bank

import json


def read_data() -> tuple:
    try:
        with open('data/data.json') as f:
            data = json.load(f)

        accounts = [Account(x['login'], x['password'], x['balance'], x['id']) for x in data['accounts']]

        cards = []
        for x in data['cards']:
            for y in accounts:
                if y.id == x['account_id']:
                    cards.append(Card(x['pin'], y, x['number'], x['cvv'], x['date']))
                    break
        repository = Repository(data['repo'])
        Card.id_tf, Account.id_tf = data['card_id_tf'], data['account_id_tf']

        atm = ATM(repository=repository, cards=cards, access=data['atm-state']['access'])
        if data['atm-state']['inserted']:
            for i in range(len(cards)):
                if cards[i].number == data['atm-state']['card.py-number']:
                    atm = ATM(repository=repository, cards=cards, card=cards[i], access=data['atm-state']['access'])

        bank = Bank(accounts, cards)
        if data['bank-state']['logged']:
            for i in range(len(accounts)):
                if accounts[i].id == data['bank-state']['account-id']:
                    bank = Bank(accounts, cards, accounts[i])

    except (FileNotFoundError, KeyError, json.decoder.JSONDecodeError):
        accounts, cards, repository = [], [], Repository(2500)
        atm = ATM(repository, cards)
        bank = Bank(accounts, cards)

    return accounts, cards, repository, atm, bank


def write_data(accounts: list, cards: list, repository: Repository, atm: ATM, bank: Bank):
    dct = {
        'accounts': [x.as_dict() for x in accounts],
        'cards': [x.as_dict() for x in cards],
        'repo': repository.money,

        'card_id_tf': Card.id_tf,
        'account_id_tf': Account.id_tf,

        'atm-state': atm.as_dict(),
        'bank-state': bank.as_dict()
    }

    with open('data/data.json', 'w') as outfile:
        json.dump(dct, outfile, indent=4)