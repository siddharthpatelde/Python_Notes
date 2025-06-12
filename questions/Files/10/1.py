class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        return self.a * self.b

    def getPerimeter(self):
        return 2 * (self.a + self.b)


r1 = Rectangle(2, 3)
r2 = Rectangle(4, 7)

print("Rectangle 1 Area:", r1.getArea())
print("Rectangle 1 Perimeter:", r1.getPerimeter())
print("Rectangle 2 Area:", r2.getArea())
print("Rectangle 2 Perimeter:", r2.getPerimeter())
