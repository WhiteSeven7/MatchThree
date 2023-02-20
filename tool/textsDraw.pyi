from pygame.font import Font
from pygame.surface import Surface

Color = str | tuple[int, int, int] | tuple[int, int, int, int]


def texts_draw(
        font: Font,
        texts: list[str],
        anti_aliasing: bool,
        font_color: Color,
        bg_color: None | Color = None
) -> Surface: ...
