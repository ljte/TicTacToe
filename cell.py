import pygame


class Cell:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.rect = pygame.Rect(x*width, y*height, width, height)
        self.value = None

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

        if self.value:
            font = pygame.font.SysFont('Consolas', 170)
            text = font.render(self.value, True, (0, 0, 0))
            pos = (self.rect.x + text.get_rect().width/2 - 10,
                   self.rect.y + 10)
            surface.blit(text, pos)

    def is_selected(self, mouse_pos: tuple):
        return self.rect.collidepoint(mouse_pos)

    @property
    def is_empty(self):
        return self.value is None

    def __repr__(self):
        return "<Cell object at @%s" % hex(id(self))
