import pygame
import ctypes
import settings
from snake import Snake
from food import Food

pygame.init()
game_font = pygame.font.Font(None,40)
text_end = game_font.render("Congratulations",True,"Orange")
myappid = 'mycompany.myproduct.subproduct.version' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
icon = pygame.image.load("D:/Work/snake.png")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((settings.WINDOW_WIDTH,settings.WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Snake Game")
SNAKE_MOVE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_MOVE, 200)

snake = Snake()
food = Food(snake.body)
running = True
while running:

    
    screen.fill(settings.BACKGROUND_COLOR)
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

        if i.type == SNAKE_MOVE:
            snake.move()

        if snake.get_head() == food.position:
            snake.grow = True
            new_position = food.generate_random_position(snake.body)

            if new_position == None:
                running = False
                pygame.blit(text_end,(20,20))
            else:
                food.position = new_position

    for x in range(0,settings.WINDOW_WIDTH,settings.CELL_SIZE):
        pygame.draw.line(screen, settings.GRID_COLOR, (x, 0), (x, settings.WINDOW_HEIGHT))
    
    for y in range(0,settings.WINDOW_HEIGHT,settings.CELL_SIZE):
        pygame.draw.line(screen,settings.GRID_COLOR,(0,y), (settings.WINDOW_WIDTH, y))

    snake.draw(screen)
    food.draw(screen)



    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and snake.snake_direction!=(0,1):
        snake.snake_direction = (0,-1)
    elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and snake.snake_direction!=(1,0):
        snake.snake_direction = (-1,0)
    elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and snake.snake_direction!=(0,-1):
        snake.snake_direction = (0,1)
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and snake.snake_direction!=(-1,0):
        snake.snake_direction = (1,0)
    clock.tick(settings.FPS)
    pygame.display.update()
    
pygame.quit()
