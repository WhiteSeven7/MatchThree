import pygame

from tool.filePath import *
from tool.vector import Vect


class Stone:
    # ”种类-图片“字典
    kind_image_dict = {
        'gold': pygame.image.load(get_path(r'..\..\res\img\stone\gold.png')),
        'wood': pygame.image.load(get_path(r'..\..\res\img\stone\wood.png')),
        'water': pygame.image.load(get_path(r'..\..\res\img\stone\water.png')),
        'fire': pygame.image.load(get_path(r'..\..\res\img\stone\fire.png')),
        'soil': pygame.image.load(get_path(r'..\..\res\img\stone\soil.png'))
    }

    def __init__(self, wall, box, gx, gy, kind):
        # 容器
        self.wall = wall
        self.box = box
        # 位置，g_pos是在wall中位置，offset是下落偏移，pos是绘制位置
        self.g_pos = Vect(gx, gy)
        self.offset = Vect(0, 0)
        self.pos = self._get_pos()
        # 类型
        self.kind = kind
        # 图像
        self.image = self.kind_image_dict[self.kind]
        # 在完成掉落时改为真，wall的fall()函数会通过此来识别哪些stone需要落入下一格
        self.finish_fall = False
        # 用于在用户交换后移动，值为移动方向
        self.moving = None

    def __repr__(self):
        return f'Stone({self.kind}, {self.g_pos}, {self.offset})'

    # 下面一个是功能函数
    def kind_is(self, kind):
        return self.kind == kind

    def draw(self, surf):
        self.pos = self._get_pos()
        surf.blit(self.image, self.pos.tuple())

    # update和它的子函数
    def _get_pos(self):
        # wall的位置 + 格子左上角的位置 + 格子内部的偏移Vect(5, 5) + 下落偏移Vect(0, 0) Vect(wall.size, 0)
        return self.wall.pos + self.wall.size * self.g_pos + Vect(5, 5) + self.offset

    def fall(self):
        """下落"""
        self.offset.y += 2
        if self.offset.y < self.wall.size:
            return
        # 更改wall.need_drop，申请wall.drop()，由wall.drop()关闭，为防止数据混乱，需要此次的wall.update()的迭代部分先完成
        self.wall.faller.need_drop = True
        # 作为自己需要drop的标志，由wall.drop()识别，由wall.drop()调用的stone.fall_recover()关闭
        self.finish_fall = True

    # 由wall.drop()内部调用
    def fall_recover(self):
        self.offset = Vect(0, 0)
        self.g_pos.y += 1
        self.finish_fall = False

    def move(self):
        """在此之前先检验self.moving是否为None"""
        self.offset += 2 * self.moving
        if self.offset.half_max() < self.wall.size:
            return
        self.wall.mover.need_exchange = True

    def move_recover(self):
        self.g_pos += self.moving
        self.moving = None
        self.offset = Vect(0, 0)
