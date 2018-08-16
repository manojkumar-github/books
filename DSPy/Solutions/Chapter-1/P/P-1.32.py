"""
Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output
device. That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator, like + or =, can be
done on a separate line. After each such input, you should output to the Python console what would be displayed on
your calculator.
"""

class Calculator(object):

    output = 0

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x , y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y

    def calculate(self):
        user_input = input('Enter a number or a operator:')

        if isinstance(eval(user_input), (int, float)):
            print (user_input, sep='')
        elif user_input in ['+','-','*','/']:
            print (user_input, sep='')
        elif user_input == '=':
            return self.output
        else:
            return
        self.calculate()



obj = Calculator()
print (obj.calculate())