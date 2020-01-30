class TestClass:
    name = "TEST"

    def get_name(self):
        print("qqqqqqqqqqqqqqq")
        return self.name

    @property
    def property_test(self):
        print("property_test!!!!!!!!!")

class Child1(TestClass, object):
    def get_name(self):
        super(Child1, self).get_name()
        return "Child Name: " + self.name

test = TestClass()
child = Child1()
print("1111>>>", test.get_name(), child.get_name())

c = callable(test.get_name())
print("cccccc >> ", c)


m = raw_input('TestClass Method Name >>>> ')
if hasattr(test,m) :
    getattr(test, m)()
#     #getattr(test,'get_name')()

print("hash: " + str(hash(test)))
print(id(test))
print(globals())

test.property_test

s = 'abcdefg'
s2 = bytearray(s, 'UTF8')
print(len(s2))