import sqlite3

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
# connect withe the myTable database
connection = sqlite3.connect(file_path)

for i in range(len(file_path)-1,0,-1):
    if "." ==file_path[i]:
        end=i
    if  '/' ==file_path[i]:
        st=i+1
        break
file_path=file_path[st:end]

print(file_path)

# cursor object
crsr = connection.cursor()

# execute the command to fetch all the data from the table emp
crsr.execute("SELECT * FROM "+file_path)

# store all the fetched data in the ans variable
ans = crsr.fetchall()

# loop to print all the data
for i in ans:
    print(i)
