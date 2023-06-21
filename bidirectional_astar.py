#import common.py
from common import *
from queue import PriorityQueue

GOAL_INSTRUCTION = {"right":(-1, 0),"down":(0, -1),"left":(1, 0),"up":(0, 1)}
INSTRUCTION = {"up":(0, -1), "left":(-1, 0), "down":(0, 1), "right":(1, 0)}

sorted_goals = []
sorted_goals = sorted(goals, key=lambda x: (x[0], x[1]))

def Manhattan_distance(current,goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1]) 

def start_heuristic(current, sorted_goals):
    return min(Manhattan_distance(current, goal) for goal in sorted_goals)

def goal_heuristic(current, initial_pos):
    return Manhattan_distance(current, initial_pos)

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
        for goal in sorted_goals:
            if goal_trace == goal:
                running = False
    path = "; ".join(ans)
    return f"{sys.argv[1]} {sys.argv[2]} {count_node} \n{path};"

def bidirectional_astar(cell, draw_gui = None):
    
    if draw_gui:
        draw_grid, grid = draw_gui
    start_count_node = 1
    goal_count_node = 1
    #sorted_goals = sorted(sorted_goals, key = lambda x: (x[0], x[1]))
    start_frontier = PriorityQueue()
    goal_frontier = PriorityQueue()
    start_cost = [[float('inf') for y in range(cell.h)] for x in range(cell.w)]
    goal_cost = [[float('inf') for y in range(cell.h)] for x in range(cell.w)]
    min_value = float('inf')
    start_cost[initial_x][initial_y] = 0
    start_frontier.put((0, start_cost[initial_x][initial_y], (initial_x, initial_y)))
    for goal in sorted_goals:
        goal_cost[goal[0]][goal[1]] = 0
        goal_frontier.put((0, goal_cost[goal[0]][goal[1]], goal))

    start_father = [[None for y in range(cell.h)] for x in range(cell.w)]
    goal_father = [[None for y in range(cell.h)] for x in range(cell.w)]
    start_visit = [[False for y in range(cell.h)] for x in range(cell.w)]
    goal_visit = [[False for y in range(cell.h)] for x in range(cell.w)]
    start_cost_so_far = {}
    goal_cost_so_far = {}
    start_cost_so_far[(initial_x, initial_y)] = 0
    for goal in sorted_goals:
        goal_cost_so_far[goal] = 0
    intersection = False
    
    # start loop
    while intersection == False and not start_frontier.empty() and not goal_frontier.empty():
        start_current = start_frontier.get()[2]
        goal_current = goal_frontier.get()[2]
        start_visit[start_current[0]][start_current[1]] = True
        goal_visit[goal_current[0]][goal_current[1]] = True
        if (goal_visit[start_current[0]][start_current[1]]):
                    min_value = min(min_value, start_cost_so_far[start_current], goal_cost_so_far[goal_current])
                    intersection = start_current
        for start_instruction in INSTRUCTION:
            new_start_x = start_current[0] + INSTRUCTION[start_instruction][0]
            new_start_y = start_current[1] + INSTRUCTION[start_instruction][1]
            if 0 <= new_start_x < cell.w and 0 <= new_start_y < cell.h and cell.grid[new_start_x][new_start_y] != 1 and not start_visit[new_start_x][new_start_y]:
                start_new_cost = start_cost_so_far[start_current] + 1
                if (new_start_x, new_start_y) not in start_cost_so_far or start_new_cost < start_cost_so_far[(new_start_x)(new_start_y)]:
                    start_cost_so_far[(new_start_x), (new_start_y)] = start_new_cost
                    start_priority = start_new_cost + start_heuristic((new_start_x, new_start_y), sorted_goals)
                    start_count_node += 1
                    start_frontier.put((start_priority, start_count_node, (new_start_x, new_start_y)))
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
                goal_new_cost = goal_cost_so_far[goal_current] + 1
                if (new_goal_x, new_goal_y) not in goal_cost_so_far or goal_new_cost < goal_cost_so_far[(new_goal_x)(new_goal_y)]:
                    goal_cost_so_far[(new_goal_x), (new_goal_y)] = goal_new_cost
                    goal_priority = goal_new_cost + start_heuristic((new_goal_x, new_goal_y), sorted_goals)
                    goal_count_node += 1
                    goal_frontier.put((goal_priority, goal_count_node, (new_goal_x, new_goal_y)))
                    if draw_gui:
                        if(grid[new_goal_x][new_goal_y].color != GREEN and grid[new_goal_x][new_goal_y].color != RED):
                            grid[new_goal_x][new_goal_y].make_queue()
                    goal_visit[new_goal_x][new_goal_y] = True
                    goal_father[new_goal_x][new_goal_y] = instruction
                if (start_visit[goal_current[0]][goal_current[1]]):
                    min_value = min(min_value, start_cost_so_far[start_current], goal_cost_so_far[goal_current])
                    intersection = (goal_current[0], goal_current[1])
        if draw_gui:
            if grid[goal_current[0]][goal_current[1]].color != GREEN and grid[goal_current[0]][goal_current[1]].color != RED:
                grid[goal_current[0]][goal_current[1]].make_visited()
            draw_grid()
        if start_frontier.empty() or goal_frontier.empty():
            break
        if (min_value <= max(start_priority, goal_priority)):
            intersection = True
            if draw_gui:
                return print_bi_path(start_father, goal_father,(initial_x, initial_y), start_current, start_count_node + goal_count_node, grid)
            else:
                return print_bi_path(start_father, goal_father,(initial_x, initial_y), start_current, start_count_node + goal_count_node)
    return f"{sys.argv[1]} {sys.argv[2]} {start_count_node + goal_count_node} \nNo solution found."
#print(bidirectional(cell))