# 1
class myClass:
    def getString(self):
        n = str(input("Input a string: "))
        return n
    def printString(self, string):
        print(string.upper())

a = myClass()
string = a.getString()
a.printString(string)

# 2
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
        
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length**2
sh1 = Shape()
sq1 = Square(2)
print(sq1.area())
print(sh1.area())

# 3
class Rectangle (Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
re1 = Rectangle(2, 4)
print(re1.area())