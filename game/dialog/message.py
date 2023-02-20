import pygame

from tool.filePath import get_path
from tool.textsDraw import texts_draw
from tool.warpText import wrap_text


class Message:
    pygame.font.init()
    fonts = {
        'myself': pygame.font.Font(get_path(r'..\..\res\font\DeYiHei\SmileySans-Oblique-2.ttf'), 30),
        'shifu': pygame.font.Font(r'C:\Windows\Fonts\FZSTK.TTF', 30)
    }

    def __init__(self, dialog, sender, text, top):
        self.dialog = dialog
        self.font_color = 'white'
        self.bg_color = 'red' if self.sender_eq(sender, 'myself') else 'blue'
        # 让字不贴着边
        self.border = 5
        self.image = texts_draw(
            self.fonts[sender], wrap_text(text, self.fonts[sender], dialog.width * 2 // 3), True, self.font_color
        )
        self.rect = self.image.get_rect().inflate(2 * self.border, 2 * self.border)
        if self.sender_eq(sender, 'myself'):
            self.rect.topleft = (dialog.width - 17 - self.width(), top)
            # 17 / 10 ~= 3 ** 0.5
            self.points = self._triangle_points(17, 10, 0, top, self.height() // 2, dialog.width)
        else:
            self.rect.topleft = (17, top)
            self.points = self._triangle_points(17, 10, 0, top, self.height() // 2)
        print(self.image.get_size(), self.rect.size)
        # pos是文字的左上角
        self.pos = (self.rect.left + self.border, self.rect.top + self.border)

    def height(self):
        return self.rect.height

    def width(self):
        return self.rect.width

    @staticmethod
    def sender_eq(sender, string):
        return sender == string

    def draw(self, surf):
        pygame.draw.polygon(surf, self.bg_color, self.points)
        pygame.draw.rect(surf, self.bg_color, self.rect, border_radius=6)
        surf.blit(self.image, self.pos)

    @staticmethod
    def _triangle_points(x_dim, y_dim, x, y, offset, width=None):
        return (
            (x, y + offset),
            (x + x_dim, y + offset + y_dim),
            (x + x_dim, y + offset - y_dim)
        ) if width is None else (
            (width - x, y + offset),
            (width - x - x_dim, y + offset + y_dim),
            (width - x - x_dim, y + offset - y_dim)
        )
