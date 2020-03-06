#-*- coding: utf-8 -*-

print('============== input test ============')
# cmd = input("Input>>")
# print(cmd)
# 이름, 나이,성별을 입력받아, "당신의 이름은 {}, 나이는 {}, 성별은{}입니다"출력
error_msg ='정확히 입력해주세요!!!'

#1. 값이 존재여부 체크
cmd = input('Input(usage:이름,나이,성별)>> ')
if cmd == '':
    print(error_msg)
    exit()
#2. ,가 있는지 체크
if ',' not in cmd:
    print(error_msg)
    exit()

cmds = cmd.split(',')
#3. 3개의 값이 있는지
if len(cmds) != 3:
    print(error_msg)
    exit()

print('당신의 이름은 {}, 나이는 {}, 성별은{}입니다'.format(cmds[0],cmds[1], cmds[2]))
print('========================================\n')