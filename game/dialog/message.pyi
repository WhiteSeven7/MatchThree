from typing import Literal

from pygame.font import Font as PgFont
from pygame.rect import Rect
from pygame.surface import Surface

from .dialog import Dialog

Sender = Literal['myself', 'shifu']
Color = str | tuple[int, int, int] | tuple[int, int, int, int]
Points = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]


class Message:
    fonts: dict[Sender, PgFont]
    dialog: Dialog
    font_color: Color
    bg_color: Color
    # 让字不贴着边
    border: int
    image: Surface
    # pos是文字的左上角
    pos: tuple[int,int]
    points: Points
    rect: Rect

    def __init__(self, dialog: Dialog, sender: Sender, text: str, pos: int): ...

    def height(self) -> int: ...

    def width(self) -> int: ...

    @staticmethod
    def sender_eq(sender: Sender, string: Sender) -> bool: ...

    def draw(self, surf: Surface) -> None: ...

    @staticmethod
    def _triangle_points(
            x_dim: int,
            y_dim: int,
            x: int,
            y: int,
            offset: int,
            width: int = None
    ) -> Points: ...
