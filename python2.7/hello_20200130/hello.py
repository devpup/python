#-*- coding: utf-8 -*-
import random

print(u'한글')

s=u'한글이지롱'

print("Hello World!")
print(s)
print(random.randrange(1, 7))

for x in [1,2,3]:
    print(x)

if(20 > 10):
    print(20 > 10)

print(2**10)
print(5 / 2.0)
print(5 // 2.0)

if(3!=4):
    print('false')

if(1 > 2 or 3 > 2):
    print('or')

print(type(10))

print('abc'"def")
print('eee' + 'fff')

s1 = 's1'
s2 = 's2'

print(s1, s2)
print(s1 + s2)
print('Your name is ' + s1)

c = 'c'
print(type(c))

str1 = '1234567890'
print(str1[0])
print(str1[1])
print(str1[2])

print(str1[0:9])
print(str1[0:-2])
print('len', len(str1), u'입니다')
print(len(str1))


message = "Hello World"
list1 = message.split(' ')
print(message.split(' '))
print(list1[0])
print(list1[1])
x,y = 10, 20
print(x,y)

str2 =u'당신의 이름은 {} 입니다.'
str2.format(u'홍길동')
print(str2)

print(u'당신의 이름은 {} 입니다'.format(u'홍길동'))
print('Num is {:05d}'.format(23))

s = '    abc 1234   '
print(s.upper())
print(s.strip())

i = s.find('c')
print(i)