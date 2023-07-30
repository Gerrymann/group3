import sqlite3

conn, cursor = None, None

def connect_to_db(db_path):
    global conn
    global cursor
    conn = sqlite3.connect(db_path)  # připojení na db
    cursor = conn.cursor()


def select(table: str, attrs: list) -> list:
    text_attrs = ','.join(attrs)
    sql = f"select {text_attrs.strip(',')} from {table}"
    cursor.execute(sql)
    return cursor.fetchall()

def insert(table, **kwargs):
    columns = ','.join(kwargs)
    values = (f"'{str(x)}'" for x in kwargs.values())
    values = ','.join(values)
    sql = f"insert into {table} ({columns}) values ({values})"
    cursor.execute(sql)
    conn.commit()



# data = select('zamestnanec', ['id', 'jmeno', 'prijmeni'])
# print(data)
# data = select('firma', ['*'])
# print(data)

if __name__== '__main__':
#   insert('zamestnanec',
#   jmeno='Roman',
#   prijmeni='Hanák',
#   pozice='developer',
#   plat=100000,
#   firma_id=4,
# )

 connect_to_db(r"C:\Users\roman\Projekty\db_python\Test_DB.db")
 data = select('zamestnanec',['id', 'jmeno', 'prijmeni','pozice'])
 print(data)

 conn.close()