#-*- coding: utf-8 -*-
import random

print('============== print test ============')
print('한글')
s='한글이지롱'
print("Hello World!")

print(s)

print(random.randrange(1, 7))

print('abc'"def")
print('eee' + 'fff')

s1 = 's1'
s2 = 's2'
print(s1, s2)
print(s1 + s2)
print('Your name is ' + s1)

x,y = 10, 20
print(x,y)

print('============== print format test ============')
str2 ='당신의 이름은 {} 입니다.'
str2 = str2.format('가나다')
print(str2)

print('당신의 이름은 {} 입니다'.format('홍길동'))
print('Num is {:05d}'.format(23))
print('Num is {:+05d}'.format(-23))
print('Num is {:+015.3f}'.format(23.34434))
print('Num is {:+015.7f}'.format(23.34))

print('A is {}, B is {}'.format('a', 'b'))
print('{:b}'.format(7))
print('{:f}'.format(7))

print('========================================\n')

print('============== 연산 test ============')
print('2에 10승 =', 2**10)
print('5 / 2.0 =', 5 / 2.0)
print('5 // 2 =', 5 // 2)
print('5 // 2.0 =', 5 // 2.0)
print('========================================\n')

print('============== type test ============')
print('type(10)=', type(10))

c = 'c'
print(type(c))
print('========================================\n')

print('============== str test ============')
s = '   abC1234   '
print('s:[', s, "], len(s):", len(s))
print('s.upper():[', s.upper(), ']')
print('s.lower():[', s.lower(), ']')
print('s.strip():[', s.strip(), ']')
print('s.strip().capitalize():[', s.strip().capitalize(), ']')
i = s.find('c')
print('c index:', i)

print('s.isalnum(): ', s.isalnum());
print('s.strip().isalnum(): ', s.strip().isalnum());

print('s.isdigit(): ', s.isdigit());
print('isupper.isidentifier():', 'isupper'.isidentifier()) # pythone keyword check
print('========================================\n')


print('============== val test ============')
x,y,z = 1,2,3
print (x,y,z)
print('========================================\n')

print('============== import test ============')
print('dir(random) : ', dir(random))
print('========================================\n')


print('============== Casting test ============')
si, sf = '3', '3.5'
i,f = int(si), float(3.5)
print('type(si)', type(si))
print('type(sf)', type(sf))
print('type(i)', type(i))
print('type(f)', type(f))
#i = int(sf)
#print('type(i)', type(i)) #err
print('========================================\n')


print('============== list[] test ============')
str1 = '1234567890'
print('str1: ', str1)
print('str1[0]:', str1[0])
print('str1[1]:', str1[1])
print('str1[2]:', str1[2])

print('str1[0:9]:', str1[0:9])
print('str1[0:-2]:', str1[0:-2])
print('str1[0:-4]:', str1[0:-4])
print('len', len(str1), '입니다')


message = "Hello World"
print('message:', message)
list1 = message.split(' ')
print('list1:', list1)
print('list1[0]:', list1[0])
print('list1[1]:', list1[1])

message1 = 'A B C'
a,b,c = message1.split(' ')
print('a b c:', a,b,c)

print('============== list[] test2 ============')
fruits = ['오렌지', '사과', '바나나']
prices = [300, 400, 500]
things = ['오렌지', 90, '바나나', 30]

tup_test = fruits[0], fruits[1]
print('type(tup_test):', type(tup_test))

frupri = [fruits, prices]
print('frupri:', frupri)

items = fruits + prices
print('items:', items)

fruits.append('체리')
print('fruits.append:', fruits)
fruits.extend(['딸기, 배'])
print('fruits.extend:', fruits)
fruits.insert(0, '포도')
print('fruits.insert:', fruits)
del fruits[0] # del fruits[0,2]
print('del fruits[0]:', fruits)
fru = fruits.pop(1)
print('fruits.pop:', fruits)
fruits.remove('오렌지')
print('fruits.remove:', fruits)
print('사과 in fruits:','사과' in fruits) #cf. not in
fruits.clear()
print('fruits.clear:', fruits)
print('========================================\n')

print('============== tuple() test (Read Only List) ============')
fruits = ('오렌지', '사과', '바나나')
xy  = 1, 2
print('xy:', xy, 'type(xy):', type(xy))
x, y = 1, 2
print(type(x))
print(type((x,y)))

print('========================================\n')


print('============== Dictionary{} (Hash Map, key:value, JSON) ============')
fruits = {'오렌지': 400, '사과': 200, '바나나': 300}
print('fruits:', fruits)
print('fruits.keys():', fruits.keys())
print('fruits.values():', fruits.values())
print('fruits[바나나]:', fruits['바나나'])
print('바나나 in fruits: ', '바나나' in fruits)
print('200 in fruits: ', '200' in fruits) # Value because False

print('============== example =============')
#문제 오렌지 3개, 사과 2개, 바나나 5개를 샀다면 총 구매액은?
total = fruits['오렌지'] * 3 + fruits['사과'] * 2 + fruits['바나나'] * 5
print('total price : ', total)

print('========================================\n')

print('============== Set{} 자료구조 ============')
s1 = {1,2,3}
s2 = {3,4,5}

print('s1 | s2', s1 | s2)
print('s1 ^ s2', s1 ^ s2)
s_union = s1.union(s2)
s1.update(s2)
print('s_union union', s_union)
print('s1 update', s_union)


print('========================================\n')


print('============== if test ============')
if(20 > 10):
    print(20 > 10)

if(3!=4):
    print('false')

if(1 > 2 or 3 > 2):
    print('or')
print('============== if test 1 ============')
score = 80
if score > 70:
    print('합격')
    print('축하합니다!')
elif score == 70:
    print('합격도 아니고 불합격도 아님!')
else :
    print('불합격')

print('========================================\n')

print('============== for test ============')
for x in [1,2,3]:
    print(x)
print('')

print('============== for range test ============')
for i in range (0, 3):
    print(i)
print('')

for i in range (0, 10, 2):
    print(i)
print('')

arr = [i ** 2 for i in range(0, 20, 2)]
print(arr)
print('max=', max(arr), ', min=', min(arr))

fruits = ['오렌지', '사과', '바나나']
for x in fruits:
    print(x)
print('')

outs = [f for f in fruits if f != '사과']
print(outs)

for i in range(0,1):
    print(fruits[i])

print('============== list, dictionaly for test ============')
lst = ['오렌지', '사과', '바나나']
dic = {'오렌지': 400, '사과': 200, '바나나': 300}

for key in dic:
    print("key=", key, dic[key])

for i, value in enumerate(lst):
    print("tt=", i, value)

for key, element in dic.items():
    print("items.key=", key, ", element=", element)

print('============== while test ============')

i, sum = 0,0
while(i >=0):
    i += 1    
    if(i > 10 and i < 20):
        continue
    sum += i
    if (i == 100):
        print("End!!", sum)
        break

print('============== example1 =============')
#1부터 100까지 합을 구하시오.
sum = 0
for i in range(1, 101):
    sum += i
print('1~100합은 : ' , sum)

print('============== example2 =============')
#1부터 100까지 홀수의 합을 구하시오.
odd_sum = 0
for i in range(1, 101):
    if i%2 == 1 :
        odd_sum += i
print('1~100홀수합은 : ' , odd_sum)

print('========================================\n')


print('============== Function test ============')
def fn():
    print('fn called')

def exp(x):
    return x ** 2

def get_fruits():
    return ['오렌지', '사과', '바나나']
print(get_fruits()[0])

def get_name():
    return 'Kent', 'Beck'

name1, name2 = get_name()
print(name1, name2)
t_name = get_name()
print(t_name)

def full_name(first_name, lst_name):
    return first_name + lst_name

print(full_name('FIRST', '_LAST'))

print('============== Function 가변 인자 test ============')
def var_param(a, *vp):
    print(a, len(vp), vp[len(vp)-1])
var_param('A', 'b', 'c', 'd')

def default_param(a, vp = 100):
    print(a, vp)
default_param(1)

print('============== Function Recursive test ============')

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))

