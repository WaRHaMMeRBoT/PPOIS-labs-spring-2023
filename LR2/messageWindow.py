from tkinter import *
from tkinter import ttk


class MessageWindow:

    def __init__(self):
        super().__init__()
        self.geometry("250x200")
        self.title("Сообщение")
        self.resizable(False, False)
        self.option_add("*tearOff", FALSE)

        ok_label = ttk.Label(text="Пользователь был добавлен", font=("Algerian", 20))
        ok_label.grid(row=0, column=0, sticky="n")

        ok_button = ttk.Button(text="Хорошо", command=self.quit)
        ok_button.grid(row=1, column=0, sticky="n")

        self.mainloop()
