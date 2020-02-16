import sqlite3

#https://docs.python.org/2/library/sqlite3.html


conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name, mobile) values(?,?)"
    cur.execute(sql, ('홍길동', None))
    conn.commit()


#multi insert

conn = sqlite3.connect("t.db")

data = (
    (21, '010-1111-2222'),
    (22, '010-3333-4444'),
)

print(type(data))

with conn:
    cur = conn.cursor()
    sql = "insert into tt(id, name) values(?,?)"
    cur.executemany(sql, data)

    conn.commit()
