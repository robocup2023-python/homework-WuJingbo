'''
题⽬：创建Point和Vector类，以将现实世界中的⼆维或三维的点抽象成Python中的类。要求 Point和Vector类可以接受两个或三个参数（对应x、y、z三个坐标）来初始化，两个参数的时候z坐标默认为0。
使⽤Print打印的时候输出是 Point(x, y, z)/Vector(x, y, z) （x、y、z要替换成点对应的属性值）。
要求对Vector类重载加号和减号，实现向量的加法和减法。
要求重载Point类的加法和减法，Point类加减Vector类得到新的Point类，Point类减Point类得到新的Vector，Point类加 Point类报错。
要求Point类在类初始化和销毁的时候分别输出 创建了Point(x, y, z) 和销毁了Point(x, y, z) 。要求重载⽐较符号，当且仅当x、y、z全部相等，Point和Vector类==才是true，当对Point类来说，A点到原点的距离⼩于B到原点的距离时，A<B为true，对Vector则是模⻓。要求重载 Vector的乘法和触发，*x表⽰逆时针旋转x度，/x表⽰顺时针旋转x度
程序分析：利⽤Python的魔术⽅法
'''
import math


class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        print("创建了", self)

    def __str__(self):
        return f"Point({self.x},{self.y},{self.z})"

    def __add__(self, other):
        if isinstance(other, Point):
            raise TypeError()
        elif isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
        elif isinstance(other, Vector):
            return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def __eq__(self, other):
        if (self.x, self.y, self.z) == (other.x, other.y, other.z):
            return True
        return False

    def __lt__(self, other):
        return self._len() < other._len()

    def _len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.len = self._len()

    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __eq__(self, other):
        if (self.x, self.y, self.z) == (other.x, other.y, other.z):
            return True
        return False

    def __lt__(self, other):
        return self.len < other.len

    def _len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __mul__(self, x):
        new_deg = math.radians(x)
        return Vector(self.len * math.cos(new_deg), self.len * math.sin(new_deg))

    def __truediv__(self, x):
        new_deg = math.radians(x)
        return Vector(self.len * math.cos(-new_deg), self.len * math.sin(-new_deg))
