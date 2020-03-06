#-*- coding: utf-8 -*-
al = "ABC"
print (len(al))
print(type(al))

u = u"가"
print (len(u))
print(type(u))

b = bytearray(u"가", 'cp949')
print ("len(b)", len(b))
print("b", type(b))


b1 = u.encode("cp949")
print("b1", type(b1))
print(b1)

b2 = b1.decode("cp949")
print("b2", type(b2))
print(b2)