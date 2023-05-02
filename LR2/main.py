from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Student:
    def __init__(self, fullname, group, *semesters):
        self.fullname = fullname
        self.group = group
        self.semesters = list(semesters)


class Model:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, index):
        del self.students[index]

    def search_student(self, key, value):
        results = []
        for i, student in enumerate(self.students):
            if key == 'fullname' and value in student.fullname:
                results.append(i)
            elif key == 'group' and value == student.group:
                results.append(i)
            elif key == 'public_works' and value in student.semesters:
                results.append(i)
        return results

class View:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Database")
        self.model = Model()

        form_frame = Frame(self.master)
        form_frame.pack(padx=10, pady=10)

        fullname_label = Label(form_frame, text="Full Name:")
        fullname_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        self.fullname_entry = Entry(form_frame)
        self.fullname_entry.grid(row=0, column=1, padx=5, pady=5)

        group_label = Label(form_frame, text="Student Group:")
        group_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        self.group_entry = Entry(form_frame)
        self.group_entry.grid(row=1, column=1, padx=5, pady=5)

        semester_label = Label(form_frame, text="Semesters (comma-separated):")
        semester_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        self.semester_entry = Entry(form_frame)
        self.semester_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = Button(form_frame, text="Add", command=self.add_student)
        add_button.grid(row=3, column=1, padx=5, pady=5, sticky=E)

        delete_button = Button(form_frame, text="Delete", command=self.delete_student)
        delete_button.grid(row=4, column=1, padx=5, pady=5, sticky=E)

        search_button = Button(form_frame, text="Search", command=self.search_student)
        search_button.grid(row=5, column=1, padx=5, pady=5, sticky=E)

        list_frame = Frame(self.master)
        list_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

        scrollbar = Scrollbar(list_frame, orient=VERTICAL)
        self.listbox = Listbox(list_frame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.show_students)

        table_columns = ["Full Name", "Student Group", "Semester 1", "Semester 2", "Semester 3", "Semester 4",
                         "Semester 5", "Semester 6", "Semester 7", "Semester 8", "Semester 9", "Semester 10"]
        self.table = ttk.Treeview(list_frame, columns=table_columns, show="headings")
        for column in table_columns:
            self.table.heading(column, text=column)
        self.table.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.show_students()

    def show_students(self, event=None):
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        fullname = self.listbox.get(index)

        student = None
        for s in self.model.students:
            if s.fullname == fullname:
                student = s
                break
        self.table.delete(*self.table.get_children())

        row = [student.fullname, student.group]
        row.extend(student.semesters)
        self.table.insert("", "end", values=row)

    def add_student(self):
        fullname = self.fullname_entry.get()
        group = self.group_entry.get()
        semesters = self.semester_entry.get().split(",")

        if not fullname or not group:
            messagebox.showwarning("Error", "Full Name and Student Group are required fields.")
            return

        student = Student(fullname, group, *semesters)
        self.model.add_student(student)
        self.listbox.insert(END, fullname)
        self.clear_entries()

    def delete_student(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Error", "Please select a student to delete.")
            return

        index = selection[0]
        self.model.delete_student(index)
        self.listbox.delete(index)

    def search_student(self):
        key = ''
        value = ''
        search_options = [('Last Name', 'fullname'), ('Student Group', 'group'), ('Public Works', 'public_works')]

        def select_option():
            nonlocal key
            nonlocal value
            key = search_options[var.get()][1]
            value = value_entry.get()
            dialog.destroy()

        dialog = Toplevel(self.master)
        dialog.title("Search Student")

        var = IntVar()
        var.set(0)
        for i, (option, _) in enumerate(search_options):
            Radiobutton(dialog, text=option, variable=var, value=i).grid(row=i, column=0, padx=5, pady=5, sticky=W)

        value_label = Label(dialog, text="Search Value:")
        value_label.grid(row=len(search_options), column=0, padx=5, pady=5, sticky=W)

        value_entry = Entry(dialog)
        value_entry.grid(row=len(search_options), column=1, padx=5, pady=5)

        search_button = Button(dialog, text="Search", command=select_option)
        search_button.grid(row=len(search_options) + 1, column=1, padx=5, pady=5, sticky=E)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

        if key and value:
            results = self.model.search_student(key, value)
            if results:
                self.listbox.selection_clear(0, END)
                for index in results:
                    self.listbox.selection_set(index)
            else:
                messagebox.showinfo("Search Results", "No students found.")

    def clear_entries(self):
        self.fullname_entry.delete(0, END)
        self.group_entry.delete(0, END)
        self.semester_entry.delete(0, END)

root = Tk()
app = View(root)
root.mainloop()