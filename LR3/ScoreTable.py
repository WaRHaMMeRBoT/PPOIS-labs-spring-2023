import sqlite3
import sys
sys.path.append("C:\\Users\\kyrill\\Documents\\GitHub\\PPOIS_Spring\\Lab 3.8")
my_way = "C:\\Users\\kyrill\\Documents\\GitHub\\PPOIS_Spring\\Lab 3.8\\HighscoreTable.db"
connection = sqlite3.connect(my_way)
cursor = connection.cursor()
cursor.execute("SELECT * FROM ScoreTable ORDER BY score + 0 DESC ")
rows =(cursor.fetchall())
rows = list(map(str,rows))
formalize_rows = []
for row in rows:
    row = row.replace("(","").replace(")","").replace(","," | ").replace("'","")
    formalize_rows.append(row)
    

def find_max():
    cursor.execute("SELECT MAX (Score) FROM ScoreTable")   
    row_max = cursor.fetchall()
    for row in row_max :
        max = int(row[0])
       
    return max    
# find_max()

def insert(name,score):
    cursor.execute("INSERT INTO ScoreTable (Name,Score) Values (?,?)",(name,score))
    connection.commit()
# cursor.execute("INSERT INTO ScoreTable (Name,Score) Values ('Avel',50)")
# connection.commit()