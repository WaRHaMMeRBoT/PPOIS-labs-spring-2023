import json

data = {}

for i in range(9):
    data[str(i)] = []
    for j in range(9):
        data[str(i)].append({})

data['dima'] = []

data['dima'].append({
    'age': 'YEBAN',
    'weight': 'YEBAN',
    'height': 'YEBAN'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
