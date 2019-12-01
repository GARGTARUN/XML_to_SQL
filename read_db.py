import sqlite3

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
# connect withe the myTable database
connection = sqlite3.connect(file_path)
print("Enter Table name:",sep='')
t_name=input()

# cursor object
crsr = connection.cursor()

# execute the command to fetch all the data from the table emp
crsr.execute("SELECT * FROM "+t_name)

# store all the fetched data in the ans variable
ans = crsr.fetchall()

# loop to print all the data
for i in ans:
    print(i)
