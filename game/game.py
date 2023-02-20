import sys

import pygame

from tool.filePath import get_path
from .dialog.dialog import Dialog
# from .wall.wall import Wall

FPS = 60
screen_size = (800, 800)

shape = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
]


class Game:

    def __init__(self):
        # 初始化
        pygame.init()
        # 主屏幕缓冲区
        self.screen = pygame.display.set_mode(screen_size)
        # 设置标题，图标
        pygame.display.set_caption("三消")
        pygame.display.set_icon(pygame.image.load(get_path(r'..\res\img\icon.png')))
        # 时钟，用于控制帧率
        self.clock = pygame.time.Clock()
        # self.wall = Wall(self, 100, 10, 70, shape, ['gold', 'wood', 'water', 'fire', 'soil'])
        self.dialog = Dialog(self, 100, 150, 600, 500, 20)
        self.events = None
        # 绘制第一帧
        pygame.display.flip()

    def control(self):
        for event in self.events:
            # 退出
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            # 在一帧内发生的事
            self.events = pygame.event.get()
            self.screen.fill('black')
            self.control()
            # self.wall.update(self.screen)
            self.dialog.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
