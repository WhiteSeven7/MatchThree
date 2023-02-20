import pygame


def texts_draw(font, texts, anti_aliasing, font_color, bg_color=None):
    surfs = [font.render(text, anti_aliasing, font_color, bg_color) for text in texts]
    sum_height = sum(surf.get_height() for surf in surfs)
    max_width = max(surf.get_width() for surf in surfs)
    canvas = pygame.Surface((max_width, sum_height), pygame.SRCALPHA)
    # canvas.set_alpha(0)

    top = 0
    for surf in surfs:
        canvas.blit(surf, (0, top))
        top += surf.get_height()
    return canvas
