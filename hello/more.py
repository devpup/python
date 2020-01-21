lst =['오렌지', '사과', '배']
dic = {'오렌지':400, '사과':300, '배':200}

for key in dic:
    print("key=", key, dic[key])

print(list(enumerate(lst)))

for i, value in enumerate(lst):
    print("tt=", i, value)
    print(lst[i])

for key, element in dic.items():
    print("items.key=", key, ", element=", element)

for i in range(0,20,2):
    print(i)

arr = [i ** 2 for i in range(0,20,2)]
print(arr)

print('min=', min(arr))
print('max=', max(arr))

outs = [f for f in lst if f != '사과']
print(outs)

#cmd = input("Input(usage:A, B)>> ")
#print(cmd)

#cmds = cmd.split(',')
#print(cmds)

human = input("Input(usage:이름, 나이, 성별)>> ")
print(human)

# if (human not in ','):
#     print(", 없음!!!")
#     exit()

if (human.find (',')== -1):
    print(", 없음!!!")
    exit()


humans = human.split(',')
print(humans)


outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {} 입니다"
print('len(humans)', len(humans))
if len(humans) == 3:
    print(outmsg.format(humans[0],humans[1],humans[2]))  
else:
    print("정확히 입력해주세요!!!")
    exit()