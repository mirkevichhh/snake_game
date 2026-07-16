import pygame
import ctypes
import settings
from snake import Snake
from food import Food
from game import Score

pygame.init()

game_font = pygame.font.Font(None,40)
fat_font = pygame.font.Font(None ,100)
small_font = pygame.font.Font(None,30)
myappid = 'mycompany.myproduct.subproduct.version' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

icon = pygame.image.load("C:/University/1LS/Python/snake-game/snake.png")
pygame.display.set_icon(icon)



apple = pygame.image.load("C:/University/1LS/Python/snake-game/apple.png") 
apple_img = pygame.transform.scale(apple,(settings.CELL_SIZE-2,settings.CELL_SIZE-2))

pause = pygame.image.load("C:/University/1LS/Python/snake-game/pause.png")
pause_img = pygame.transform.scale(pause,(40,40))

kept = pygame.image.load("C:/University/1LS/Python/snake-game/key.png")
kept_img = pygame.transform.scale(kept,(80,80))



screen = pygame.display.set_mode((settings.WINDOW_WIDTH,settings.WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Snake Game")
SNAKE_MOVE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_MOVE, settings.SPEED)

score_of_game = Score(0)
snake = Snake()
food = Food(snake.body)

flag_for_tutor = True
game_state = "Start_menu"
running = True
while running:

    
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            
        if game_state == "Playing":
            if i.type == SNAKE_MOVE:
                if snake.snake_direction != (0, 0):
                    snake.move()
                    
            elif i.type == pygame.KEYDOWN:
                if (i.key == pygame.K_w or i.key == pygame.K_UP) and snake.snake_direction != (0, 1):
                    snake.change_direction(0, -1)
                elif (i.key == pygame.K_a or i.key == pygame.K_LEFT) and snake.snake_direction != (1, 0):
                    snake.change_direction(-1, 0)
                elif (i.key == pygame.K_s or i.key == pygame.K_DOWN) and snake.snake_direction != (0, -1):
                    snake.change_direction(0, 1)
                elif (i.key == pygame.K_d or i.key == pygame.K_RIGHT) and snake.snake_direction != (-1, 0):
                    snake.change_direction(1, 0)
                
            
        if snake.end_of_game == True:
            score_of_game.best_score()
            pygame.time.wait(1000)
            game_state = "Game_over"
            snake.end_of_game = False
            
            
        if game_state == "Game_over":
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_r:
                    settings.SPEED = 200
                    pygame.time.set_timer(SNAKE_MOVE, settings.SPEED)
                    snake = Snake()
                    food = Food(snake.body)
                    score_of_game.score = 0
                    game_state = "Playing"
                elif i.key == pygame.K_q:
                    running = False
                    
        
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                if game_state == "Playing":
                    pygame.time.set_timer(SNAKE_MOVE, 0)
                    game_state = "Paused"
                elif game_state == "Paused":
                    game_state = "Playing"
                    pygame.time.set_timer(SNAKE_MOVE, settings.SPEED)
                    
        
            
            
            
        

        if snake.get_head() == food.position:
            score_of_game.score+=10
            snake.grow = True
            if settings.SPEED>=120:
                settings.SPEED-=5
                pygame.time.set_timer(SNAKE_MOVE, settings.SPEED)

            
                
            new_position = food.generate_random_position(snake.body)

            if new_position == None:
                game_state = "Game_over"
            else:
                food.position = new_position
        

    


    if game_state == "Playing": 
        screen.fill(settings.BACKGROUND_COLOR)   
        pygame.draw.rect(screen,(settings.WPAPPER_COLOR),(0,0,settings.WINDOW_WIDTH,settings.HEADER_ROWS))
        pygame.draw.rect(screen,(settings.WPAPPER_COLOR),(0,0,settings.CELL_SIZE,settings.WINDOW_HEIGHT))
        pygame.draw.rect(screen,(settings.WPAPPER_COLOR),(settings.WINDOW_WIDTH - settings.CELL_SIZE,0,settings.CELL_SIZE,settings.WINDOW_HEIGHT))
        pygame.draw.rect(screen,(settings.WPAPPER_COLOR),(0,settings.WINDOW_HEIGHT-settings.CELL_SIZE,settings.WINDOW_WIDTH,settings.CELL_SIZE))
        for x in range(settings.CELL_SIZE,settings.WINDOW_WIDTH - settings.CELL_SIZE,settings.CELL_SIZE):
            pygame.draw.line(screen, settings.GRID_COLOR, (x, settings.HEADER_ROWS), (x, settings.WINDOW_HEIGHT - settings.CELL_SIZE))
        for y in range(settings.HEADER_ROWS, settings.WINDOW_HEIGHT - settings.CELL_SIZE, settings.CELL_SIZE):
            pygame.draw.line(screen, settings.GRID_COLOR, (settings.CELL_SIZE, y), (settings.WINDOW_WIDTH - settings.CELL_SIZE, y))
        if snake.snake_direction!=(0,0):
            flag_for_tutor = False
        
        if flag_for_tutor == True and snake.snake_direction == (0, 0):
                kept_rect = kept_img.get_rect(center=(settings.WINDOW_WIDTH // 2 - 100-5-3, 202))
                screen.blit(kept_img, kept_rect)
                
            
            
        snake.draw(screen)
        food.draw(screen,apple_img)
        score_of_game.draw(screen)
        score_of_game.draw_high_score(screen)
        
            
    elif game_state == "Game_over":
        screen.fill(settings.GAME_OVER_COLOR)
        text_game_over = fat_font.render("GAME OVER",True,"Red" )
        screen.blit(text_game_over,(settings.WINDOW_WIDTH // 2 -200,settings.WINDOW_HEIGHT//2  - 120))
        text_record = game_font.render(f"Record of the game: {score_of_game.high_score}", True, "White")
        screen.blit(text_record,(settings.WINDOW_WIDTH // 2 -150,settings.WINDOW_HEIGHT//2  -40))
        score_text  = game_font.render(f"Your score was: {score_of_game.score}", True, "White")
        screen.blit(score_text,(settings.WINDOW_WIDTH//2-110, settings.WINDOW_HEIGHT // 2 ))
        text_options = game_font.render("You have next options:", True,"White")
        screen.blit(text_options, (settings.WINDOW_WIDTH // 2 - 400, settings.WINDOW_HEIGHT // 2 +100))
        restart_text = game_font.render("Press 'R' to Restart", True, "White")
        screen.blit(restart_text, (settings.WINDOW_WIDTH // 2 - 370, settings.WINDOW_HEIGHT // 2 + 135))
        text_leave = game_font.render("Press 'Q' to Leave", True,"White")
        screen.blit(text_leave, (settings.WINDOW_WIDTH // 2 - 370, settings.WINDOW_HEIGHT // 2 +170))
        
    elif game_state == "Paused":
        screen.fill(settings.BACKGROUND_COLOR)   
        pygame.draw.rect(screen,(settings.WPAPPER_COLOR),(0,0,settings.WINDOW_WIDTH,settings.HEADER_ROWS))
        pygame.draw.rect(screen,(settings.WPAPPER_COLOR),(0,0,settings.CELL_SIZE,settings.WINDOW_HEIGHT))
        pygame.draw.rect(screen,(settings.WPAPPER_COLOR),(settings.WINDOW_WIDTH - settings.CELL_SIZE,0,settings.CELL_SIZE,settings.WINDOW_HEIGHT))
        pygame.draw.rect(screen,(settings.WPAPPER_COLOR),(0,settings.WINDOW_HEIGHT-settings.CELL_SIZE,settings.WINDOW_WIDTH,settings.CELL_SIZE))
        for x in range(settings.CELL_SIZE,settings.WINDOW_WIDTH - settings.CELL_SIZE,settings.CELL_SIZE):
            pygame.draw.line(screen, settings.GRID_COLOR, (x, settings.HEADER_ROWS), (x, settings.WINDOW_HEIGHT - settings.CELL_SIZE))
        for y in range(settings.HEADER_ROWS, settings.WINDOW_HEIGHT - settings.CELL_SIZE, settings.CELL_SIZE):
            pygame.draw.line(screen, settings.GRID_COLOR, (settings.CELL_SIZE, y), (settings.WINDOW_WIDTH - settings.CELL_SIZE, y))

        snake.draw(screen)
        food.draw(screen, apple_img)
        score_of_game.draw(screen)
        score_of_game.draw_high_score(screen)


        overlay = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        overlay.set_alpha(200) 
        overlay.fill(settings.PAUSED_COLOR)
        screen.blit(overlay, (0, 0))
        

        pause_rect = pause_img.get_rect(center=(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2 - 20))
        screen.blit(pause_img, pause_rect)
        
        hint_text = small_font.render("Press ESC to resume", True, (50, 50, 50))
        hint_rect = hint_text.get_rect(center=(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2 + 50))
        screen.blit(hint_text, hint_rect)
        
    elif game_state == "Start_menu":
        screen.fill(settings.START_MENU_COLOR)
        text_welcome = game_font.render("WELCOME TO THE SNAKE GAME",True, "White")
        screen.blit(text_welcome,(settings.WINDOW_WIDTH // 2 -230,settings.WINDOW_HEIGHT//2  - 120))
        text_1 = small_font.render("The snake game is a classic, addictive arcade game where players navigate",True,"White")
        screen.blit(text_1,(10, settings.WINDOW_HEIGHT//2 +140 ))
        text_2  = small_font.render("a constantly moving line that grows longer every time it consumes food, requiring", True, "White")
        screen.blit(text_2,(10, settings.WINDOW_HEIGHT // 2 + 165))
        text_3 = small_font.render("careful maneuvering to avoid crashing into walls or the snake's own tail.", True,"White")
        screen.blit(text_3, (10, settings.WINDOW_HEIGHT // 2 +190))
        
        key_rect = pygame.Rect(settings.WINDOW_WIDTH // 2 - 150, settings.WINDOW_HEIGHT // 2 - 65, settings.WINDOW_WIDTH // 3, settings.CELL_SIZE * 2)
        pygame.draw.rect(screen, settings.KEY_COLOR, key_rect)
        text_brigada = small_font.render("Press to start the game",True,(240, 227, 86))
        text_rect = text_brigada.get_rect(center=key_rect.center)
        screen.blit(text_brigada, text_rect)
        mouse = pygame.mouse.get_pos()
        if  key_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            game_state = "Playing"
        
            
        
        
        
    clock.tick(settings.FPS)
    pygame.display.update()
    
pygame.quit()
