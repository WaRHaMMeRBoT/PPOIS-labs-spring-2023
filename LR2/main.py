from dataLoader import *
from tkinter import *
from functools import partial
from tkinter.messagebox import showinfo, showerror
import os
from os import path

file = []


def finish():
    for i in detachedItems:
        StudentBase.reattach(i, "", 0)
    write(StudentBase, file[0])
    print("ReWritten")


def close():
    finish()
    root.destroy()


def start(StudentBase, file):
    students = read(file)
    for person in students:
        StudentBase.insert("", END, values=person)
    print("Start")


def sort(col, reverse):
    l = [(StudentBase.set(k, col), k) for k in StudentBase.get_children("")]
    l.sort(reverse=reverse)
    for index, (_, k) in enumerate(l):
        StudentBase.move(k, "", index)
    StudentBase.heading(col, command=lambda: sort(col, not reverse))


def deleting_student(FIO, window, Group, hours_from, hours_to):
    number = len(StudentBase.get_children())
    if (
        FIO.get() != ""
        and Group.get() == "Все группы"
        and hours_from.get() == "0"
        and hours_to.get() == "0"
    ):
        for item in StudentBase.get_children():
            if StudentBase.set(item, 0) == FIO.get():
                StudentBase.detach(item)
    if (
        FIO.get() == ""
        and Group.get() != "Все группы"
        and hours_from.get() == "0"
        and hours_to.get() == "0"
    ):
        for item in StudentBase.get_children():
            if StudentBase.set(item, 1) == Group.get():
                StudentBase.detach(item)
    if FIO.get() == "" and Group.get() != "Все группы":
        if hours_from.get() <= hours_to.get():
            for item in StudentBase.get_children():
                if StudentBase.set(item, 1) == Group.get() and (
                    hours_from.get() <= StudentBase.set(item, 12)
                    and StudentBase.set(item, 12) <= hours_to.get()
                ):
                    StudentBase.detach(item)
    elif FIO.get() != "" and Group.get() == "Все группы":
        if hours_from.get() <= hours_to.get():
            for item in StudentBase.get_children():
                if StudentBase.set(item, 0) == FIO.get() and (
                    hours_from.get() <= StudentBase.set(item, 12)
                    and StudentBase.set(item, 12) <= hours_to.get()
                ):
                    StudentBase.detach(item)
    window.destroy()
    showinfo(
        "Удаление студентов",
        f"Студентов удалено: {number - len(StudentBase.get_children())}",
    )


def finding_student(FIO, window, Group, hours_from, hours_to):
    if (
        FIO.get() == ""
        and Group.get() == "Все группы"
        and hours_from.get() == "0"
        and hours_to.get() == "0"
    ):
        for i in detachedItems:
            StudentBase.reattach(i, "", 0)
    for i in detachedItems:
        StudentBase.reattach(i, "", 0)
    if (
        FIO.get() != ""
        and Group.get() == "Все группы"
        and hours_from.get() == "0"
        and hours_to.get() == "0"
    ):
        for item in StudentBase.get_children():
            if StudentBase.set(item, 0) != FIO.get():
                StudentBase.detach(item)
                detachedItems.append(item)
    if (
        FIO.get() == ""
        and Group.get() != "Все группы"
        and hours_from.get() == "0"
        and hours_to.get() == "0"
    ):
        for item in StudentBase.get_children():
            if StudentBase.set(item, 1) != Group.get():
                StudentBase.detach(item)
                detachedItems.append(item)
    if FIO.get() == "" and Group.get() != "Все группы":
        if hours_from.get() < hours_to.get():
            for item in StudentBase.get_children():
                if StudentBase.set(item, 1) == Group.get() and not (
                    hours_from.get() <= StudentBase.set(item, 12)
                    and StudentBase.set(item, 12) <= hours_to.get()
                ):
                    StudentBase.detach(item)
                    detachedItems.append(item)
    elif FIO.get() != "" and Group.get() == "Все группы":
        if hours_from.get() < hours_to.get():
            for item in StudentBase.get_children():
                if StudentBase.set(item, 0) == FIO.get() and not (
                    hours_from.get() <= StudentBase.set(item, 12)
                    and StudentBase.set(item, 12) <= hours_to.get()
                ):
                    StudentBase.detach(item)
                    detachedItems.append(item)
    window.destroy()
    if len(StudentBase.get_children()) == 0:
        showerror("Ошибка", "Ничего не найдено")
        for i in detachedItems:
            StudentBase.reattach(i, "", 0)
        return
    showinfo(
        "Поиск студентов",
        f"Студентов найдено: {len(StudentBase.get_children())}",
    )


