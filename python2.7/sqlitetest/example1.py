#-*- coding: utf-8 -*-
import sqlite3
import random

fam_names = list("김이박정최")
first_name = list("건성현욱정민현주희")

def make_name():
    sung = random.choice(fam_names)
    name = "".join(random.sample(first_name,2))
    #tuple 형태로 만들기 위해서 ()로 싸고 뒤에 , 붙임
    return (sung + name, )

data = []
for i in range(0, 100):
    data.append(make_name())

conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name) values(?)"
    cur.executemany(sql, data)
    conn.commit()
