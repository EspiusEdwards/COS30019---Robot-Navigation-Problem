#import common.py
from common import *
from queue import PriorityQueue

def Manhattan_distance(current,goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1]) 
def heuristic(current, goals):
    return min(Manhattan_distance(current, goal) for goal in goals)

def astar(cell, draw_gui = None):
    if draw_gui:
        draw_grid, grid = draw_gui
    count_node = 1
    INSTRUCTION = {"up":(0, -1), "left":(-1, 0), "down":(0, 1), "right":(1, 0)}
    frontier = PriorityQueue()
    frontier.put((0,count_node,(initial_x, initial_y)))
    father = [[None for y in range(cell.h)] for x in range(cell.w)]
    visit = [[False for y in range(cell.h)] for x in range(cell.w)]
    cost_so_far = {}
    cost_so_far[(initial_x, initial_y)] = 0
    
    while not frontier.empty():
        # get the second element of the tuple
        current = frontier.get()[2]
        visit[current[0]][current[1]] = True
        if cell.grid[current[0]][current[1]] == 3:
            if draw_gui:
                return print_path(father, INSTRUCTION, (initial_x, initial_y), current, count_node, grid)
            else:
                return print_path(father, INSTRUCTION, (initial_x, initial_y), current, count_node)
        for instruction in INSTRUCTION:
            new_x = current[0] + INSTRUCTION[instruction][0]
            new_y = current[1] + INSTRUCTION[instruction][1]
            if 0 <= new_x < cell.w and 0 <= new_y < cell.h and cell.grid[new_x][new_y] != 1 and not visit[new_x][new_y]:
                new_cost = cost_so_far[current] + 1
                if (new_x, new_y) not in cost_so_far or new_cost < cost_so_far[(new_x, new_y)]:
                    cost_so_far[(new_x, new_y)] = new_cost
                    priority = new_cost + heuristic((new_x, new_y), goals)
                    count_node += 1
                    frontier.put((priority, count_node, (new_x, new_y)))
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


    
    