def adding_student(FIO, window, Group, hours):
    number = hours.get() // 4
    if FIO.get() == "" or Group.get() == "Все группы":
        window.destroy()
        showerror(
            title="Добавление студента", message="Фамилия и/или номер группы неверны"
        )
        return
    student_info = []
    student_info.append(FIO.get())
    student_info.append(Group.get())
    if hours.get() < 4:
        student_info.append(hours.get())
        for i in range(0, 9):
            student_info.append(0)
        student_info.append(hours.get())
    else:
        for i in range(0, number):
            student_info.append(4)
        student_info.append(hours.get() % 4)
        for i in range(0, 9 - number):
            student_info.append(0)
    student_info.append(hours.get())
    student = tuple(student_info)
    StudentBase.insert("", END, values=student)
    window.destroy()
    showinfo("Добавление студента", f"Студент добавлен\n{FIO.get()}\n{Group.get()}")


def Action(Name, window, FIO, Group, hours_from, hours_to):
    if Name == "Удалить":
        deleting_student(FIO, window, Group, hours_from, hours_to)
    elif Name == "Добавить":
        adding_student(FIO, window, Group, hours_from)
    elif Name == "Найти":
        finding_student(FIO, window, Group, hours_from, hours_to)


def pack_fio_element(frame, Name, FIO):
    label = ttk.Label(frame, text=Name)
    entry = ttk.Entry(frame, textvariable=FIO)
    label.pack(anchor=CENTER)
    entry.pack(anchor=CENTER)
    frame.pack(anchor=NW, fill=X, padx=5, pady=5)


def pack_group_element(frame, Name, Group):
    label = ttk.Label(frame, text=Name)
    options = ["Все группы", "Все группы", "121703", "121702", "121701"]
    OptionMenu = ttk.OptionMenu(frame, Group, *options)
    label.pack(anchor=CENTER)
    OptionMenu.pack(anchor=CENTER)
    frame.pack(anchor=NW, fill=X, padx=5, pady=5)


def pack_hours_element(frame, hours_from, hours_to):
    mainLabel = ttk.Label(frame, text="Часы опт")
    label_1 = ttk.Label(frame, text="От")
    entry_1 = ttk.Entry(frame, textvariable=hours_from)
    label_2 = ttk.Label(frame, text="До")
    entry_2 = ttk.Entry(frame, textvariable=hours_to)
    mainLabel.pack(anchor=CENTER)
    label_1.pack(anchor=CENTER)
    entry_1.pack(anchor=CENTER)
    label_2.pack(anchor=CENTER)
    entry_2.pack(anchor=CENTER)
    frame.pack(anchor=NW, fill=X, padx=5, pady=5)


def pack_button(frame, Name, window, FIO, Group, hours_from, hours_to):
    btn = ttk.Button(
        frame,
        text=Name,
        command=partial(Action, Name, window, FIO, Group, hours_from, hours_to),
    )
    btn.pack(anchor=CENTER)
    frame.pack(anchor=NW, fill=X, padx=5, pady=5)


def Window(titleName, Name):
    window = Toplevel()
    window.resizable(False, False)
    window.title(titleName)
    window.geometry("400x500+700+200")
    FIO = StringVar(value="")
    Group = StringVar(value="")
    hours_from = StringVar(value=0)
    hours_to = StringVar(value=0)
    frame_1 = ttk.Frame(window, borderwidth=0, relief=RIDGE, padding=[8, 10])
    frame_2 = ttk.Frame(window, borderwidth=0, relief=SOLID, padding=[8, 10])
    frame_3 = ttk.Frame(window, borderwidth=0, relief=SOLID, padding=[8, 10])
    frame_4 = ttk.Frame(window, borderwidth=0, relief=SOLID, padding=[8, 10])
    pack_fio_element(frame_1, "Введите ФИО", FIO)
    pack_group_element(frame_2, "Выберите номер группы", Group)
    pack_hours_element(frame_3, hours_from, hours_to)
    pack_button(frame_4, Name, window, FIO, Group, hours_from, hours_to)
    window.grab_set()


def SearchWindow():
    Window("Поиск студентов", "Найти")


def DeleteWindow():
    Window("Удаление студентов", "Удалить")


def pack_add_hours_student(frame, hours):
    label_1 = ttk.Label(frame, text="Введите общее количество часов опт")
    entry_1 = ttk.Entry(frame, textvariable=hours)
    label_1.pack(anchor=CENTER)
    entry_1.pack(anchor=CENTER)
    frame.pack(anchor=NW, fill=BOTH, padx=5, pady=5)


