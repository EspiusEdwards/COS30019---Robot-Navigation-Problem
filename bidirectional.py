#import common.py
from common import *
# bfs to find path in cell from the initial point to goals use instruction and father dictionary
GOAL_INSTRUCTION = {"right":(-1, 0),"down":(0, -1),"left":(1, 0),"up":(0, 1)}
INSTRUCTION = {"up":(0, -1), "left":(-1, 0), "down":(0, 1), "right":(1, 0)}
def print_bi_path(start_father, goal_father, initial_pos, intersection, count_node, grid = None):
    goal_trace = intersection
    start_trace = intersection
    ans = []
    running = True
    while start_trace != initial_pos:
        ans.insert(0, start_father[start_trace[0]][start_trace[1]])
        start_direction = INSTRUCTION[start_father[start_trace[0]][start_trace[1]]]
        parent = (start_trace[0] - start_direction[0], start_trace[1] - start_direction[1])
        start_trace = parent
        if grid:
            if grid[start_trace[0]][start_trace[1]].color != GREEN and grid[start_trace[0]][start_trace[1]].color != RED:
                grid[start_trace[0]][start_trace[1]].make_path()
    while running:
        ans.append(goal_father[goal_trace[0]][goal_trace[1]])
        goal_direction = GOAL_INSTRUCTION[goal_father[goal_trace[0]][goal_trace[1]]]
        parent = (goal_trace[0] - goal_direction[0], goal_trace[1] - goal_direction[1])
        goal_trace = parent
        if grid:
            if grid[goal_trace[0]][goal_trace[1]].color != GREEN and grid[goal_trace[0]][goal_trace[1]].color != RED:
                grid[goal_trace[0]][goal_trace[1]].make_path()
                grid[intersection[0]][intersection[1]].make_path()
        for goal in goals:
            if goal_trace == goal:
                running = False
    path = "; ".join(ans)
    return f"{sys.argv[1]} {sys.argv[2]} {count_node} \n{path};"
def bidirectional(cell, draw_gui = None):
    if draw_gui:
        draw_grid, grid = draw_gui
    start_father = [[None for y in range(cell.h)] for x in range(cell.w)]
    goal_father = [[None for y in range(cell.h)] for x in range(cell.w)]
    start_queue = []
    start_queue.append((initial_x, initial_y))
    start_visit = [[False for y in range(cell.h)] for x in range(cell.w)]
    start_visit[initial_x][initial_y] = True  
    goal_queue = []
    count_node = 1
    for goal in goals:
        goal_queue.append(goal)
    goal_visit = [[False for y in range(cell.h)] for x in range(cell.w)]
    for goal in goals:
        goal_visit[goal[0]][goal[1]] = True
    intersection = False
    
    while intersection == False and len(start_queue) != 0 and len(goal_queue) != 0:
        start_current = start_queue.pop(0)
        goal_current = goal_queue.pop(0)
        if (goal_visit[start_current[0]][start_current[1]]):
            intersection = True
            if draw_gui:
                return print_bi_path(start_father, goal_father,(initial_x, initial_y), start_current, count_node, grid)
            else:
                return print_bi_path(start_father, goal_father,(initial_x, initial_y), start_current, count_node)
        if (start_visit[goal_current[0]][goal_current[1]]):
            intersection = True
            if draw_gui:
                return print_bi_path(start_father, goal_father, (initial_x, initial_y), goal_current, count_node, grid)
            else:
                return print_bi_path(start_father, goal_father, (initial_x, initial_y), goal_current, count_node)
        for start_instruction in INSTRUCTION:
            new_start_x = start_current[0] + INSTRUCTION[start_instruction][0]
            new_start_y = start_current[1] + INSTRUCTION[start_instruction][1]
            if 0 <= new_start_x < cell.w and 0 <= new_start_y < cell.h and cell.grid[new_start_x][new_start_y] != 1 and not start_visit[new_start_x][new_start_y]:
                start_queue.append((new_start_x, new_start_y))
                count_node += 1
                if draw_gui:
                    if(grid[new_start_x][new_start_y].color != GREEN and grid[new_start_x][new_start_y].color != RED):
                        grid[new_start_x][new_start_y].make_queue()
                start_visit[new_start_x][new_start_y] = True
                start_father[new_start_x][new_start_y] = start_instruction
        if draw_gui:
            if grid[start_current[0]][start_current[1]].color != GREEN and grid[start_current[0]][start_current[1]].color != RED:
                grid[start_current[0]][start_current[1]].make_visited()
        for instruction in GOAL_INSTRUCTION:
            new_goal_x = goal_current[0] + GOAL_INSTRUCTION[instruction][0]
            new_goal_y = goal_current[1] + GOAL_INSTRUCTION[instruction][1]
            if 0 <= new_goal_x < cell.w and 0 <= new_goal_y < cell.h and cell.grid[new_goal_x][new_goal_y] != 1 and not goal_visit[new_goal_x][new_goal_y]:
                goal_queue.append((new_goal_x, new_goal_y))
                count_node += 1
                goal_visit[new_goal_x][new_goal_y] = True
                goal_father[new_goal_x][new_goal_y] = instruction
        if draw_gui:
            if grid[goal_current[0]][goal_current[1]].color != GREEN and grid[goal_current[0]][goal_current[1]].color != RED:
                grid[goal_current[0]][goal_current[1]].make_visited()
            draw_grid()
    return f"{sys.argv[1]} {sys.argv[2]} {count_node} \nNo solution found."
#print(bidirectional(cell))