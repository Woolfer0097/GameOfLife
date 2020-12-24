import pygame
from copy import deepcopy
from GameOfLife.board import Board

GREEN = pygame.Color("green")
BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
FPS = 10


class Life(Board):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * (width + 1) for _ in range(height + 1)]
        self.matrix = []
        self.left = 10
        self.top = 10
        self.cell_size = 15

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y] == 1:
                    pygame.draw.rect(screen, GREEN, (self.cell_size * x + self.left,
                                                     self.top + self.cell_size * y,
                                                     self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(screen, WHITE, (self.cell_size * x + self.left,
                                                     self.top + self.cell_size * y,
                                                     self.cell_size, self.cell_size),
                                     1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        content = self.board[cell[0]][cell[1]]
        if content == 0:
            self.board[cell[0]][cell[1]] = 1
        else:
            self.board[cell[0]][cell[1]] = 0
        self.on_click(cell)

    def get_neighbours(self, x, y):
        m = self.board
        first, second, third, \
            fourth, sixth, \
            seventh, eighth, nineth = \
            m[x - 1][y - 1], m[x][y - 1], \
            m[x + 1][y - 1], m[x - 1][y], \
            m[x + 1][y], \
            m[x - 1][y + 1], m[x][y + 1], \
            m[x + 1][y + 1]
        neighbours = [first, second, third, fourth,
                      sixth, seventh, eighth, nineth]
        return neighbours

    def next_move(self):
        self.matrix = deepcopy(self.board)
        for j in range(self.height):
            for i in range(self.width):
                neighbours = self.get_neighbours(i, j)
                count = neighbours.count(1)
                if self.board[i][j] == 0:
                    if count == 3:
                        self.matrix[i][j] = 1
                else:
                    if count == 3 or count == 2:
                        self.matrix[i][j] = 1
                    else:
                        self.matrix[i][j] = 0
        self.board = self.matrix


if __name__ == '__main__':
    pygame.init()
    size = w, h = 620, 620
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Игра «Жизнь»")
    clock = pygame.time.Clock()
    board = Life(40, 40)
    pressed = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not pressed:
                    board.get_click(event.pos)
                if event.button == 3:
                    if not pressed:
                        pressed = True
                    else:
                        pressed = False
                if event.button == 4:
                    FPS += 1
                if event.button == 5:
                    if FPS - 1 > 0:
                        FPS -= 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not pressed:
                        pressed = True
                    else:
                        pressed = False
        if pressed:
            board.next_move()
        screen.fill(BLACK)
        board.render()
        pygame.display.flip()
        clock.tick(FPS)
