import random

print(random.randrange(6))

lst = range(1, 14)
print( random.shuffle(lst))

lst = list(range(1, 14))
print(lst, type(lst))

random.shuffle(lst)
print(lst)

apb = "abcdefghijklmnopqrstuvwxyz"
print(random.choice(apb))

print(random.uniform(1, 10)) #1 ~ 10 float

print(random.sample(lst, k=3))