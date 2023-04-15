import tkinter as tk 

from print_garden import print_garden
from serializers import load_state, write_state
from cli import field_collection, BaseGarden


garden = load_state()

window = tk.Tk()     # создаем корневой объект - окно
window.title("Gargen")     # устанавливаем заголовок окна
window.geometry("900x600")    # устанавливаем размеры окна
text_area = tk.Text(window, height=900, width=60)
text_area.place(x=0,y=50)
label = tk.Label(text="Hello METANIT.COM", background='sandy brown') # создаем текстовую метку
with open('./gargen_printed.txt', '+w') as f:
    print_garden(garden, f)

with open('./gargen_printed.txt', '+r') as f:
    line_n = 1
    for line in f:
        text_area.insert(f'{line_n}.0', f'{line}')
        line_n += 1
        


init_button = tk.Button(
    window,
    text="Initialize",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
)
init_button.place(x=600, y=100)
tk.Label(text='Initialize 3-size garden').place(x=600, y=85)

tk.Label(text='Next day').place(x=600, y=150)
nexday_button = tk.Button(
    window,
    text="Next day",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
)
nexday_button.place(x=600, y=175)

desinfect_button = tk.Button(
    window,
    text="Desinfect",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
)
tk.Label(text='Desinfect field').place(x=600, y=225)
desinfect_button.place(x=600, y=240)

Heal_button = tk.Button(
    window,
    text="Heal",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
)
tk.Label(text='Heal field').place(x=600, y=290)
Heal_button.place(x=600, y=315)

Hydrate_button = tk.Button(
    window,
    text="Hydrate",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
)
tk.Label(text='Hydrate field').place(x=600, y=365)
Hydrate_button.place(x=600, y=390)

Weeding_button = tk.Button(
    window,
    text="Hydrate",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
)
tk.Label(text='Weeding field').place(x=600, y=440)
Weeding_button.place(x=600, y=475)

Kill_button = tk.Button(
    window,
    text="Kill plant",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
)
tk.Label(text='Kill plant').place(x=600, y=525)
Kill_button.place(x=600, y=550)


        


label.pack()    # размещаем метку в окне
window.mainloop()


# def handle_click(event):
#     print("Нажата кнопка!")
 
# button = tk.Button(text="Кликни!", command = )
 
# button.bind("<Button-1>", handle_click)