import pygame


class Border:
    """鼠标所在box的外围的白色方框"""

    def __init__(self, wall, color):
        self.wall = wall
        self.g_pos = None
        self.image = pygame.Surface((60, 60))
        self.image.fill(color)
        pygame.draw.rect(self.image, 'black', pygame.Rect(4, 4, 52, 52))
        self.image.set_colorkey('black')

    def right_pos(self):
        # 不能用bool(self.g_pos)，因为bool(Vect(0, 0)) 是 False
        return self.g_pos is not None

    def draw(self, surf):
        """在调用前确认self.g_pos不是None"""
        surf.blit(self.image, (self.wall.pos + self.g_pos * self.wall.size).tuple())
