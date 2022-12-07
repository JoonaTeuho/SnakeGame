import pygame
import sys

# Ruudun määrittely
screen_width = 600
screen_height = 600

# Pelialueen määrittely
gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

# Suuntien määrittely
up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

class Snake():
    # Madon alustaminen
    def __init__(self):
        self.length = 1
        self.positions = [(300, 300)]
        self.direction = (0,0)
        self.color = (255, 255, 0)
        self.score = 0
        self.high_score = 0

    def get_head_position(self):
        return self.positions[0]

    # Kääntymisfunktio
    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    # Liikkumisfunktio
    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        elif new[0] == (x*gridsize)%screen_width:
            self.reset()
        elif new[1] == (y*gridsize)%screen_height:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    # Pelin (uudelleen) aloittaminen
    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = (0,0)

        #High scoren määrittely
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    # Madon luonti
    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)