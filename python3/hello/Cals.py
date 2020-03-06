class Calc:
    # @staticmethod
    # def plus(a,b):
    #     return a + b

    def plus(self, num1, num2) :
        return num1 + num2

    def minus(self, num1, num2) :
        return num1 - num2

    def mul(self, num1, num2) :
        return num1 * num2

    def div(self, num1, num2) :
        return num1 / num2


print(Calc.plus(1,2))