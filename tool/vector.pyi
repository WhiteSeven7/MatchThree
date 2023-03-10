from typing import Self, Sequence, Mapping


class Vect:
    x: int
    y: int

    # 实例化方法
    def __init__(self, x: int = 0, y: int = 0): ...

    @classmethod
    def fse(cls, sequence: Sequence[int]) -> 'Vect': ...

    @classmethod
    def fma(cls, mapping: Mapping[str, int]) -> 'Vect': ...

    #信息读取
    def __repr__(self): ...

    # 格式转化
    def __str__(self): ...

    def __bool__(self): ...

    # 数学运算
    def __neg__(self) -> 'Vect': ...

    def __add__(self, other: 'Vect') -> 'Vect': ...

    def __iadd__(self, other: 'Vect') -> Self: ...

    def __sub__(self, other: 'Vect') -> 'Vect': ...

    def __isub__(self, other: 'Vect') -> Self: ...

    def __mul__(self, other: int) -> 'Vect': ...

    def __rmul__(self, other) -> 'Vect': ...

    def __imul__(self, other: int) -> Self: ...

    def per_mul(self, other: 'Vect') -> 'Vect': ...

    def per_imul(self, other: 'Vect') -> Self: ...

    def __floordiv__(self, other: int) -> 'Vect': ...

    def __ifloordiv__(self, other: int) -> Self: ...

    def per_floordiv(self, other: 'Vect') -> 'Vect': ...

    def per_ifloordiv(self, other: 'Vect') -> Self: ...

    def __mod__(self, other: int) -> 'Vect': ...

    def __imod__(self, other: int) -> Self: ...

    def per_mod(self, other: 'Vect') -> 'Vect': ...

    def per_imod(self, other: 'Vect') -> Self: ...

    # 相等比较
    def __eq__(self, other) -> bool: ...

    # 哈希值
    def __hash__(self) -> int: ...

    # 迭代方法
    def __iter__(self): ...

    def tuple(self) -> tuple[int, int]: ...

    def list(self) -> list[int]: ...

    def dict(self) -> dict[str, int]: ...

    # 其他数学运算
    def angle(self) -> float: ...

    def half_max(self) -> int: ...


UP: 'Vect'
DOWN: 'Vect'
LEFT: 'Vect'
RIGHT: 'Vect'
LOZENGE: set['Vect']
CLOVER: set['Vect']
