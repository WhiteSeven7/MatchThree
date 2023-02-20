from typing import NoReturn

import pygame

from .wall.wall import Wall
from .dialog.dialog import Dialog

class Game:
    screen: pygame.surface.Surface
    clock: pygame.time.Clock
    events: None | list[pygame.event.Event]
    wall: Wall
    dialog: Dialog

    def control(self) -> None | NoReturn: ...

    def run(self) -> NoReturn: ...
