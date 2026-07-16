import pygame
import settings

class Snake:
    def __init__(self):
        start_snake_x,start_snake_y = settings.START_SNAKE_POSITION

        self.body = [(start_snake_x - i , start_snake_y ) for i in range(settings.START_LENGTH)]

        self.snake_direction = (0,0)
        self.grow = False
        self.end_of_game = False

    def get_head(self):
        return self.body[0]
    
    def draw(self, surface):
        
        dir_x, dir_y = self.snake_direction
        padding = settings.CELL_SIZE // 6
        radius = settings.CELL_SIZE // 2
        elongation = 5
        if dir_x == 0 and dir_y == 0:
            dir_x, dir_y = 1, 0

        
        for index, i in enumerate(self.body):
            pixel_x = i[0] * settings.CELL_SIZE
            pixel_y = i[1] * settings.CELL_SIZE

            
            if index == 0:
                continue
            elif index == len(self.body) - 1 and len(self.body) > 1:
                prev_segment = self.body[index - 1]
                tail_dir_x = prev_segment[0] - i[0]
                tail_dir_y = prev_segment[1] - i[1]
                tail_rect = pygame.Rect(pixel_x, pixel_y, settings.CELL_SIZE, settings.CELL_SIZE)

                if tail_dir_x == 1: 
                    pygame.draw.rect(surface, settings.SNAKE_COLOR, tail_rect, border_top_left_radius=radius, border_bottom_left_radius=radius)
                elif tail_dir_x == -1: 
                    pygame.draw.rect(surface, settings.SNAKE_COLOR, tail_rect, border_top_right_radius=radius, border_bottom_right_radius=radius)
                elif tail_dir_y == 1: 
                    pygame.draw.rect(surface, settings.SNAKE_COLOR, tail_rect, border_top_left_radius=radius, border_top_right_radius=radius)
                else: 
                    pygame.draw.rect(surface, settings.SNAKE_COLOR, tail_rect, border_bottom_left_radius=radius, border_bottom_right_radius=radius)
            else:
                prev_seg = self.body[index - 1]
                next_seg = self.body[index + 1]

               
                dx1 = prev_seg[0] - i[0]
                dy1 = prev_seg[1] - i[1]
                dx2 = next_seg[0] - i[0]
                dy2 = next_seg[1] - i[1]

                square = pygame.Rect(pixel_x, pixel_y, settings.CELL_SIZE, settings.CELL_SIZE)

                
                if (dx1 != 0 and dy2 != 0) or (dx2 != 0 and dy1 != 0):
                    
                    if (dx1 == -1 and dy2 == -1) or (dx2 == -1 and dy1 == -1):
                        pygame.draw.rect(surface, settings.SNAKE_COLOR, square, border_bottom_right_radius=radius)
                    elif (dx1 == 1 and dy2 == -1) or (dx2 == 1 and dy1 == -1):
                        pygame.draw.rect(surface, settings.SNAKE_COLOR, square, border_bottom_left_radius=radius)
                    elif (dx1 == -1 and dy2 == 1) or (dx2 == -1 and dy1 == 1):
                        pygame.draw.rect(surface, settings.SNAKE_COLOR, square, border_top_right_radius=radius)
                    elif (dx1 == 1 and dy2 == 1) or (dx2 == 1 and dy1 == 1):
                        pygame.draw.rect(surface, settings.SNAKE_COLOR, square, border_top_left_radius=radius)
                else:
                    
                    pygame.draw.rect(surface, settings.SNAKE_COLOR, square)


       
        head_x = self.body[0][0] * settings.CELL_SIZE
        head_y = self.body[0][1] * settings.CELL_SIZE

        if dir_x == 1: 
            head_rect = pygame.Rect(head_x, head_y, settings.CELL_SIZE + elongation, settings.CELL_SIZE)
            pygame.draw.rect(surface, settings.SNAKE_COLOR, head_rect, border_top_right_radius=radius, border_bottom_right_radius=radius)
        elif dir_x == -1: 
            head_rect = pygame.Rect(head_x - elongation, head_y, settings.CELL_SIZE + elongation, settings.CELL_SIZE)
            pygame.draw.rect(surface, settings.SNAKE_COLOR, head_rect, border_top_left_radius=radius, border_bottom_left_radius=radius)
        elif dir_y == 1: 
            head_rect = pygame.Rect(head_x, head_y, settings.CELL_SIZE, settings.CELL_SIZE + elongation)
            pygame.draw.rect(surface, settings.SNAKE_COLOR, head_rect, border_bottom_left_radius=radius, border_bottom_right_radius=radius)
        elif dir_y == -1: 
            head_rect = pygame.Rect(head_x, head_y - elongation, settings.CELL_SIZE, settings.CELL_SIZE + elongation)
            pygame.draw.rect(surface, settings.SNAKE_COLOR, head_rect, border_top_left_radius=radius, border_top_right_radius=radius)

        
        eyes_radius = settings.CELL_SIZE // 6
        
        if dir_x == 1: 
            eye1 = (head_x + settings.CELL_SIZE - padding - eyes_radius, head_y + padding + eyes_radius)
            eye2 = (head_x + settings.CELL_SIZE - padding - eyes_radius, head_y + settings.CELL_SIZE - padding - eyes_radius)
            tongue_start = (head_x + settings.CELL_SIZE + elongation, head_y + settings.CELL_SIZE // 2)
            tongue_end = (head_x + settings.CELL_SIZE + elongation + settings.CELL_SIZE // 4, head_y + settings.CELL_SIZE // 2)
        elif dir_x == -1: 
            eye1 = (head_x + padding + eyes_radius, head_y + padding + eyes_radius)
            eye2 = (head_x + padding + eyes_radius, head_y + settings.CELL_SIZE - padding - eyes_radius)
            tongue_start = (head_x - elongation, head_y + settings.CELL_SIZE // 2)
            tongue_end = (head_x - elongation - settings.CELL_SIZE // 4, head_y + settings.CELL_SIZE // 2)
        elif dir_y == 1: 
            eye1 = (head_x + padding + eyes_radius, head_y + settings.CELL_SIZE - padding - eyes_radius)
            eye2 = (head_x + settings.CELL_SIZE - padding - eyes_radius, head_y + settings.CELL_SIZE - padding - eyes_radius)
            tongue_start = (head_x + settings.CELL_SIZE // 2, head_y + settings.CELL_SIZE + elongation)
            tongue_end = (head_x + settings.CELL_SIZE // 2, head_y + settings.CELL_SIZE + elongation + settings.CELL_SIZE // 4)
        elif dir_y == -1: 
            eye1 = (head_x + padding + eyes_radius, head_y + padding + eyes_radius)
            eye2 = (head_x + settings.CELL_SIZE - padding - eyes_radius, head_y + padding + eyes_radius)
            tongue_start = (head_x + settings.CELL_SIZE // 2, head_y - elongation)
            tongue_end = (head_x + settings.CELL_SIZE // 2, head_y - elongation - settings.CELL_SIZE // 4)

        pygame.draw.circle(surface, (0, 0, 0), eye1, eyes_radius)
        pygame.draw.circle(surface, (0, 0, 0), eye2, eyes_radius)
        pygame.draw.line(surface, (255, 0, 0), tongue_start, tongue_end, 2)

    def move(self):
        head_x = self.body[0][0]
        head_y = self.body[0][1]

        dir_x, dir_y = self.snake_direction
        new_x = (head_x + dir_x)
        new_y = (head_y + dir_y)
        new_head = (new_x,new_y)
        self.body.insert(0,new_head)
        

        if self.grow == True:
            self.grow = False
        else:
            self.body.pop()
            
            
        if not (1<=new_head[0]<settings.GRID_WIDTH-1) or not (2<=new_head[1]<settings.GRID_HEIGHT-1):
            self.end_of_game = True
            
            
        for i in self.body[1:]:
            if i == new_head:
                self.end_of_game = True 
                break
            
            
    def change_direction(self,new_dir_x,new_dir_y):
        head_x,head_y = self.body[0]
        neck_x,neck_y = self.body[1]
        found_side_x = neck_x - head_x
        found_side_y = neck_y - head_y
        if (new_dir_x,new_dir_y ) != (found_side_x,found_side_y):
            self.snake_direction = (new_dir_x,new_dir_y)  
        
        

        
