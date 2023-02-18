from random import choice

import pygame

from tool.safeRemove import safe_remove
from tool.vector import Vect, LOZENGE
from .border import Border
from .box import Box
from .faller import Faller
from .mover import Mover
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
        self.group = self._set_group(shape)
        # x, y方向的数量，用于有序迭代
        self.x_num = len(shape[0])
        self.y_num = len(shape)
        # 记录能产生的Stone类型
        self.stone_kinds = selected_kinds
        # 为wall的box填充stone
        self._generate(selected_kinds)
        # 进行下落和user_work、three_match的工作
        self.faller = Faller(self, 30)
        # 鼠标所在的box位置，mouse_on_border
        self.mob = Border(self, (223, 223, 223))
        # 被选中的位置，边框
        self.clicked = Border(self, (218, 112, 214))
        # 进行移动的相关操作
        self.mover = Mover(self)
        # 储存get_three的结果，减少重复调用
        self.three_list = None

    # 下面这些方法只在Wall实例化时运行，隶属于__init__的子函数
    def _set_group(self, shape):
        """设置group,x_num,y_num"""
        return {
            Vect(gx, gy): Box(self, self.box_kind_dict[box_kind_id], gx, gy)
            for gy, a_line in enumerate(shape)
            for gx, box_kind_id in enumerate(a_line)
            if self.box_kind_dict[box_kind_id]
        }

    def _generate(self, selected_kinds):
        """为wall的box填充stone"""
        for gy in range(self.y_num):
            for gx in range(self.x_num):
                if self[Vect(gx, gy)]:
                    self._generate_one(gx, gy, selected_kinds)

    def _generate_one(self, gx, gy, se_kinds):
        box = self[Vect(gx, gy)]
        # 当这个box是generator时，不进行”防炸干涉”
        if box.kind == 'generator':
            box.contain(Stone(self, box, gx, gy, choice(se_kinds)))
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
        box.contain(Stone(self, box, gx, gy, choice(se_kinds)))

    # 在每帧运行一次
    def update(self, surf):
        if self.mover.check_stones:
            self.mover.check_exchange()
        # 主迭代
        self.faller.dynamic()
        self.mover.stone_move()
        # 若发生申请掉落
        if self.faller.need_drop:
            self.faller.drop()
        if self.mover.need_exchange:
            self.mover.exchange()
        # 绘制
        self.draw(surf)
        # 一些恢复
        self.three_list = None

    # 在这里是update子函数（drop()的需求），并且在最后完成，在box和stone中独立于update
    def draw(self, surf):
        for box in self.values():
            box.draw(surf)
        for box in self.values():
            if box.kind == 'normal' and box.content:
                box.content.draw(surf)
        if self.mob.right_pos():
            self.mob.draw(surf)
        if self.clicked.right_pos():
            self.clicked.draw(surf)

    def user_work(self, events):
        if self.mover.moving_stones:
            return
        g_pos = (Vect.fse(pygame.mouse.get_pos()) - self.pos) // self.size
        # 如果这个位置有box
        if self.faller.is_ready() and self[g_pos] and self[g_pos].kind != 'generator':
            self.mob.g_pos = g_pos
        for event in events:
            if event.type != pygame.MOUSEBUTTONDOWN:
                continue
            g_pos = (Vect.fse(event.dict['pos']) - self.pos) // self.size
            if not self[g_pos]:
                continue
            # 用户点击了有效的位置
            clicked = self.clicked
            if clicked.g_pos is None:
                clicked.g_pos = g_pos
                continue
            # 用户之前点过了位置
            direction = g_pos - clicked.g_pos
            if g_pos == clicked.g_pos:
                clicked.g_pos = None
            elif direction in LOZENGE:
                self.mover.set_moving(self[g_pos].content, self[clicked.g_pos].content, 'swap', direction)
                clicked.g_pos = None
            else:
                clicked.g_pos = g_pos

    def _get_three_one_direction(self, box_set):
        # 是否为一个新的set而不是 box_set 中已有的set，在下面第一个循环中判断
        new_set: bool = True
        # 判断box_set中元素有没有已有match的
        for r_box in box_set:
            if not r_box.match:
                continue
            r_box.match.update(box_set)
            box_set = r_box.match
            new_set = False
            break
        # 设置box_set中元素的match
        for r_box in box_set:
            r_box.match = box_set
        # 若为新的set，则加入all_three
        if new_set:
            self.three_list.append(box_set)

    # get_three()的子函数
    def _get_three_one(self, gx, gy, box):
        # 该循环只有两个，过于浪费，故不采用
        # for b_1, b_2 in (
        #         (self[Vect(gx + 1, gy)], self[Vect(gx + 2, gy)]),
        #         (self[Vect(gx, gy + 1)], self[Vect(gx, gy + 2)])
        # ):
        #     if b_1 and b_1.content and b_2 and b_2.content \
        #             and box.content.kind == b_1.content.kind == b_2.content.kind:
        #         self._get_three_one_direction({box, b_1, b_2}, all_three)

        # 右一和右二的box
        r, r2 = self[Vect(gx + 1, gy)], self[Vect(gx + 2, gy)]
        if r and r.can_crush() and r2 and r2.can_crush() and box.same_stone_kind(r, r2):
            self._get_three_one_direction({box, r, r2})
        # 下一和下二的box
        d, d2 = self[Vect(gx, gy + 1)], self[Vect(gx, gy + 2)]
        if d and d.can_crush() and d2 and d2.can_crush() and box.same_stone_kind(d, d2):
            self._get_three_one_direction({box, d, d2})

    # 得到可以三消的list[set[Box]]
    def get_three(self):
        if self.three_list:
            return
        self.three_list = []
        for gx in range(self.x_num):
            for gy in range(self.y_num):
                box = self[Vect(gx, gy)]
                if not (box and box.content and box.kind == 'normal'):
                    continue
                self._get_three_one(gx, gy, box)

    # 三消，在没有空box时调用，返回值为是否发生三消，dynamic()的子函数
    def three_match(self):
        self.get_three()
        if not self.three_list:
            return False
        for box_set in self.three_list:
            for box in box_set:
                box.clear()
                box.match = None
        return True
