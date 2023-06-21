import pygame
from GUI import *
#import common.py
from common import *
# bfs to find path in cell from the initial point to goals use instruction and father dictionary
def bfs(cell, draw_gui = None):
    if draw_gui:
        draw_grid, grid = draw_gui     

    INSTRUCTION = {"up":(0, -1), "left":(-1, 0), "down":(0, 1), "right":(1, 0)}
    queue = []
    count_node = 1
    queue.append((initial_x, initial_y))
    father = [[None for y in range(cell.h)] for x in range(cell.w)]
    visit = [[False for y in range(cell.h)] for x in range(cell.w)]
    visit[initial_x][initial_y] = True
    while len(queue) > 0:
        current = queue.pop(0)
        if cell.grid[current[0]][current[1]] == 3:
            if draw_gui:
                return print_path(father, INSTRUCTION, (initial_x, initial_y), current, count_node, grid)
            else:
                return print_path(father, INSTRUCTION, (initial_x, initial_y), current, count_node)
        for instruction in INSTRUCTION:
            new_x = current[0] + INSTRUCTION[instruction][0]
            new_y = current[1] + INSTRUCTION[instruction][1]
            if 0 <= new_x < cell.w and 0 <= new_y < cell.h and cell.grid[new_x][new_y] != 1 and not visit[new_x][new_y]:
                queue.append((new_x, new_y))
                count_node += 1
                if draw_gui:
                    if(grid[new_x][new_y].color != GREEN and grid[new_x][new_y].color != RED):
                        grid[new_x][new_y].make_queue()
                visit[new_x][new_y] = True
                father[new_x][new_y] = instruction
        if draw_gui:
            if grid[current[0]][current[1]].color != GREEN and grid[current[0]][current[1]].color != RED:
                grid[current[0]][current[1]].make_visited()              
            draw_grid()
    return f"{sys.argv[1]} {sys.argv[2]} {count_node} \nNo solution found."

#print(bfs(cell))
