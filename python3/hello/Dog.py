class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name + " was Born")
    
    def speak(self):
        print("YELP!", self.name)

    def wag(self):
        print("Dog's wag tail")

    def __del__(self):
        print(type(self).__name__, "destroy!!")

class Puppy(Dog):
    def __init__(self) :
        self.name = "Puppy"
        self.color = "Red"
        print("Puppy was Born")

    def speak(self):
        print("Bow wow!", self.name)

    def wag(self):
        print("Dog's wag tail")
        self.__read_diary()

    # 내부에서만 사용할 수 있음.. private
    def __read_diary(self):
        print('read Diary')

    @classmethod
    def classmethod1(cls):
        print('classmethod1')
    #not self because Static Method
    
    @staticmethod
    def tto():
        print("Ttoooooooooooooooooooooo!!!!!!!!!!")


print("############ Dog(Puddle) Start ############")
puddle = Dog("puddle")
spd = Dog("spd")
puddle.speak()
print("####################################")

print("############ Puppy Start ############")
puppy = Puppy()
puppy.speak()
print('Name is', puppy.name)
print('is Dog', isinstance(puppy, Dog))
puppy.wag()
#puppy.__read_diary()
Puppy.tto()
puppy.classmethod1()
print("####################################")

#marry = Dog('marry')

