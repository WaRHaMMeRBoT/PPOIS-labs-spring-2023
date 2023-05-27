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
window.title("Gargen")     
window.geometry("900x800")

text_area = tk.Text(window, height=900, width=60)
text_area.place(x=0,y=50)


init_button = tk.Button(
    window,
    text="Initialize",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
    command= lambda : (init_handler(update_garden, load_state()))
)
init_button.place(x=600, y=50)
tk.Label(text='Initialize 3-size garden').place(x=600, y=25)

tk.Label(text='Next day').place(x=600, y=100)
nexday_button = tk.Button(
    window,
    text="Next day",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
    command= lambda : (nextday_handler(update_garden, load_state()))
)
nexday_button.place(x=600, y=125)

desinfect_input = tk.Entry(window)  
desinfect_input.place(x=600, y=200)
desinfect_button = tk.Button(
    window,
    text="Desinfect",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
    command= lambda: (desinfect_handler(desinfect_input, update_garden, load_state()))
)
tk.Label(text='Desinfect field number:').place(x=600, y=175)

print(desinfect_input.get())
desinfect_button.place(x=600, y=225)

heal_input = tk.Entry(window)
heal_input.place(x=600, y=300)
Heal_button = tk.Button(
    window,
    text="Heal",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
    command= lambda: (heal_hendler(heal_input, update_garden, load_state()))
)
tk.Label(text='Heal field number:').place(x=600, y=275)
Heal_button.place(x=600, y=325)


hydrate_input = tk.Entry(window)
hydrate_input.place(x=600, y=400)
Hydrate_button = tk.Button(
    window,
    text="Hydrate",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
    command= lambda: (hydate_handler(hydrate_input, update_garden, load_state()))

)
tk.Label(text='Hydrate field').place(x=600, y=375)
Hydrate_button.place(x=600, y=425)


weeding_input = tk.Entry(window)
weeding_input.place(x=600, y=500)
Weeding_button = tk.Button(
    window,
    text="Weeding",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
    command= lambda: (weeding_hangler(weeding_input, update_garden, load_state()))

)
tk.Label(text='Weeding field and new plant name').place(x=600, y=475)
Weeding_button.place(x=600, y=525)


kill_input = tk.Entry(window)
kill_input.place(x=600, y=600)
Kill_button = tk.Button(
    window,
    text="Kill plant",
    # width=35,
    # height=5,
    bg="gray",
    fg="black",
    command= lambda: (kill_handler(kill_input, update_garden, load_state()))

)
tk.Label(text='Kill plant').place(x=600, y=575)
Kill_button.place(x=600, y=625)

