from math import pi, atan

from .math_ import sign


class Vect:
    # 实例化方法
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @classmethod
    def fse(cls, sequence):
        """从列表、元组或任何可以[0][1]的数据结构中读取"""
        return cls(sequence[0], sequence[1])

    @classmethod
    def fma(cls, mapping):
        """从字典或任何可以['x']['y']的数据结构中读取"""
        return cls(mapping['x'], mapping['y'])

    # 信息读取
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x},{self.y})'

    # 格式转化
    def __str__(self):
        return f'({self.x},{self.y})'

    def __bool__(self):
        return bool(self.x) or bool(self.y)

    # 数学运算
    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return self.__class__(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__class__(self.x * other, self.y * other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def per_mul(self, other):
        return self.__class__(self.x * other.x, self.y * other.y)

    def per_imul(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __floordiv__(self, other):
        return self.__class__(self.x // other, self.y // other)

    def __ifloordiv__(self, other):
        self.x //= other
        self.y //= other
        return self

    def per_floordiv(self, other):
        return self.__class__(self.x // other.x, self.y // other.y)

    def per_ifloordiv(self, other):
        self.x //= other.x
        self.y //= other.y
        return self

    def __mod__(self, other):
        return self.__class__(self.x % other, self.y % other)

    def __imod__(self, other):
        self.x %= other
        self.y %= other
        return self

    def per_mod(self, other):
        return self.__class__(self.x % other.x, self.y % other.y)

    def per_imod(self, other):
        self.x %= other.x
        self.y %= other.y
        return self

    # 相等比较
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 哈希值
    def __hash__(self):
        return hash((self.x, self.y))

    # 迭代方法
    def __iter__(self):
        return iter((self.x, self.y))

    def tuple(self):
        return self.x, self.y

    def list(self):
        return [self.x, self.y]

    def dict(self):
        return {'x': self.x, 'y': self.y}

    # 其他数学运算
    def angle(self):
        if self.x == 0:
            return sign(self.y) * pi / 2
        if self.x > 0:
            return atan(self.y / self.x)
        return sign(self.y) * pi + atan(self.y / self.x)

    def half_max(self):
        return max(abs(self.x), abs(self.y))


UP = Vect(0, -1)
DOWN = Vect(0, 1)
LEFT = Vect(-1, 0)
RIGHT = Vect(1, 0)
LOZENGE = {UP, DOWN, LEFT, RIGHT}
CLOVER = {
    Vect(0, -1), Vect(0, 1), Vect(-1, 0), Vect(1, 0),
    Vect(0, -2), Vect(0, 2), Vect(-2, 0), Vect(2, 0)
}
