import pygame

from tool.vector import Vect
from .message import Message


class Dialog:
    def __init__(self, game, x, y, width, height, gap):
        self.game = game
        self.surf = pygame.Surface((width, height))
        self.surf.fill('green')
        self.pos = Vect(x, y)
        self.width = width
        self.height = height
        self.gap = gap
        self._messages = []
        # 记录下一个添加的message的top
        self._now_y = gap // 2

        self.add('myself', '你好！')
        self.add('shifu', '再见。')
        self.add('shifu', '再\n见的册而得救出么化粪池再\n见的册而得救出么化粪池羽绒服三。')

    def add(self, sender, text):
        message = Message(self, sender, text, self._now_y)
        self._messages.append(message)
        self._now_y += message.height() + self.gap

    def draw(self, surf):
        self.surf.fill('green')
        for message in self._messages:
            message.draw(self.surf)
        surf.blit(self.surf, self.pos.tuple())
