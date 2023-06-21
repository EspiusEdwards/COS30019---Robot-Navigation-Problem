class Cell:
    def __init__(self, h, w):
        self.w = w
        self.h = h
        self.visited = False
        #self.parent = None
        #self.wall = False
        self.grid = [[0 for y in range(self.h)] for x in range(self.w)]
        self.goal = False
    def initial_pos(self, x, y):
        self.grid[x][y] = 2
        return (x,y)
    def print_grid(self):
        for y in range(self.h):
            for x in range(self.w):
                print(self.grid[x][y], end=" ")
            print()
    def set_wall(self, wall_x, wall_y, wall_w, wall_h):
        for y in range(wall_y, wall_y + wall_h):
            for x in range(wall_x, wall_x + wall_w):
                if x >= 0 and x < self.w and y >= 0 and y < self.h:
                    self.grid[x][y] = 1
    def set_goal(self, goals):
        for goal in goals:
            x, y = goal
            self.grid[x][y] = 3

