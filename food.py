import pygame
import random
import settings
class Food:
    def __init__(self,snake_body):
        self.position = self.generate_random_position(snake_body)
    def generate_random_position(self,snake_body):
        free_points = []
        for x in range(1,settings.GRID_WIDTH-1):
            for y in range(2,settings.GRID_HEIGHT-1):
                if (x,y) not in snake_body:
                    free_points.append((x,y))
        if not free_points:
            return None
        return random.choice(free_points)

    def draw(self,surface, apple_img):
        
        if self.position is None:
            return
        pixel_x = self.position[0] * settings.CELL_SIZE 
        pixel_y = self.position[1] * settings.CELL_SIZE 
         
        surface.blit(apple_img,(pixel_x,pixel_y))

