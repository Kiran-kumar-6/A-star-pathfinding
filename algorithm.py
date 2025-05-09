import math
import time
from queue import PriorityQueue
from spot import Spot

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def reconstruct_path(came_from, current, draw, start):
    while current in came_from:
        current = came_from[current]
        if not current.is_start():  # Don't change color if it's the start point
            current.make_path()
        draw()
    # Ensure start point is visible after path reconstruction
    start.make_start()
    draw()

def algorithm(draw, grid, start, end, speed=0.01):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw, start)  # Pass start point to reconstruct_path
            end.make_end()  # Ensure end point stays turquoise
            return True

        for neighbor in current.neighbors:
            dx = abs(neighbor.row - current.row)
            dy = abs(neighbor.col - current.col)
            move_cost = math.sqrt(2) if dx == 1 and dy == 1 else 1
            if neighbor.is_weight():
                move_cost *= 5

            temp_g_score = g_score[current] + move_cost

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    if not neighbor.is_start() and not neighbor.is_end():  # Don't change color if it's start or end
                        neighbor.make_open()

        draw()
        time.sleep(speed)

        if current != start and current != end:  # Don't change color if it's start or end
            current.make_closed()

    return False 