def AddWindow():
    window = Toplevel()
    window.resizable(False, False)
    window.title("Добавление студента")
    window.geometry("400x500+700+200")
    hours = IntVar(value=0)
    FIO = StringVar(value="")
    Group = StringVar(value="")
    frame_1 = ttk.Frame(window, borderwidth=0, relief=RIDGE, padding=[8, 10])
    frame_2 = ttk.Frame(window, borderwidth=0, relief=RIDGE, padding=[8, 10])
    frame_3 = ttk.Frame(window, borderwidth=0, relief=RIDGE, padding=[8, 10])
    frame_4 = ttk.Frame(window, borderwidth=0, relief=RIDGE, padding=[8, 10])
    pack_fio_element(frame_1, "Введите ФИО", FIO)
    pack_group_element(frame_2, "Выберите номер группы", Group)
    pack_add_hours_student(frame_3, hours)
    pack_button(frame_4, "Добавить", window, FIO, Group, hours, 0)
    window.grab_set()


def autorization(filename, root, file):
    if os.path.exists(filename.get()):
        file.append(filename.get())
        root.destroy()
    else:
        showerror("Ошибка", f"Файла с именем: {filename.get()} не существует")


root = Tk()
style = ttk.Style()
style.theme_use("clam")
root.title("Вход")
root.geometry("400x66")
filename = StringVar(value="")
frame = ttk.Frame(root, borderwidth=0, relief=GROOVE, padding=[8, 0])
label_1 = ttk.Label(frame, text="Введите название файла")
entry = ttk.Entry(frame, textvariable=filename)
button = ttk.Button(
    frame, text="Ввод", command=partial(autorization, filename, root, file)
)
label_1.pack(anchor=CENTER)
entry.pack(anchor=CENTER)
button.pack(anchor=SE, fill=X)
frame.pack(fill=BOTH)
root.mainloop()

root = Tk()
style = ttk.Style()
style.theme_use("clam")
root.title("База студентов")
root.geometry("1018x500")
root.resizable(False, False)

columns = (
    "ФИО",
    "Группа",
    "1 сем.",
    "2 сем.",
    "3 сем.",
    "4 сем.",
    "5 сем.",
    "6 сем.",
    "7 сем.",
    "8 сем.",
    "9 сем.",
    "10 сем.",
    "Общее кол-во",
)
StudentBase = ttk.Treeview(columns=columns, show="headings")
detachedItems = []

StudentBase.heading("ФИО", text="ФИО", command=lambda: sort(0, False))
StudentBase.heading("Группа", text="Группа", command=lambda: sort(1, False))
StudentBase.heading("1 сем.", text="1 сем.", command=lambda: sort(2, False))
StudentBase.heading("2 сем.", text="2 сем.", command=lambda: sort(3, False))
StudentBase.heading("3 сем.", text="3 сем.", command=lambda: sort(4, False))
StudentBase.heading("4 сем.", text="4 сем.", command=lambda: sort(5, False))
StudentBase.heading("5 сем.", text="5 сем.", command=lambda: sort(6, False))
StudentBase.heading("6 сем.", text="6 сем.", command=lambda: sort(7, False))
StudentBase.heading("7 сем.", text="7 сем.", command=lambda: sort(8, False))
StudentBase.heading("8 сем.", text="8 сем.", command=lambda: sort(9, False))
StudentBase.heading("9 сем.", text="9 сем.", command=lambda: sort(10, False))
StudentBase.heading("10 сем.", text="10 сем.", command=lambda: sort(11, False))
StudentBase.heading("Общее кол-во", text="Общее", command=lambda: sort(12, False))

StudentBase.column("#1", stretch=FALSE, width=200, anchor=CENTER)
StudentBase.column("#2", stretch=FALSE, width=120, anchor=CENTER)
StudentBase.column("#3", anchor=CENTER)
StudentBase.column("#4", anchor=CENTER)
StudentBase.column("#5", anchor=CENTER)
StudentBase.column("#6", anchor=CENTER)
StudentBase.column("#7", anchor=CENTER)
StudentBase.column("#8", anchor=CENTER)
StudentBase.column("#9", anchor=CENTER)
StudentBase.column("#10", anchor=CENTER)
StudentBase.column("#11", anchor=CENTER)
StudentBase.column("#12", anchor=CENTER)
StudentBase.column("#13", anchor=CENTER)
frame = ttk.Frame(borderwidth=0)

btnSearch = ttk.Button(frame, text="Search", padding=(133, 20), command=SearchWindow)
btnDelete = ttk.Button(frame, text="Delete", padding=(133, 20), command=DeleteWindow)
btnAdd = ttk.Button(frame, text="Add", padding=(133, 20), command=AddWindow)
root.grid_rowconfigure(1)
root.grid_columnconfigure(3)
btnSearch.grid(row=0, column=0)
btnDelete.grid(row=0, column=1)
btnAdd.grid(row=0, column=2)


frame.pack(fill=X)
StudentBase.pack(fill="both", expand=1)

start(StudentBase, file[0])
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
