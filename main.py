import pygame
import sys

from grid import Grid
import ai


def check_winner(board: list):
    # check rows
    for i in range(3):
        if board[i][0].value == board[i][1].value == board[i][2].value:
            return board[i][0].value

    # check columns
    for i in range(3):
        if board[0][i].value == board[1][i].value == board[2][i].value:
            return board[0][i].value

    # check diagonals
    if board[0][0].value == board[1][1].value == board[2][2].value:
        return board[0][0].value

    if board[0][2].value == board[1][1].value == board[2][0].value:
        return board[0][2].value

    """
     if none of the conditions above is true
     check if there are still empty cells left
     otherwise it's a tie.
    """
    for row in board:
        for cell in row:
            if cell.is_empty:
                return None

    return "Tie"


def main():
    # initial setup
    pygame.init()
    WIDTH, HEIGHT = 500, 550
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TicTacToe")
    click = False

    # grid.cells is basically a board
    grid = Grid(3, 3, 500, 500)
    winner = None
    font = pygame.font.SysFont('Consolas', 30)

    # mainloop
    while True:
        win.fill((255, 255, 255))
        grid.draw(win)
        # m - mouse => mx, my - mouse_x, mouse_y
        mx, my = pygame.mouse.get_pos()

        if click:
            if not winner and winner != "Tie" and my < 510:
                grid.cell_clicked((mx, my))
                winner = check_winner(grid.cells)
                if not winner:
                    # ai.make_simple_turn(grid)
                    ai.make_best_move(grid.cells)
                    winner = check_winner(grid.cells)

            if grid.restart_button_clicked((mx, my)):
                grid.restart()
                winner = None

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if winner:
            message = f"{winner} won" if winner in 'XO' else "It's a tie!"
            text = font.render(message, True, (0, 0, 0))
            win.blit(text, (20, 510))
        pygame.display.update()


if __name__ == "__main__":
    main()
