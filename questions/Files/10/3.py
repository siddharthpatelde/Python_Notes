class Triangle:
    def __init__(self, c, h):
        self.__c = c
        self.__h = h

    def getArea(self):
        return 0.5 * self.__c * self.__h

    def __str__(self):
        return f"Base: {self.__c}, Height: {self.__h}, Area: {self.getArea()}"


tri = Triangle(4, 5)
print(tri)
