class Circle:
    def __init__(self, r):
        self.__r = r

    def getR(self):
        return self.__r

    def setR(self, r):
        self.__r = r

    def getArea(self):
        return 3.14 * self.__r * self.__r


circle1 = Circle(3)
circle2 = Circle(4)

print(f"Circle 1: r = {circle1.getR()}, A = {circle1.getArea()}")
print(f"Circle 2: r = {circle2.getR()}, A = {circle2.getArea()}")

circle1.setR(10)
print(f"Circle 1: r = {circle1.getR()}, A = {circle1.getArea()}")
