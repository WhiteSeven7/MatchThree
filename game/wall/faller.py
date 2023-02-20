from random import choice

from tool.vector import Vect
from .stone import Stone


class Faller:
    def __init__(self, wall, fm_cool):
        self.wall = wall
        # 若被改为真，则执行drop()函数
        self.need_drop = False
        # fall_match_time。有stone下落时始终为0，没有时会每帧+1，达到上限时才可以自动启动three_match()
        self.fm_time = fm_cool
        self.fm_cool = fm_cool

    def is_ready(self):
        return self.fm_time >= self.fm_cool

    def set_fall(self, empties):
        wall = self.wall
        # 让generator类型的box生成stone
        for box in empties:
            if box.kind == 'generator':
                box.contain(Stone(wall, box, box.g_pos.x, box.g_pos.y, choice(wall.stone_kinds)))
        # 算出所有需要fall的stone
        empty_ups = {
            wall[Vect(box.g_pos.x, y)].content
            for box in empties
            for y in range(box.g_pos.y)
            if wall[Vect(box.g_pos.x, y)].content
        }
        # 让这些stone掉落
        for stone in empty_ups:
            stone.fall()

    # 应在主迭代前完成这个函数
    def dynamic(self):
        """
        1. 获取所有空box
        2. 无空box时，进行三消
        3. 有空box时，开启stone.need_fall
        """
        wall = self.wall
        wall.mob.g_pos = None  # 先清空位置，使mob只在被赋值时可见
        if empties := [box for box in wall.values() if box.is_empty()]:
            # 有空box
            self.fm_time = 0
            self.set_fall(empties)
        else:
            if not self.is_ready():
                self.fm_time += 1
            if self.is_ready():
                if wall.three_match():
                    # 发生了三消，再次出现空box，重置empties
                    empties = [box for box in wall.values() if box.is_empty()]
                    self.fm_time = 0
                    self.set_fall(empties)
                else:
                    # 未发生了三消
                    wall.user_work(wall.game.events)

    # 应在主迭代后完成这个函数，并且需要need_drop为开启状态（即”条件启动“）
    def drop(self):
        """掉落函数，可通过申请need_drop = True来使用"""
        # 将需要drop的stone提取出来
        wall = self.wall
        dropped_stones = [
            box.content
            for box in wall.values()
            if box.content and box.content.finish_fall
        ]
        # 将ds原本的box清空
        for ds in dropped_stones:
            wall[ds.g_pos].clear()
            # 这一步中ds.g_pos.y += 1
            ds.fall_recover()
        # 将ds放入要进入的box，这两步不能合并，切记！
        for ds in dropped_stones:
            wall[ds.g_pos].contain(ds)
        # 完成关闭
        self.need_drop = False
