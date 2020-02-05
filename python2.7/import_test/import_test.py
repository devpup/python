from calcs import plus,minus,mul,div
print(plus(3,5))


import calcs
print(calcs.plus)


import sys, os
os.system('cls')
print("Path>>", sys.path)
print("pwd>>", os.getcwd())
os.chdir("..")  #change dir
print("cwd>>", os.getcwd()) #current working dir
print("dir>>", dir())
os.system('dir')

#cf. from utils import *
#cf. import my_pkg.test_module.fn (directory.module(filename).function)



