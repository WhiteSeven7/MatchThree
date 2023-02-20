from typing import Literal

from pygame import Surface

from tool.vector import Vect
from .stone import Stone
from .wall import Wall

BoxKind = Literal['normal', 'generator']


class Box:
    # 容器
    wall: Wall
    # 种类
    kind: BoxKind
    # 位置，格点中，绘制位置
    g_pos: Vect
    pos: Vect
    # stone或者none
    content: None | Stone
    # 半透明灰色方块
    image: Surface
    # 记录在wall.three_match()中是否已在match组中
    match: None | set['Box']

    def __init__(self, wall: Wall, kind: BoxKind, x: int, y: int): ...

    def __repr__(self) -> str: ...

    # 下面三个为功能函数
    def is_empty(self) -> bool: ...

    def clear(self) -> None: ...

    def contain(self, stone: Stone) -> None: ...

    def kind_is(self, kind: 'BoxKind'): ...

    def can_crush(self) -> bool: ...

    def same_stone_kind(self, box1: 'Box', box2: 'Box') -> bool: ...

    # 绘制函数
    def draw(self, surf: Surface): ...
