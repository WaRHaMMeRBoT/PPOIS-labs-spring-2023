import tkinter as tk 
from Controllers.print_garden import print_garden
from Controllers.controller import *
from Models.serializers import load_state, write_state

garden = load_state()
def update_garden(garden, arg=None):
    text_area.delete('1.0', tk.END)
    if arg: arg.delete(0, tk.END)
    with open('./gargen_printed.txt', '+w') as f:
        print_garden(garden, f)
    with open('./gargen_printed.txt', '+r') as f:
        line_n = 1
        for line in f:
            text_area.insert(f'{line_n}.0', f'{line}')
            line_n += 1
    write_state(garden)
    garden = load_state()

window = tk.Tk() 
window.geometry("700x600")

text_area = tk.Text(window, height=35, width=52)
text_area.place(x=20,y=20)


init_button = tk.Button(
    window,
    text="Initialize",
    width=11,
    height=2,
    bg="light green",
    fg="black",
    command= lambda : (init_handler(update_garden, load_state()))
)
init_button.place(x=470, y=50)

nexday_button = tk.Button(
    window,
    text="Next day",
    width=11,
    height=2,
    bg="light blue",
    fg="black",
    command= lambda : (nextday_handler(update_garden, load_state()))
)
nexday_button.place(x=590, y=50)

desinfect_input = tk.Entry(window,width=14)  
desinfect_input.place(x=470, y=195)
desinfect_button = tk.Button(
    window,
    text="Desinfect",
    width=11,
    height=2,
    bg="pink",
    fg="black",
    command= lambda: (desinfect_handler(desinfect_input, update_garden, load_state()))
)
tk.Label(text='Write a number of a field you want to:').place(x=470, y=150)
print(desinfect_input.get())
desinfect_button.place(x=470, y=225)

heal_input = tk.Entry(window,width=14) 
heal_input.place(x=590, y=195)
Heal_button = tk.Button(
    window,
    text="Fertilize",
    width=11,
    height=2,
    bg="white",
    fg="black",
    command= lambda: (heal_hendler(heal_input, update_garden, load_state()))
)
Heal_button.place(x=590, y=225)


hydrate_input = tk.Entry(window,width=14) 
hydrate_input.place(x=470, y=320)
Hydrate_button = tk.Button(
    window,
    text="Hydrate",
    width=11,
    height=2,
    bg="blue",
    fg="black",
    command= lambda: (hydate_handler(hydrate_input, update_garden, load_state()))

)
Hydrate_button.place(x=470, y=350)

weeding_input = tk.Entry(window,width=14) 
weeding_input.place(x=590, y=320)
Weeding_button = tk.Button(
    window,
    text="Weeding",
    width=11,
    height=2,
    bg="brown",
    fg="black",
    command= lambda: (weeding_hangler(weeding_input, update_garden, load_state()))

)
Weeding_button.place(x=590, y=350)

kill_input = tk.Entry(window,width=14)
kill_input.place(x=525, y=440)
Kill_button = tk.Button(
    window,
    text="Kill",
    width=11,
    height=2,
    bg="black",
    fg="white",
    command= lambda: (kill_handler(kill_input, update_garden, load_state()))
)
Kill_button.place(x=525, y=470)

