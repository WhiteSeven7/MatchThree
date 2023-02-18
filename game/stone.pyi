from typing import Literal

from pygame import Surface

from tool.vector import Vect
from .box import Box
from .wall import Wall

StoneKind = Literal['gold', 'wood', 'water', 'fire', 'soil']


class Stone:
    # ”种类-图片“字典
    kind_image_dict: dict[StoneKind: Surface]
    # 容器
    wall: Wall
    box: Box
    # 位置，g_pos是在wall中位置，offset是下落偏移，pos是绘制位置
    g_pos: Vect
    offset: Vect
    pos: Vect
    # 类型
    kind: StoneKind
    # 图像
    image: Surface
    # 下落状态
    finish_fall: bool
    # 用于在用户交换后移动，值为移动方向
    moving: None | Vect

    # 初始化
    def __init__(self, wall: Wall, box: Box, gx: int, gy: int, kind: StoneKind): ...

    def __repr__(self) -> str: ...

    # 绘画
    def draw(self, surf: Surface) -> None: ...

    # update和它的子函数
    def _get_pos(self) -> Vect: ...

    def fall(self) -> None: ...

    def fall_recover(self) -> None: ...

    def move(self) -> None: ...

    def move_recover(self) -> None: ...
