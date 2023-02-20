import pygame

from tool.vector import Vect


class Box:
    def __init__(self, wall, kind, gx, gy):
        # 容器
        self.wall = wall
        # 种类
        self.kind = kind
        # 位置，格点中，绘制位置
        self.g_pos = Vect(gx, gy)
        self.pos = self.wall.pos + self.g_pos * self.wall.size + Vect(4, 4)
        # stone或者none
        self.content = None
        # 半透明灰色方块
        self.image = pygame.Surface((52, 52))
        self.image.fill((63, 63, 63))
        self.image.set_alpha(127)
        # 记录在wall.three_match()中是否已在match组中
        self.match = None

    def __repr__(self):
        return f'Box({self.kind}, {self.g_pos}, {self.content})'

    # 下面六个为功能函数
    def is_empty(self):
        return not bool(self.content)

    def clear(self):
        self.content = None

    def contain(self, stone):
        self.content = stone

    def kind_is(self, kind):
        return self.kind == kind

    def can_crush(self):
        """ 常规box且有stone """
        return self.kind == 'normal' and self.content

    def same_stone_kind(self, box1, box2):
        """需确定box1,box2可用"""
        return self.content.kind == box1.content.kind == box2.content.kind

    # 绘制函数
    def draw(self, surf):
        """一般的box都要画出来"""
        if self.kind != 'generator':
            surf.blit(self.image, self.pos.tuple())
