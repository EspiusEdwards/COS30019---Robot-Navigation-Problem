#import the class Cell from cell.py
from cell import Cell
import ast
#read the input file RobotNav-test.txt and store the values in a list
def read_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    #remove \n
    lines = [line.strip() for line in lines] 
    # Take rows and columns from lines[0]
    # take first number of lines[0] as rows and second number as columns
    rows, columns = map(int, lines[0].strip("[]").split(","))
    cell = Cell(rows, columns)
    #cell.print_grid()
    # take first number of lines[1] as start point and second number as end point
    initial_x, initial_y = map(int,lines[1].strip("()").split(","))
    cell.initial_pos(initial_x, initial_y)
    # Take goal from lines[2] with strip |
    goals = lines[2].replace("|", "").split()
    goals = [ast.literal_eval(goal) for goal in goals]
    cell.set_goal(goals)
    for line in lines[3:]:
        wall_x, wall_y, wall_w, wall_h = map(int, line.strip("()").split(","))
        cell.set_wall(wall_x, wall_y, wall_w, wall_h)
    file.close()
    return cell, initial_x, initial_y, goals

