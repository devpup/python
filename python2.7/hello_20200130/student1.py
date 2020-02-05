#-*- coding: utf-8 -*-
import os
from functools import reduce

class Student:
    def __init__(self, name, gender, age, score):
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)

    def __str__(self):
        #return u"{}:{}".format(self.name, self.score).encode('euc-kr')
        return u"{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.score).encode('euc-kr')

students = []

print(os.getcwd())
with open('students.csv', 'r') as file:
    for i, line in enumerate(file):
        ss = line.decode('utf-8').strip().split(',')
        stu = Student(ss[0], ss[1], ss[2], ss[3])
        students.append(stu)    
        #print(stu)

students.sort(key=lambda stu:stu.score, reverse=True)

for s in students:
    print(s)

#타언어 이항연산자
#type(x) == int ? A:B
#python 이항연사자
#A if type(A) == int else B

#최초 x의 타입은 student고 reduce로 돌고 두번째부터는 int다
total = reduce(lambda x,y: (x if type(x) == int else x.score) + y.score, students)

print("total >>>>", total)

