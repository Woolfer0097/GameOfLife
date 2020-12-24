import pygame

BLACK = pygame.Color("black")
WHITE = pygame.Color("white")


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 15

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, WHITE, (self.cell_size * x + self.left,
                                                 self.top + self.cell_size * y,
                                                 self.cell_size, self.cell_size),
                                 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        return ((mouse_pos[0] - self.left) // self.cell_size,
                (mouse_pos[1] - self.top) // self.cell_size)

    def on_click(self, cell_coords):
        pass


if __name__ == '__main__':
    pygame.init()
    size = width, height = 620, 620
    screen = pygame.display.set_mode(size)
    board = Board(40, 40)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render()
        pygame.display.flip()