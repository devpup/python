
print(4 // 2)
print(4 / 2)
print(type(4//2))
print(type(4/2))

c = 'c'
print(type(c))

str1 = 'abc'
print(str1[0])

message = "Hello World"
print(message[0:7])
print(message[:7])
print(message[:len(message)])

message = "aaa bbb ccc"
print(message.split(' '))
print(message.split(' ')[1])
a,b,c = message.split(' ')
print(a + b + c)

x,y,z=1,2,3
print(x)
print(y)
print(z)

print("아나녕하세요")

si,sf='3','3.5'
i,f = int(si),float(sf)
print(i,f)
ff = float(si)
print(ff)
#ff = int(sf)
#print(ff)

str23 = str(23)
print(str23)
print(type(str(23)))

print('================== LIST ==================')

fruits = ['오렌지','사과','바나나']
prices=[30,40,50]
things =['오렌지', 90, '바나나', 50]
print(fruits[0:2])
print(prices)
fru_pri = [fruits, prices]
print(fru_pri)
fru_pri2 = fruits + prices
print(fru_pri2)
fruits.append('딸기')
print('fruits', fruits)
fruits.extend(['배', '키위'])
print('fruits', fruits)
print(len(fruits))
print(len(fruits[0]))
fruits.insert(0, '포도')
print('fruits', fruits)
print(fruits.pop(1))
print('fruits', fruits)
fruits.remove('포도')
print('fruits', fruits)

print('================== Tuple (Read Only List) ==================')
fruits = ['오렌지', '사과', '바나나']
q=fruits[0],fruits[1]
print(q)

fruits = ('오렌지', '사과', '바나나')
print(fruits)
print(fruits[0:2])

print('================== Dictionary (Hash Map, keyValue, Json) ==================')
fruits = {'오렌지':400, '사과':300, '바나나':200}
print(fruits.keys())
print(fruits.values())
print(fruits['바나나'])
print('오렌지' in fruits)
print(200 in fruits)

print(fruits['오렌지']*3+fruits['사과']*2+fruits['바나나']*5)



print('================== if ==================')