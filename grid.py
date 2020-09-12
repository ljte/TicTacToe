import pygame

from cell import Cell


class Grid:
    def __init__(self, nrows, ncols, width, height):
        self.nrows = nrows
        self.ncols = ncols
        self.width = width
        self.height = height
        self.cells = [[Cell(j, i, width / ncols, height / nrows)
                       for j in range(ncols)] for i in range(nrows)]
        font = pygame.font.SysFont('Consolas', 30)
        self.restart_btn = font.render('Restart', True, (0, 0, 0))

    def draw(self, surface: pygame.Surface):
        # draw cells
        for row in self.cells:
            for cell in row:
                cell.draw(surface)

        # draw grid lines
        gap = self.width / self.ncols
        for i in range(self.ncols + 1):
            pygame.draw.line(surface, (0, 0, 0), (i * gap, 0),
                             (i * gap, self.height), 2)
            pygame.draw.line(surface, (0, 0, 0), (0, i * gap),
                             (self.width, i * gap), 2)

        # draw 'restart' text in the left bottom corner
        surface.blit(self.restart_btn, (360, 510))

    def cell_clicked(self, mouse_pos: tuple):
        for row in self.cells:
            for cell in row:
                if cell.is_selected(mouse_pos):
                    cell.value = "X"

    def get_empty_cell(self):
        for row in self.cells:
            for cell in row:
                if cell.is_empty:
                    return cell
        return None

    def restart(self):
        for row in self.cells:
            for cell in row:
                cell.value = None

    def restart_button_clicked(self, mouse_pos):
        center = (360 + self.restart_btn.get_rect().width/2,
                  510 + self.restart_btn.get_rect().height/2)
        rect = self.restart_btn.get_rect(center=center)
        if rect.collidepoint(mouse_pos):
            return True
        return False
