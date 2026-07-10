import pygame
import settings

class Snake:
    def __init__(self):
        start_snake_x,start_snake_y = settings.START_SNAKE_POSITION

        self.body = [(start_snake_x - i , start_snake_y ) for i in range(settings.START_LENGTH)]

        self.snake_direction = (0,1)
        self.grow = False

    def get_head(self):
        return self.body[0]
    
    def draw(self,surface):
        dir_x, dir_y = self.snake_direction
        padding = settings.CELL_SIZE//6
        snake_size = settings.CELL_SIZE - (padding * 2)
        for i in self.body:
            if dir_x==1 or dir_x==-1:
                pixel_x = i[0] * settings.CELL_SIZE 
                pixel_y = i[1] * settings.CELL_SIZE + padding
                square = pygame.Rect(pixel_x,pixel_y,settings.CELL_SIZE,snake_size)
            elif dir_y==1 or dir_y==-1:
                pixel_x = i[0] * settings.CELL_SIZE + padding
                pixel_y = i[1] * settings.CELL_SIZE 
                square = pygame.Rect(pixel_x,pixel_y,snake_size,settings.CELL_SIZE)

            
            pygame.draw.rect(surface, settings.SNAKE_COLOR, square)

        head_x = self.body[0][0] * settings.CELL_SIZE
        head_y = self.body[0][1] * settings.CELL_SIZE
        eyes_radius = settings.CELL_SIZE // 6

        

        if dir_x ==1 : #right
            eye1 = (head_x + settings.CELL_SIZE - padding - eyes_radius, head_y + padding + eyes_radius)
            eye2 = (head_x + settings.CELL_SIZE - padding - eyes_radius, head_y + settings.CELL_SIZE - padding - eyes_radius)

            tongue_start = (head_x + settings.CELL_SIZE, head_y + settings.CELL_SIZE // 2)
            tongue_end = (head_x + settings.CELL_SIZE + settings.CELL_SIZE // 4, head_y + settings.CELL_SIZE // 2)

        elif dir_x == -1: # left
            eye1 = (head_x + padding + eyes_radius, head_y + padding + eyes_radius)
            eye2 = (head_x + padding + eyes_radius, head_y + settings.CELL_SIZE - padding - eyes_radius)
            tongue_start = (head_x, head_y + settings.CELL_SIZE // 2)
            tongue_end = (head_x - settings.CELL_SIZE // 4, head_y + settings.CELL_SIZE // 2)

        elif dir_y == 1: # down
            eye1 = (head_x + padding + eyes_radius, head_y + settings.CELL_SIZE - padding - eyes_radius)
            eye2 = (head_x + settings.CELL_SIZE - padding - eyes_radius, head_y + settings.CELL_SIZE - padding - eyes_radius)
            tongue_start = (head_x + settings.CELL_SIZE // 2, head_y + settings.CELL_SIZE)
            tongue_end = (head_x + settings.CELL_SIZE // 2, head_y + settings.CELL_SIZE + settings.CELL_SIZE // 4)

        elif dir_y == -1: # up
            eye1 = (head_x + padding + eyes_radius, head_y + padding + eyes_radius)
            eye2 = (head_x + settings.CELL_SIZE - padding - eyes_radius, head_y + padding + eyes_radius)
            tongue_start = (head_x + settings.CELL_SIZE // 2, head_y)
            tongue_end = (head_x + settings.CELL_SIZE // 2, head_y - settings.CELL_SIZE // 4)

            pygame.draw.circle(surface, (0, 0, 0), eye1, eyes_radius)
            pygame.draw.circle(surface, (0, 0, 0), eye2, eyes_radius)
            pygame.draw.line(surface, (255, 0, 0), tongue_start, tongue_end, 2)

    def move(self):
        head_x = self.body[0][0]
        head_y = self.body[0][1]

        dir_x, dir_y = self.snake_direction
        new_x = (head_x + dir_x)%settings.GRID_WIDTH
        new_y = (head_y + dir_y)%settings.GRID_HEIGHT
        new_head = (new_x,new_y)
        self.body.insert(0,new_head)
        

        if self.grow == True:
            self.grow = False
        else:
            self.body.pop()

        
