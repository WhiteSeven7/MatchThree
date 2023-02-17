from typing import Collection

from pygame import Surface

from tool.vector import Vect
from .box import Box, BoxKind
from .game import Game
from .stone import Stone, StoneKind

Shape = list[list[int]]


class Wall:
    # 对照表，用于一些函数
    box_kind_dict: dict[int, BoxKind | None]
    # 游戏框架
    game: Game
    # 左上角的位置，用于绘制
    pos: Vect
    # 单个格子尺寸
    size: int
    # 组
    group: dict[Vect, None | Box]
    # normal_group: dict[Vect, None | Box]
    # generator_group: dict[Vect, None | Box]
    # x,y方向的数量，用于有序迭代
    x_num: int
    y_num: int
    # 若被改为真，则执行下落换位程序
    need_drop: bool

    # 通过self[..]对group进行管理
    def __getitem__(self, item: Vect) -> None | Box: ...

    def __setitem__(self, key: Vect, value: None | Box): ...

    def __delitem__(self, key: Vect) -> None: ...

    # group的迭代
    def __iter__(self) -> iter: ...

    def keys(self) -> Collection[Vect]: ...

    def values(self) -> Collection[Box]: ...

    def items(self) -> Collection[tuple[Vect, Box]]: ...

    # 初始化
    def __init__(self, game: Game, x: int, y: int, size: int, shape: Shape, selected_kind: list[StoneKind]): ...

    # 下面这些方法只在Wall实例化时运行，隶属于__init__的子函数
    def _set_group(self, shape: Shape) -> None: ...

    def _generate(self, selected_kind: list[StoneKind]) -> None: ...

    def _generate_one(self, x: int, y: int, selected_kinds: list[StoneKind]) -> None: ...

    # 在每帧运行一次，剩下的是它的子函数
    def update(self, surf: Surface) -> None: ...

    # 绘制，在这里是update子函数（因为drop()的需求），在box和stone中独立于update
    def draw(self, surf: Surface) -> None: ...

    def get_ups(self, empties: list[Box]) -> set[Stone]: ...

    def empty_check(self) -> None: ...

    def drop(self) -> None: ...
