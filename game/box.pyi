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

    def __init__(self, wall: Wall, kind: BoxKind, x: int, y: int): ...

    # 绘制函数
    def draw(self, surf: Surface): ...

    # update和它的子函数
    def update(self): ...
