"""
    用于pygame的Surface对象和PIL的Image对象的相互转换
"""
from typing import Literal

from PIL.Image import Image
from pygame.surface import Surface

ColorMode = Literal["1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr"]
color_mode: dict[int, ColorMode]


def image_to_surface(image: Image) -> Surface: ...


def surface_to_image(surface: Surface) -> Image: ...
