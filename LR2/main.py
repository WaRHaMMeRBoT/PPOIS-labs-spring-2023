from tkinter import *
from tkinter import ttk

root = Tk()
root.title("laboratory task 2")
root.geometry("300x250")

# определяем данные для отображения
people = [("Tom", 38, 0, 1, 10, 11), ("David", 100, 10, 12, 0, 22), ("Alfred", 69, 10, 0, 10, 20)]

# определяем столбцы
columns = ("name", "group", "ill", "other_reason", "Without_reason", "title")

tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)

# определяем заголовки
tree.heading("name", text="Имя")
tree.heading("group", text="Группа")
tree.heading("ill", text="По болезни")
tree.heading("other_reason", text="Другие причины")
tree.heading("Without_reason", text="Без причин")
tree.heading("title", text="Итого")

# добавляем данные
for person in people:
    tree.insert("", END, values=person)
def update():
    root = Tk()
    root.title("laboratory task 2")
    root.geometry("300x250")

    columns = ("name", "group", "ill", "other_reason", "Without_reason", "title")

    tree = ttk.Treeview(columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1)

    # определяем заголовки
    tree.heading("name", text="Имя")
    tree.heading("group", text="Группа")
    tree.heading("ill", text="По болезни")
    tree.heading("other_reason", text="Другие причины")
    tree.heading("Without_reason", text="Без причин")
    tree.heading("title", text="Итого")

    # добавляем данные
    for person in people:
        tree.insert("", END, values=person)

    btn1 = ttk.Button(text="Удаление", command=delete)
    btn1.pack(side=RIGHT, padx=5, pady=5)

    btn2 = ttk.Button(text="Поиск")
    btn2.pack(side=RIGHT)

def delete():
    global people
    people.pop[1]
    root.destroy()
    update()

btn1 = ttk.Button(text="Удаление", command=delete)
btn1.pack(side=RIGHT, padx=5, pady=5)

btn2 = ttk.Button(text="Поиск")
btn2.pack(side=RIGHT)

root.mainloop()
