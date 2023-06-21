#import cell
from cell import Cell
from GUI import *
#import read_file
from read_file import read_file
import sys

#read the input file RobotNav-test.txt and store the values in a list
# take input of python main.py input.txt method
# input.txt is the input file
# method is the search algorithm
if (len(sys.argv) != 1 ):
    cell, initial_x, initial_y, goals = read_file(sys.argv[1])
else:
    cell, initial_x, initial_y, goals = read_file("input.txt")
def print_path(father, instruction, initial_pos, end_pos, count_node, grid = None):
    trace = end_pos
    ans = []
    while trace != initial_pos:
        ans.insert(0, father[trace[0]][trace[1]])
        direction = instruction[father[trace[0]][trace[1]]]
        parent = (trace[0] - direction[0], trace[1] - direction[1])
        trace = parent
        if grid:
            if grid[trace[0]][trace[1]].color != GREEN and grid[trace[0]][trace[1]].color != RED:
                grid[trace[0]][trace[1]].make_path()
    path = "; ".join(ans)

    return f"{sys.argv[1]} {sys.argv[2]} {count_node} \n{path};"
