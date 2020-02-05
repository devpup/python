

# file = open("filename", "w")
# file.write("파일내용")
# file.close()


# with open("filename", "w") as file:
# 	file.write("...........")

# #with open("filename", "r", encoding='utf8') as file:
# with open("filename", "r") as file:
# 	for line in file:
# 		print(line)


# iterable functions

# ss = {0,1,2,3,4,5,6} #set이고 data가 sorting 되네~~
# it = iter(ss)
# next(it,None) //마지막까지만 돈다~


# *** filter()
# 1)
# >>> int_number = range(-5, 6)
# >>> print(list(int_number))
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# >>> negatives = filter(lambda x: x < 0, int_number)
# >>> l1 = list(negatives)
# >>> l1
# [-5, -4, -3, -2, -1]

# 2)
# >>> def fn(x): return x < 0
# ...
# >>> n2 = filter(fn, int_number)
# >>> n2
# <filter object at 0x000001AA4896CD48>
# >>> type(n2)
# <class 'filter'>
# >>> list(n2)
# [-5, -4, -3, -2, -1]


# *** map
# >>> triple_numbers = map(lambda x:x*3, int_number)
# >>> print(list(triple_numbers))
# [-15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15]
# >>> type(triple_numbers)
# <class 'map'>

