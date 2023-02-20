"""
    用于pygame的Surface对象和PIL的Image对象的相互转换
"""
import pygame
from PIL import Image

color_mode = {
    3: 'RGB',
    4: 'RGBA',
    1: 'P'
}


def image_to_surface(image):
    """将Pillow Image转换为Pygame Surface对象"""
    return pygame.image.fromstring(image.tobytes(), image.size, 'RGBA')


def surface_to_image(surface):
    """将Pygame Surface转换为Pillow Image对象"""
    mode = color_mode[surface.get_bytesize()]
    return Image.frombytes(mode, surface.get_size(), pygame.image.tostring(surface, mode))
