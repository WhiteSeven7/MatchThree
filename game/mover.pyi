from typing import Literal

from tool.vector import Vect
from .stone import Stone
from .wall import Wall

MoverStatus = Literal['swap', 'cancel', 'not_move']
TowStones = tuple[Stone, Stone]


class Mover:
    wall: Wall
    # 需要move的两个stone
    moving_stones: None | TowStones
    # 若为真，执行exchange()函数
    need_exchange: bool
    # 在两个stone发生exchange()后，打开
    check_stones: None | TowStones
    # 防止反复打回的bug
    status: 'MoverStatus'

    def __init__(self, wall: Wall): ...

    def exchange(self) -> None: ...

    def check_exchange(self) -> None: ...

    def set_moving(self, stone_1: Stone, stone_2: Stone,status: 'MoverStatus', direction: None | Vect = None): ...

    # 让stone移动
    def stone_move(self)->None:...
