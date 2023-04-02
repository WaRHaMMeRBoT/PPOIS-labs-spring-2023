import sqlite3
my_path = "C:\\Users\\kiril\\OneDrive\\Документы\\GitHub\\PPOIS_Spring\\Lab 2.2\\PPOIS2lab.db"
con = sqlite3.connect(my_path)
cur = con.cursor()
table = """CREATE TABLE Students4(
    ID INTEGER NOT NULL PRIMARY KEY UNIQUE,
    FullName CHAR, 
    GroupNumber INT(5), 
    Sem1 INT,
    Sem2 INT,
    Sem3 INT,
    Sem4 INT,
    Sem5 INT,
    Sem6 INT,
    Sem7 INT,
    Sem8 INT,
    Sem9 INT,
    Sem10 INT,
    Sem_total INT GENERATED ALWAYS AS ( Sem1 + Sem2 + Sem3 + Sem4 + Sem5 + Sem6 + Sem7 + Sem8 + Sem9 + Sem10)
    );"""

def add_string_db(cons,curs):
        sqlite_insert_query = """INSERT INTO Students4
                                (FullName , GroupNumber, Sem1 ,Sem2 ,Sem3 ,Sem4 ,Sem5 ,Sem6 ,Sem7 ,Sem8 ,Sem9 ,Sem10 )
                                VALUES 
                                ('Stas',121702, 101 , 5 , 21 , 33 , 45 , 5 , 84 , 21 , 55 , 9)"""
        count = curs.execute(sqlite_insert_query)
        cons.commit()

def show_table(cons,curs):
    curs = cons.cursor()
    curs.execute("SELECT * FROM Students4")
    rows = curs.fetchall()
    for row in rows:
        print(row)

def find(cons,curs,id):
    curs = cons.cursor()
    if id == 1:
        print("Find by group")
        print("Enter Group number:")
        val1 = int(input())
        curs.execute("SELECT * FROM Students4 WHERE GroupNumber=?",(val1,))
    elif id == 2:
        print("Find by FullName")
        print("Enter FullName:")
        val2 = str(input())
        curs.execute("SELECT * FROM Students4 WHERE FullName=?",(val2,))
    rows = curs.fetchall()
    for row in rows:
        print(row)

def find_by_amount(cons,curs,id):
    curs = cons.cursor()
    if id == 1:
        print("Find by group")
        print("Enter Group number:")
        val1 = int(input())
        print("Enter Min amount:")
        min_param = int(input())
        print("Enter Max amount:")
        max_param = int(input())
        curs.execute("SELECT * FROM Students4 WHERE GroupNumber=?1 AND Sem_total BETWEEN ?2 AND ?3", (val1,min_param,max_param,))
    elif id == 2:
        print("Find by FullName")
        print("Enter FullName:")
        val2 = str(input())
        print("Enter Min amount:")
        min_param = int(input())
        print("Enter Max amount:")
        max_param = int(input())
        curs.execute("SELECT * FROM Students4 WHERE FullName=?1 AND Sem_total BETWEEN ?2 AND ?3", (val2,min_param,max_param,))
    rows = curs.fetchall()
    for row in rows:
        print(row) 






# cur.execute(table) 
# add_string_db(con,cur)
# print(show_table(con,cur))          
print(find(con,cur,2))


# print(find_by_amount(con,cur,2))
# print(show_table(con,cur))
con.close()