print('========================================\n')

print('============== Class Object Instance test ============')
print('CamelCase는 Class명 및 Class File 명에 사용');
print('snake_case는 변수 및 함수에 사용') 
print('========================================\n')


print('============== Built-in Functions ============')
print('https://docs.python.org/ko/3/library/functions.html')
print('abs(-3)', abs(-3))
print('divmod(5,2)', divmod(5,2))
print('bin(7)', bin(7))
print('oct(7)', oct(7))
print('hex(7)', hex(7))

# None, 0 check 동시에 가능
print('bool(-1)', bool(-1))

print('int(123)', int('123'))
print('float(123)', float('123'))
print('str(123)', str(123))
print('2^3', pow(2,3))

#현재 전역변수
print('현재 전역변수 globals() :', globals()) 

#man page
print('man page help(min) :', help(min))

#반올림 딱중간일땐 무조건 짝수를 선택
print('round(1.5)', round(1.5))
print('round(2.5)', round(2.5))
print('round(2.51)', round(2.51))
print('round(2.3456)', round(2.3456), 3)

#접근가능한 메모리 올라가있는 변수 밑 function들
print('dir()', dir())
print('========================================')
print('dir(random)', dir(random))
print('========================================')
import builtins
print('dir(builtins)', dir(builtins))
print('========================================\n')

eval('print("eval, 123")')
exec('print("exec, 123")')


print('============== Built-in Class ============')
class TestClass:
    name = 'TEST'

    #instance가 부르던 static으로 부르던 staticmethod를 있으면 알아서 한다
    @staticmethod
    def static_method():
        print('static_method')

    def get_name(self):
        print(type(self).__name__, 'get_name')
        return self.name
    
    @property
    def full_name(self):
        return self.name + "FFF"

class Child(TestClass):
    def get_name(self):
        super().get_name()
        return "Child Name:" + self.name

test = TestClass()
#print(test.get_name())

### @property로 선언해서 함수를 property로 부름
print(test.full_name)

child = Child()
print(child.get_name())

print('============== Built-in getattr Class ============')
getattr(test, 'get_name')()
getattr(TestClass, 'static_method')()
print("hasattr(test, 'get_name')", hasattr(test, 'get_name'))
#delattr(class, 'attr name')
print('isinstance(test, TestClass)', isinstance(test, TestClass))
print('issubclass(Child, TestClass)', issubclass(Child, TestClass))


print('================unique한값? id(주소값과 같다)가 더 unique=====================')
print('hash(test)', hash(test))
print('id(test)', id(test))
print('========================================')
#호출 가능 여부
c = callable(test.get_name)
print(c)
print('========================================\n')


print('============== bytearray, bytes, chr ============')
#cp949
s = '한글'
print(s, ' len:', len(s))
s2 = bytes(s, 'UTF8')
print(s2, 'len:', len(s2))
s3 = bytearray(s, 'UTF8')
print(s3, 'len:', len(s3))

#ascii
print('chr(97):', chr(97))
print("ord('a'):", ord('a'))
print('========================================\n')
