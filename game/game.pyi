from typing import NoReturn

import pygame

from .wall import Wall


class Game:
    screen: pygame.surface.Surface
    clock: pygame.time.Clock
    events: None | list[pygame.event.Event]
    wall: Wall

    def control(self) -> None | NoReturn: ...

    def run(self) -> NoReturn: ...
