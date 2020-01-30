#-*- coding: utf-8 -*-

class Square:
    x,y = 0,0

    def __init__(self):
        print(u'사각형 created')
    
    def set_XY(self, x, y):
        self.x, self.y = x, y
        1

#직사각형
class Rect(Square):
    def extent(self) :
        return self.x * self.y

#평행사변형
class Parallelogram(Square):
    def extent(self) :
        return self.x * self.y

rect_type = input('사각형의 종료는?\n 1)직사각형\n 2)평행사변형\n >>'.decode('utf-8').encode('euc-kr'))

print(type(rect_type))
print('rect_type:' , rect_type)

if rect_type == 1:
    rect = Rect()
    tmp = input('가로와 세로는?? (usage: 가로, 세로)'.decode('utf-8').encode('euc-kr'))
    print(type(tmp), tmp)
    if len(tmp) != 2:
        print("len is not 2")
        exit()

    rect.set_XY(tmp[0], tmp[1])
    print(u'직사각형의 넓이는 {}입니다'.format(rect.extent()))
elif rect_type == 2:
    para = Parallelogram()
    str_tmp = input('가로와 세로는?? (usage: 가로, 세로)'.decode('utf-8').encode('euc-kr'))
    x, y = str_tmp.split(',')
    rect.set_XY(x,y)
    print(u'평행사면형의 넓이는 {}입니다'.format(para.extent()))
else :
    print(u'잘못입력하셨습니다')