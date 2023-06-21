# hide welcome prompt from pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" 
import pygame
from common import *
from bfs import *
from GUI import *
from dfs import *
from gbfs import *
from astar import *
from bidirectional import *
from bidirectional_astar import *
# write function for command line operation. Input: search input.txt method where search is main file in exe, input.txt is the input file, method is the search algorithm
if (len(sys.argv) == 1):
        pass
else:
    #lower case sys.argv[2] to make it case insensitive
    sys.argv[2] = sys.argv[2].lower()
    if sys.argv[2] == "bfs":
        print(bfs(cell))
    elif sys.argv[2] == "dfs":
        print(dfs(cell))
    elif sys.argv[2] == "gbfs":
        print(greedy_best_first_search(cell))
    elif sys.argv[2] == "astar":
        print(astar(cell))
    elif sys.argv[2] == "cus1":
        print(bidirectional(cell))
    elif sys.argv[2] == "cus2":
        print(bidirectional_astar(cell))
    else:
        print("Invalid method")
    
pygame.init()
# set the width and height of the screen [width, height]
screen = pygame.display.set_mode((1400,700))
pygame.display.set_caption("Robot Navigation")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
search_algorithm = "BFS"

def text(string, size=50, color=WHITE):
    font = pygame.font.SysFont('arial', size)
    return font.render(string, True, color)

def draw_grid(WIN, grid):
    for row in grid:
        for node in row:
            node.draw_cell(WIN)
    pygame.display.update()
# write function to create grid and can reset it

# Create the grid
def create_grid():
    grid =[]
    for x in range(cell.w):
        row =[]
        for y in range(cell.h):
            cell_gui = CellGUI(x, y)
            row.append(cell_gui)
            if cell.grid[x][y] == 1:
                cell_gui.make_wall()
            elif cell.grid[x][y] == 2:
                cell_gui.make_start()
            elif cell.grid[x][y] == 3:
                cell_gui.make_goal()
        grid.append(row)
    return grid
# Assign the grid
grid = create_grid()
# Main program loop
while not done:
    # Limit to 60 frames per second
    # clock.tick(60)
    # Drawing grid 
    screen.fill(GREY)
    # Draw BFS button
    pygame.draw.rect(screen, BLACK, (1200, 0, 120, 60)) 
    screen.blit(text("BFS"), (1220,0))
    # Draw DFS button
    pygame.draw.rect(screen, BLACK, (1200, 100, 120, 60))
    screen.blit(text("DFS"), (1220,100))
    # Draw GBFS button
    pygame.draw.rect(screen, BLACK, (1200, 200, 120, 60))
    screen.blit(text("GBFS"), (1202,200))
    # Draw A* button
    pygame.draw.rect(screen, BLACK, (1200, 300, 120, 60))
    screen.blit(text("A*"), (1240,300))
    # Draw bidirection button
    pygame.draw.rect(screen, BLACK, (1150, 400, 240, 60))
    screen.blit(text("Bidirectional"), (1160,400))
    # Draw birectional A* button
    pygame.draw.rect(screen, BLACK, (1120, 500, 280, 60))
    screen.blit(text("Bidirectional A*"), (1120,500))
    # Draw reset button
    pygame.draw.rect(screen, BLACK, (1200, 600, 130, 60))
    screen.blit(text("Reset"), (1210,600))
    
    # update drawing the grid
    draw_grid(screen, grid)
    # End draw the grid
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # End draw interface
    # Game event takes place
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Game logic 
        if event.type == pygame.MOUSEBUTTONDOWN:
            # BFS button (1200, 0, 120, 60)
            if 1200 < mouse_x < 1320 and 0 < mouse_y < 60: 
                bfs(cell, draw_gui = (lambda: draw_grid(screen, grid), grid))
            # DFS button (1200, 100, 120, 60)
            if 1200 < mouse_x < 1320 and 100 < mouse_y < 160: 
                dfs(cell, draw_gui = (lambda: draw_grid(screen, grid), grid))
            # GBFS button (1200, 200, 120, 60)
            if 1200 < mouse_x < 1320 and 200 < mouse_y < 260:
                greedy_best_first_search(cell, draw_gui = (lambda: draw_grid(screen, grid), grid))
            # A* button (1200, 300, 120, 60)
            if 1200 < mouse_x < 1320 and 300 < mouse_y < 360: 
                astar(cell, draw_gui = (lambda: draw_grid(screen, grid), grid))
            # Bidirectional button (1150, 400, 240, 60)
            if 1150 < mouse_x < 1390 and 400 < mouse_y < 460: 
                bidirectional(cell, draw_gui = (lambda: draw_grid(screen, grid), grid))
            # Bidirectional A* button (1120, 500, 280, 60)
            if 1120 < mouse_x < 1400 and 500 < mouse_y < 560: 
                bidirectional_astar(cell, draw_gui = (lambda: draw_grid(screen, grid), grid))
            # reset button (1200, 600, 120, 60)
            if 1200 < mouse_x < 1320 and 600 < mouse_y < 660: 
                grid = create_grid()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
# Close the window and quit.
pygame.quit()





