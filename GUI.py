import pygame
#Constants 
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
GREY = (128,128,128)
LIGHTGREEN = (152, 251, 152)
LIGHTBLUE = (173,216,230)
YELLOW = (255,255,0)
class CellGUI:
    def __init__(self, x, y, width = 50, color = WHITE):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw_cell(self, screen):
        pygame.draw.rect(screen, self.color, [(50 * self.x), (50 * self.y), self.width, self.width], 0)
        pygame.draw.rect(screen, GREY, [(50 * self.x), (50 * self.y), self.width, self.width], width=2)  
    
    def make_start(self):
        self.color = RED
    def make_goal(self):
        self.color = GREEN
    def make_wall(self):
        self.color = BLACK
    def make_queue(self):
        pygame.time.delay(50)
        self.color = LIGHTGREEN
    def make_visited(self):
        pygame.time.delay(50)
        self.color = LIGHTBLUE
    def make_path(self):
        self.color = YELLOW
        
        



