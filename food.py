import pygame
import random
import settings
class Food:
    def __init__(self,snake_body):
        self.position = self.generate_random_position(snake_body)
    def generate_random_position(self,snake_body):
        free_points = []
        for x in range(settings.GRID_WIDTH):
            for y in range(settings.GRID_HEIGHT):
                if (x,y) not in snake_body:
                    free_points.append((x,y))
        if not free_points:
            return None
        return random.choice(free_points)

    def draw(self,surface):
        if self.position is None:
            return
        pixel_x = self.position[0] * settings.CELL_SIZE + settings.CELL_SIZE//2
        pixel_y = self.position[1] * settings.CELL_SIZE + settings.CELL_SIZE//2
        
        food_radius = settings.CELL_SIZE//6

        pygame.draw.circle(surface, (255, 0, 0), (pixel_x,pixel_y), food_radius)

