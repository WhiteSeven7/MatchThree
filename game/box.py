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

    # 绘制函数
    def draw(self, surf):
        """一般的box都要画出来"""
        if self.kind != 'generator':
            surf.blit(self.image, self.pos.tuple())

    # update和它的子函数
    def update(self):
        if self.content:
            self.content.update()
