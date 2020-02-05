#-*- coding: utf-8 -*-
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return u"{}:{}".format(self.name, self.score).encode('euc-kr')

students = [
    Student(u"김일수", 10),
    Student(u"김이수", 30),
    Student(u"김삼수", 20)
]

print(students[0])

def print_students():
    print("=======================")
    for s in students:
        print(s)

def print_stu1(str1):
    print("---------------------")
    for s in str1:
        print(s)
ss = sorted(students, key=lambda stu: stu.score, reverse=False) 
#print_students()
print_stu1(ss)
print(type(ss),dir(ss))


students.sort(key=lambda stu: stu.score)
print_students()

