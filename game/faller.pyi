from .box import Box
from .wall import Wall


class Faller:
    wall: Wall
    # 若被改为真，则执行下落换位程序
    need_drop: bool
    # fall_match_time，有stone下落时始终为0，没有时会每帧+1（达到60时不增），达到60时才可以自动启动three_match()
    fm_time: int
    fm_cool: int

    def __init__(self, wall: Wall, fm_cool: int): ...

    def is_ready(self) -> bool: ...

    # empty_check()的子函数
    def set_fall(self, empties: list[Box]) -> None: ...

    # 应在主迭代前完成这个函数
    def dynamic(self) -> None: ...

    # 应在主迭代后完成这个函数，并且需要need_drop为开启状态（即”条件启动“）
    def drop(self) -> None: ...
