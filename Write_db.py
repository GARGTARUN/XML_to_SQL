import pandas as pd
import xml.etree.ElementTree as et
import sqlite3

# connecting to the database

connection = sqlite3.connect("myTable.db")


xtree = et.parse("emp.xml")
xroot = xtree.getroot()

df_cols = ["first_name", "last_name", "title", "division"]
rows = []

for node in xroot:
    e_name = node.find("firstname").text if node is not None else None
    e_lname = node.find("lastname").text if node is not None else None
    e_title = node.find("title").text if node is not None else None
    e_div = node.find("division").text if node is not None else None

    rows.append({"first_name": e_name, "last_name": e_lname,
                 "title": e_title, "division": e_div})

out_df = pd.DataFrame(rows, columns=df_cols)

df = pd.DataFrame(out_df)
df.to_sql("emp", connection, if_exists="replace")
connection.commit()
connection.close()
print((df.head(6)))

