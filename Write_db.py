import pandas as pd
import xml.etree.ElementTree as et
import sqlite3
import pandas as pd
import xml.etree.ElementTree as et


def parse_XML(xml_file, df_cols):
    xtree = et.parse(xml_file)
    xroot = xtree.getroot()
    rows = []

    for node in xroot:
        res = []
        res.append(node.attrib.get(df_cols[0]))
        for el in df_cols[1:]:
            if node is not None and node.find(el) is not None:
                res.append(node.find(el).text)
            else:
                res.append(None)
        rows.append({df_cols[i]: res[i]
                     for i, _ in enumerate(df_cols)})

    out_df = pd.DataFrame(rows, columns=df_cols)

    return out_df
# connecting to the database
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print("Enter Table name:",sep='')
table_name=input()
# list of all the tags
elemList=[]
xtree = et.parse(file_path)
for elem in xtree.iter():
    if elem.tag in elemList:
        break
    elemList.append(elem.tag)

elemList.pop(0)
elemList.pop(0)
elemList.insert(0,"none")
#print(elemList)
# dataframe of all the data

df= parse_XML(file_path,elemList)
df = df.drop(columns="none")
print(df.head(6))
connection = sqlite3.connect(table_name+".db")
df.to_sql(table_name, connection, if_exists="replace")
connection.commit()
connection.close()


