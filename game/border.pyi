from pygame import Surface

from tool.vector import Vect
from .wall import Wall

Color = str | tuple[int, int, int] | tuple[int, int, int, int]


class Border:
    """鼠标所在box的外围的白色方框"""
    wall: Wall
    image: Surface
    g_pos: None | Vect
    pos: Vect

    def __init__(self, wall: Wall, color: Color): ...

    def right_pos(self) -> bool: ...

    def draw(self, surf: Surface) -> None: ...
