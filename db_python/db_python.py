import sqlite3


db_path = r"C:\Users\roman\Projekty\db_python\Test_DB.db"

conn = sqlite3.connect(db_path) # připojení na db
cursor = conn.cursor()

sql = "select * from zamestnanec where jmeno = 'Petra'"
cursor.execute(sql)
for item in cursor.fetchall():
    print(item)

sql = "insert into firma (nazev, ico, adresa) values ('Apple', '111111', 'Long Island, CA')"
cursor.execute(sql)
conn.commit()

sql = "select * from firma"
cursor.execute(sql)
data = cursor.fetchall()
print(data)

conn.close()
