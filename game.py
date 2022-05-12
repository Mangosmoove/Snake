import numpy as np
from Learning import QLearing
from backbone import Food, RL
from BFS import bfs
import pygame

pygame.init()

# Pygame Internals
display_width = 200
display_height = 250
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")
img = pygame.image.load('head.png')
img2 = pygame.image.load('food.png')
pygame.display.flip()
FPS = 30  #Game Speed
block_size = 10 #How many pixels our head / food is

# colors
black = (0, 255, 255)
red = (255, 0, 0)
#Produce random color each time
color = list(np.random.choice(range(256), size = 3))
white = (0, 0, 0)

actions = ["up", "left", "right"]
SnakeAI = QLearing(actions, epsilon = 0.01)

# If first run, comment out
#SnakeAI.loadQ()

#Train QLearning
def QLearning_Training(times=10):
    Score_Total = []
    for i in range(times):
        # Adds events to event Q
        pygame.event.pump()
        game_over = False

        start_x = 70
        start_y = 50

        snake = RL(gameDisplay, display_width, display_height, img, start_x, start_y)
        foods = Food(gameDisplay, display_width, display_height, block_size, img2, snake.sList)

        a_x, a_y = foods.getFood()
        initialState = snake.get_state([a_x, a_y])
        action = "right"

        while not game_over:
            a_x, a_y = foods.getFood()
            snake.updateList(a_x, a_y)
            # Negative Reward
            reward = -1

            # Snake dies
            if snake.is_alive() is False:
                game_over = True
                # Negative Reward
                reward = -30
                Score_Total.append(snake.snake_length - 1)
            print(reward)
            gameDisplay.fill(white)

            # Snake does well, eats food
            if snake.eaten is True:
                foods.updateFood(snake.sList)

                # Positive Reward
                reward = 10

            state = snake.get_state([a_x, a_y])  # Updated state
            SnakeAI.updateQ(tuple(initialState), action, tuple(state), reward)

            # Save the Q
            SnakeAI.saveQ()
            a_x, a_y = foods.getFood()
            initialState = snake.get_state([a_x, a_y])
            action = SnakeAI.getA(tuple(state))
            snake.changeDirection(action)

            foods.display()
            snake.eaten = False
            snake.display()
            snake.showScore()
            pygame.display.update()
            clock.tick(FPS)

    score = sum(Score_Total) / len(Score_Total)
    print("Average score: {}".format(score))


def BFS_Game():
    pygame.event.pump()
    Score_Total = []
    start_x = 70
    start_y = 50
    game_over = False

    snake = RL(gameDisplay, display_width, display_height, img, start_x, start_y)
    foods = Food(gameDisplay, display_width, display_height, block_size, img2, snake.sList)

    while not game_over:
        x, y = foods.getFood()
        snake.updateList(x, y)

        if snake.eaten is True:
            foods.updateFood(snake.sList)

        if snake.is_alive() is False:
            game_over = True
            Score_Total.append(snake.snake_length - 1)
        gameDisplay.fill(white)

        foods.display()
        snake.eaten = False
        snake.display()
        snake.showScore()
        pygame.display.update()
        clock.tick(FPS)

        x, y = foods.getFood()
        headX, headY = snake.snakeHead()
        visited = snake.sList.copy()
        visited.remove([headX, headY])
        result = bfs(display_width, display_height, block_size, visited, [x, y], [headX, headY])

        try:
            next_cell = result[1]

        except TypeError:
            print("Average score: {}".format(Score_Total))

        Xdist = next_cell[0] - headX
        Ydist = next_cell[1] - headY

        if Ydist < 0:
            snake.direction = "up"
        elif Ydist > 0:
            snake.direction = "down"
        elif Xdist < 0:
            snake.direction = "left"
        elif Xdist > 0:
            snake.direction = "right"


    print("Average score: {}".format(Score_Total))

if __name__ == "__main__":
    #For QLearning
    QLearning_Training()

    #For BFS
    #BFS_Game()
