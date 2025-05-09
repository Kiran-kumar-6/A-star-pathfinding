import pygame

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = (255, 255, 255)  # WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == (255, 0, 0)  # RED

    def is_open(self):
        return self.color == (0, 255, 0)  # GREEN

    def is_barrier(self):
        return self.color == (0, 0, 0)  # BLACK

    def is_start(self):
        return self.color == (255, 165, 0)  # ORANGE

    def is_end(self):
        return self.color == (64, 224, 208)  # TURQUOISE

    def is_weight(self):
        return self.color == (180, 180, 180)  # WEIGHT

    def reset(self):
        self.color = (255, 255, 255)  # WHITE

    def make_start(self):
        self.color = (255, 165, 0)  # ORANGE

    def make_closed(self):
        self.color = (255, 0, 0)  # RED

    def make_open(self):
        self.color = (0, 255, 0)  # GREEN

    def make_barrier(self):
        self.color = (0, 0, 0)  # BLACK

    def make_end(self):
        self.color = (64, 224, 208)  # TURQUOISE

    def make_path(self):
        self.color = (128, 0, 128)  # PURPLE

    def make_weight(self):
        self.color = (180, 180, 180)  # WEIGHT

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # including diagonals
            new_row, new_col = self.row + dx, self.col + dy
            if 0 <= new_row < self.total_rows and 0 <= new_col < self.total_rows:
                neighbor = grid[new_row][new_col]
                if not neighbor.is_barrier():
                    self.neighbors.append(neighbor)

    def __lt__(self, other):
        return False 