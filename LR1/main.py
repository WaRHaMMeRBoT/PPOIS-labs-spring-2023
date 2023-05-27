import random
import pickle
from garden import Garden
from garden import Actions

try:
    with open('save.pickle', 'rb') as f:
        garden = pickle.load(f)
except FileNotFoundError:
    garden = Garden(8)
    
a = Actions()
while 1:
    garden.Show_field()
    inp = input()
    if inp == 'end': break
    else:
        garden.Next_move()
        a.actions(garden, inp)

with open('save.pickle', 'wb') as f:
    pickle.dump(garden, f)
    