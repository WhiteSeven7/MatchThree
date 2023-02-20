from pygame.surface import Surface

from tool.vector import Vect
from .message import Message, Sender
from ..game import Game


class Dialog:
    game: Game
    surf: Surface
    pos: Vect
    width: int
    height: int
    gap: int
    _messages: list[Message]
    _now_y: int

    def __init__(self, game: Game, x: int, y: int, width: int, height: int, gap: int): ...

    def add(self, sender: Sender, text: str) -> None: ...

    def draw(self, surf: Surface): ...
