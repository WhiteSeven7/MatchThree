from typing import Collection

from pygame import Surface
from pygame.event import Event

from tool.vector import Vect
from .border import Border
from .box import Box, BoxKind
from .faller import Faller
from .mover import Mover
from .stone import StoneKind
from ..game import Game

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
    # 记录能产生的Stone类型
    stone_kinds: list[StoneKind]
    faller: Faller

    # # 若被改为真，则执行下落换位程序
    # need_drop: bool
    # # fall_match_time，有stone下落时始终为0，没有时会每帧+1（达到60时不增），达到60时才可以自动启动three_match()
    # fm_time: int
    # fm_cool: int
    # 显示鼠标所在位置

    mob: Border
    # 被选中的位置，边框
    clicked: Border
    # 进行移动的相关操作
    mover: Mover
    # 储存get_three的结果，减少重复调用
    three_list: None | list[set[Box]]

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
    def __init__(self, game: Game, x: int, y: int, size: int, shape: 'Shape', selected_kind: list[StoneKind]): ...

    # 下面这些方法只在Wall实例化时运行，隶属于__init__的子函数
    def _set_group(self, shape: 'Shape') -> dict[Vect, None | Box]: ...

    def _generate(self, selected_kind: list[StoneKind]) -> None: ...

    def _generate_one(self, x: int, y: int, selected_kinds: list[StoneKind]) -> None: ...

    # 在每帧运行一次，剩下的是它的子函数
    def update(self, surf: Surface) -> None: ...

    # 在这里是update子函数（drop()的需求），并且在最后完成，在box和stone中独立于update
    def draw(self, surf: Surface) -> None: ...

    # 用户操作，empty_check()的子函数
    def user_work(self, events: list[Event]) -> None: ...

    def _get_three_one_direction(self, box_set: set[Box]): ...

    def _get_three_one(self, gx: int, gy: int, box: Box) -> None: ...

    def get_three(self) -> None: ...

    # 三消，在没有空box时调用，返回值为是否发生三消，empty_check的子函数
    def three_match(self) -> bool: ...
