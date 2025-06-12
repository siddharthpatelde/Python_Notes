import math

class Tank:
    def __init__(self, A, h):
        self.__A = A
        self.__h = h

    def getVolume(self):
        return self.__A * self.__h

    def getArea(self):
        return self.__A


class Cilinder(Tank):
    def __init__(self, r, h):
        area = math.pi * r * r
        super().__init__(area, h)

    def getR(self):
        return math.sqrt(self.getArea() / math.pi)


class Quarder(Tank):
    def __init__(self, a, h):
        area = a * a
        super().__init__(area, h)

    def getA(self):
        return math.sqrt(self.getArea())


c = Cilinder(1, 2)
q = Quarder(3, 4)

print(f"Cilinder: r = {c.getR()}, Volume = {c.getVolume()}")
print(f"Quarder: a = {q.getA()}, Volume = {q.getVolume()}")
