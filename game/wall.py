from random import choice, randint

from tool.safeRemove import safe_remove
from tool.vector import Vect, DOWN
from .box import Box
from .stone import Stone


class Wall:
    box_kind_dict = {
        0: None,
        1: 'normal',
        2: 'generator'
    }

    # 通过self[..]对group进行管理
    def __getitem__(self, item):
        return self.group.get(item, None)

    def __setitem__(self, key, value):
        self.group[key] = value

    def __delitem__(self, key):
        del self.group[key]

    # group的迭代
    def __iter__(self):
        return iter(self.group)

    def keys(self):
        return self.group.keys()

    def values(self):
        return self.group.values()

    def items(self):
        return self.group.items()

    # 初始化
    def __init__(self, game, x, y, size, shape, selected_kinds):
        # 大框架
        self.game = game
        # 左上角的位置，用于绘制
        self.pos = Vect(x, y)
        # 单个空间的尺寸
        self.size = size
        # 设置group
        self._set_group(shape)
        # x, y方向的数量，用于有序迭代
        self.x_num = len(shape[0])
        self.y_num = len(shape)
        # 为wall的box填充stone
        self._generate(selected_kinds)
        # 若被改为真，则执行下落换位程序
        self.need_drop = False

    # 下面这些方法只在Wall实例化时运行，隶属于__init__的子函数
    def _set_group(self, shape):
        """设置group,x_num,y_num"""
        self.group = {}
        for gy, a_line in enumerate(shape):
            for gx, box_kind_id in enumerate(a_line):
                box_kind = self.box_kind_dict[box_kind_id]
                if box_kind is None:
                    continue
                self.group[Vect(gx, gy)] = Box(self, self.box_kind_dict[box_kind_id], gx, gy)

    def _generate(self, selected_kinds):
        """为wall的box填充stone"""
        for gy in range(self.y_num):
            for gx in range(self.x_num):
                if self[Vect(gx, gy)] and not randint(0, 4):
                    self._generate_one(gx, gy, selected_kinds)

    def _generate_one(self, gx, gy, se_kinds):
        box = self[Vect(gx, gy)]
        # 当这个box是generator时，不进行”防炸干涉”
        if box.kind == 'generator':
            box.content = Stone(self, box, gx, gy, choice(se_kinds))
            return
        # 当这个box是normal时，不进行”防炸干涉”
        left = self[Vect(gx - 1, gy)]
        left_2 = self[Vect(gx - 2, gy)]
        if left and left.content and left_2 and left_2.content and left.content.kind == left_2.content.kind:
            se_kinds = safe_remove(se_kinds, left.content.kind)
        up = self[Vect(gx, gy - 1)]
        up_2 = self[Vect(gx, gy - 2)]
        if up and up.content and up_2 and up_2.content and up.content.kind == up_2.content.kind:
            se_kinds = safe_remove(se_kinds, up.content.kind)
        # 如果原se_kinds中少于或等于2个元素，se_kinds可能为空list
        box.content = Stone(self, box, gx, gy, choice(se_kinds))

    # 在每帧运行一次
    def update(self, surf):
        self.empty_check()
        # 主迭代
        for box in self.values():
            box.update()
        # 若发生申请掉落
        if self.need_drop:
            self.drop()
        self.draw(surf)

    # 绘制，在这里是update子函数（drop()的需求），在box和stone中独立于update
    def draw(self, surf):
        for box in self.values():
            box.draw(surf)
        for box in self.values():
            if box.kind == 'normal' and box.content:
                box.content.draw(surf)

    # empty_check()的子函数
    def get_ups(self, empties):
        # 获得空box上方的所有stone
        return {
            self[Vect(box.g_pos.x, y)].content
            for box in empties
            for y in range(box.g_pos.y)
            if self[Vect(box.g_pos.x, y)].content
        }

    def empty_check(self):
        """用于开启stone.need_fall，应在主迭代前完成这个函数"""
        empties = [box for box in self.values() if box.content is None]
        empty_ups = self.get_ups(empties)
        for stone in empty_ups:
            stone.need_fall = True

    def drop(self):
        """掉落函数，可通过申请need_drop = True来使用"""
        # 将需要drop的stone提取出来
        dropped_stones = [
            box.content
            for box in self.values()
            if box.content and box.content.finish_fall
        ]
        # 将ds原本的box清空
        for ds in dropped_stones:
            self[ds.g_pos].content = None
            # 这一步中ds.g_pos.y += 1
            ds.fall_recover()
        # 将ds放入要进入的box，这两步不能合并，切记！
        for ds in dropped_stones:
            self[ds.g_pos].content = ds
        # 完成关闭
        self.need_drop = False
