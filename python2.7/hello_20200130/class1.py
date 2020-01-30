class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name + " was Born")
    
    def speak(self):
        print("YELP!", self.name)

    def wag(self):
        print("Dog's wag tail")

    def __del__(self):
        print("destroy!!")

class Puppy(Dog):
    def __init__(self) :
        self.name = "Puppy"
        print("Puppy was Born")
    def wag(self):
        print("Dog's wag tail")
        self.__read_diary()

    def __read_diary(self):
        print('read Diary')

    @classmethod
    def classmethod1(cls):
        print('classmethod1')
    #not self because Static Method
    @staticmethod
    def tto():
        print("Ttoooooooooooooooooooooo!!!!!!!!!!")

class Calc:
    @staticmethod
    def plus(a,b):
        return a + b

puddle = Dog("puddle")
spd = Dog("spd")
puddle.speak()

puppy = Puppy()
puppy.speak()
print('Name is', puppy.name)
print('is Dog', isinstance(puppy, Dog))
puppy.wag()
#puppy.__read_diary()
Puppy.tto()
puppy.classmethod1()

#marry = Dog('marry')

print(Calc.plus(1,2))