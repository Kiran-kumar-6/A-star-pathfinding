import streamlit as st
import pygame
import numpy as np
from spot import Spot
from algorithm import algorithm

# Constants
WIDTH = 800
ROWS = 50
GAP = WIDTH // ROWS

# Colors
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def main():
    st.title("A* Path Finding Algorithm Visualization")
    
    # Initialize pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("A* Path Finding Algorithm")
    
    # Create grid
    grid = make_grid(ROWS, WIDTH)
    
    # Initialize variables
    start = None
    end = None
    
    # Streamlit controls
    st.sidebar.title("Controls")
    speed = st.sidebar.slider("Animation Speed", 0.001, 0.1, 0.01, 0.001)
    
    if st.sidebar.button("Clear Grid"):
        start = None
        end = None
        grid = make_grid(ROWS, WIDTH)
    
    # Main game loop
    run = True
    while run:
        draw(win, grid, ROWS, WIDTH)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                spot = grid[row][col]
                
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    spot.make_weight()
                elif spot != end and spot != start:
                    spot.make_barrier()
            
            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, WIDTH), grid, start, end, speed)
    
    pygame.quit()

if __name__ == "__main__":
    main() 