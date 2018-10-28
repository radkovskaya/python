# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt

class Triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def square(self):
        print("Площадь треугольника :" ,(0.5 * ((self.x1 - self.x3) * (self.y2 - self.y3) - (self.x2 - self.x3) * (self.y1 - self.y3))))
    def height(self):
        print("Высота треугольника с основанием в точках (x1,y1), (x2,y2) :", 2 * (0.5 * ((self.x1 - self.x3) * (self.y2 - self.y3) - (self.x2 - self.x3) * (self.y1 - self.y3))) / (sqrt(((self.x1 - self.x2)**2)+((self.y1 - self.y2)**2))))
    def perimeter(self):
        print("Периметр треугольника: ", sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2)) + sqrt(((self.x2 - self.x3)**2)+((self.y2 - self.y3)**2)) + sqrt(((self.x1 - self.x3)**2)+((self.y1 - self.y3)**2)))

# triang_1 = Triangle(1, 6, 9, 6, 10, 9)
# triang_1.square()
# triang_1.height()
# triang_1.perimeter()


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Trapeze:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    def info(self):
        if diff(self.p1, self.p2) == diff(self.p3, self.p4) or diff(self.p1,self.p4) == diff(self.p2,self.p3):
            print("Трапеция является равнобедренной")
        else:
            print("Трапеция не является равнобедренной")
    def h(self):
        return sqrt((diff(self.p1, self.p2)**2 - (diff(self.p1,self.p4) - diff(self.p2,self.p3))/2)**2)
    def square(self):
        return (diff(self.p2, self.p3) + diff(self.p1, self.p4)) * self.h() * 0.5
    def perimeter(self):
        return (diff(self.p1, self.p2) + diff(self.p2, self.p3) + diff(self.p3, self.p4) + diff(self.p1,self.p4))
def diff(p1, p2):
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# A = Point(-3, 0)
# B = Point(-2, 2)
# C = Point(2, 2)
# D = Point(3, 0)
# trap_1 = Trapeze(A, B, C, D)
# print("Длина стороны AB = ", diff(A, B))
# print("Длина стороны BC = ", diff(B, C))
# print("Длина стороны CD = ", diff(C, D))
# print("Длина стороны AD = ", diff(A, D))
# trap_1.info()
# print("Площадь трапеции = ", trap_1.square())
# print("Периметр трапеции = ", trap_1.perimeter())






