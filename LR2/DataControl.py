import json
import datetime
from Tournament import *

path = 'Data.json'


def write(tournaments_list):
    tournaments = {'tournaments': []}
    tournament = {'tournament_name': [], 'date': [], 'sport_name': [], 'winner_name': [], 'prize_money': []}
    for _tournament in tournaments_list:
        tournament['tournament_name'] = _tournament.tournament_name
        tournament['date'] = _tournament.date
        tournament['sport_name'] = _tournament.sport_name
        tournament['winner_name'] = _tournament.winner_name
        tournament['prize_money'] = _tournament.prize_money
        tournaments['tournaments'].append(tournament.copy())
    with open(path, "w", encoding="utf-8") as file:
        json.dump(tournaments, file, indent=1, sort_keys=False)


def read(tournaments_list):
    with open(path, "r", encoding="utf-8") as file:
        data_base = json.load(file)
    for tournament in data_base['tournaments']:
        _tournament = Tournament()
        _tournament.tournament_name = tournament['tournament_name']
        _tournament.date = tournament['date']
        _tournament.sport_name = tournament['sport_name']
        _tournament.winner_name = tournament['winner_name']
        _tournament.prize_money = tournament['prize_money']
        _tournament.set_winner_money()
        tournaments_list.append(_tournament)
