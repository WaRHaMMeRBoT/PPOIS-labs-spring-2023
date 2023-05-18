from random import randint
import pandas as pd


def generate() -> dict:
    names = [
        ['Иванов', 'Петров', 'Сидоров', 'Ковалев', 'Лобанов', 'Быков', 'Мартынов'],
        ['Василий', 'Федор', 'Анатолий', 'Алексей', 'Илья', 'Александр', 'Иван', 'Максим'],
        ['Васильевич', 'Федорович', 'Анатолевич', 'Алексеевич', 'Ильич', 'Александрович',
         'Иванович', 'Максимович']
    ]
    sport = ['плавание', 'футбол', 'волейбол', 'баскетбол', 'гандбол', 'теннис', 'гимнастика']
    tour = ['Жаркие игры', 'Спортивный десант', 'Время первых', 'Сила спорта', 'Чемпионат Республики']

    day = str(randint(1, 28))
    if len(day) == 1:
        day = '0' + day
    month = str(randint(1, 12))
    if len(month) == 1:
        month = '0' + month
    return {
        'tour_name': tour[randint(0, len(tour) - 1)],
        'date': f'{day}.{month}.{randint(1990, 2022)}',
        'sport': sport[randint(0, len(sport) - 1)],
        'name': f'{names[0][randint(0, len(names[0]) - 1)]} '
                f'{names[1][randint(0, len(names[1]) - 1)]} '
                f'{names[2][randint(0, len(names[2]) - 1)]}',
        'reward': randint(1, 10) * 100
    }


def generate_df():
    df = pd.DataFrame()
    for i in range(50):
        df = df.append(generate(), ignore_index=True)
    df['winner_reward'] = df['reward'] * 0.6
    print(df)
    return df

