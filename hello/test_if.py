print('================== if ==================')
score = 80
if score > 70:
    print('합격')
    print('축하합니다!')
elif score == 70:
    print('합격도 아니고 불합격도아님!!')
else:
    print('불합격')
    print('다음기회!')

print('================== if in(each)==================')
for i in range(1,100):
    print(i)

fruits = ['오렌지','사과','바나나']
for x in fruits:
    print(x)

for y in fruits[0:2]:
    print(y)

i, sum = 0,0
while( i >=0):
    i += 1
    if(i > 10 and i < 20):
        continue
    sum += i
    if (i == 100):
        print("End!!", sum)
        break