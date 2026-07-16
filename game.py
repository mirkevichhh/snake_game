import pygame
import settings
import food
import snake



class Score:
    def __init__(self,score_of_game):
        self.score = score_of_game
        self.high_score = self.load_best_score()
        self.font = pygame.font.Font(None, 40)
        
    def draw(self,surface):
        score_surface = self.font.render(f"Score: {self.score}", True, settings.SCORE_COLOR)
        x = 10
        y = 20
        surface.blit(score_surface, (x, y))
    
    def load_best_score(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
    
    def best_score(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.high_score))
                
    def draw_high_score(self,surface):
        high_score_surface = self.font.render(f"Record score: {self.high_score} ", True, settings.SCORE_COLOR)
        x = settings.WINDOW_WIDTH  - 260
        y = 20
        surface.blit(high_score_surface,(x,y))    
            

        
        
