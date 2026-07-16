import unittest
import settings
from snake import Snake
from food import Food

class Test_Snake_Game(unittest.TestCase):
    def test_movement(self):
        snake = Snake()
        start_x,start_y = snake.body[0]
        
        snake_down = Snake()
        snake_down.snake_direction = (0,1)
        snake_down.move()
        self.assertEqual(snake_down.body[0],(start_x,start_y+1))
        
        snake_right = Snake()
        snake_right.snake_direction = (1,0)
        snake_right.move()
        self.assertEqual(snake_right.body[0],(start_x+1,start_y))
        
        snake_up=Snake()
        snake_up.snake_direction=(0,-1)
        snake_up.move()
        self.assertEqual(snake_up.body[0],(start_x, start_y-1))
        
        snake_left = Snake()
        snake_left.snake_direction = (-1,0)
        snake_left.move()
        self.assertEqual(snake_left.body[0],(start_x-1,start_y)) 
        
    def test_no_reverse_to_snake(self):
        snake = Snake()
        current_x,current_y = snake.body[0]
        
        snake_right_to_left = Snake()
        snake_right_to_left.snake_direction = (1,0)
        snake_right_to_left.move()
        snake_right_to_left.change_direction(-1,0)
        snake_right_to_left.move()
        self.assertEqual(snake_right_to_left.body[0],(current_x+2,current_y))
        
        snake_down_to_up = Snake()
        snake_down_to_up.snake_direction = (0,1)
        snake_down_to_up.move()
        snake_down_to_up.change_direction(0,-1)
        snake_down_to_up.move()
        self.assertEqual(snake_down_to_up.body[0],(current_x,current_y+2))
        
        snake_left_to_right = Snake()
        snake_left_to_right.snake_direction = (-1,0)
        snake_left_to_right.move()
        snake_left_to_right.change_direction(1,0)
        snake_left_to_right.move()
        self.assertEqual(snake_left_to_right.body[0],(current_x-2,current_y))
        
        snake_up_to_down = Snake()
        snake_up_to_down.snake_direction=(0,-1)
        snake_up_to_down.move()
        snake_up_to_down.change_direction(0,1)
        snake_up_to_down.move()
        self.assertEqual(snake_up_to_down.body[0],(current_x,current_y-2))
        
    def test_wall_collision(self):
        snake_to_left_wall = Snake()
        snake_to_left_wall.body = [(1,10),(2,10),(3,10)]
        snake_to_left_wall.snake_direction = (-1,0)
        snake_to_left_wall.move()
        self.assertTrue(snake_to_left_wall.end_of_game) 
        
        snake_to_right_wall = Snake()
        snake_to_right_wall.body = [(settings.GRID_WIDTH,10),(settings.GRID_WIDTH-1,10),(settings.GRID_WIDTH-2,10)]
        snake_to_right_wall.snake_direction = (1,0)
        snake_to_right_wall.move()
        self.assertTrue(snake_to_right_wall.end_of_game) 
        
        snake_to_up_wall = Snake()
        snake_to_up_wall.body = [(1,1),(1,2),(1,3)]
        snake_to_up_wall.snake_direction = (0,-1)
        snake_to_up_wall.move()
        self.assertTrue(snake_to_up_wall.end_of_game) 
        
        snake_to_down_wall = Snake()
        snake_to_down_wall.body = [(1,settings.GRID_HEIGHT),(settings.GRID_HEIGHT-1,10),(settings.GRID_HEIGHT-2,10)]
        snake_to_down_wall.snake_direction = (0,1)
        snake_to_down_wall.move()
        self.assertTrue(snake_to_left_wall.end_of_game) 
        
    def test_self_colusion(self):
        snake = Snake()
        snake.body = [(10, 10), (10, 11), (11, 11), (11, 10), (12, 10)]
        snake.snake_direction = (1, 0)
        snake.move()
        self.assertTrue(snake.end_of_game)
        
    def test_generate_food(self):
        snake = Snake()
        snake.body = [(x,6) for x in range(6,20)]
        food = Food(snake.body)
        self.assertNotIn(food.position,snake.body)
        self.assertIsNotNone(food.position)
            
           

if __name__ == '__main__':
    unittest.main()