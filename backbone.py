import random

#Snake Main
class Snake:
    def __init__(self, gameBox, display_width, display_height, img, x, y, sizeOfFood = 10):
        self.display_width = display_width
        self.display_height = display_height
        self.gameBox = gameBox

        self.head = img
        self.snake_length = 1
        self.sList = [[x, y]]
        self.foodSize = sizeOfFood
        self.eaten = False
        self.direction = "left"

    def showScore(self):
        from game import color, pygame
        score = self.snake_length - 1
        title = pygame.font.SysFont("arial", 13).render("Score: " + str(score), True, color)
        # https://realpython.com/lessons/using-blit-and-flip/
        # drawing score on screen in top left position
        self.gameBox.blit(title, [0, 0])

    def is_alive(self):
        if self.sList[-1] in self.sList[:-1]:
            return False

        elif self.sList[-1][0] >= self.display_width \
                or self.sList[-1][0] < 0\
                or self.sList[-1][1] >= self.display_height\
                or self.sList[-1][1] < 0:

            return False

        else:
            return True

    def Eat_Food(self, randomFoodX, randomFoodY):
        if self.sList[-1][0] == randomFoodX and self.sList[-1][1] == randomFoodY:
            return True
        else:
            return False

    def snakeHead(self):
        return self.sList[-1][0], self.sList[-1][1]

    def updateList(self, randomFoodX, randomFoodY):
        if self.direction == "up":
            Ymove = -self.foodSize
            Xmove = 0


        elif self.direction == "down":
            Ymove = self.foodSize
            Xmove = 0


        elif self.direction == "left":
            Xmove = -self.foodSize
            Ymove = 0


        elif self.direction == "right":
            Xmove = self.foodSize
            Ymove = 0


        snake_head = []
        snake_head.append(self.sList[-1][0] + Xmove)
        snake_head.append(self.sList[-1][1] + Ymove)
        self.sList.append(snake_head)

        if self.Eat_Food(randomFoodX, randomFoodY):
            self.snake_length += 1
            self.eaten = True

        if len(self.sList) > self.snake_length:
            del self.sList[0]

    def display(self):
        from game import color, pygame
        # https://realpython.com/lessons/using-blit-and-flip/
        # drawing snake head on screen
        self.gameBox.blit(self.head, (self.sList[-1][0], self.sList[-1][1]))

        for i in self.sList[:-1]:
            pygame.draw.rect(self.gameBox, color, [i[0], i[1], self.foodSize, self.foodSize])

class Food:
    def __init__(self, gameBox, display_width, display_height, pixels, img, snake_list, sizeOfFood = 10):
        self.display_width = display_width
        self.display_height = display_height
        self.gameBox = gameBox

        self.pSize = pixels
        self.food = img
        self.foodSize = sizeOfFood
        self.randomFoodX = random.randint(0, self.display_width / self.pSize - 1) * 10
        self.randomFoodY = random.randint(0, self.display_height / self.pSize - 1) * 10

        while [self.randomFoodX, self.randomFoodY] in snake_list:
            self.randomFoodX = random.randint(0, self.display_width / self.pSize - 1) * 10
            self.randomFoodY = random.randint(0, self.display_height / self.pSize - 1) * 10

    def getFood(self):
        return self.randomFoodX, self.randomFoodY

    def updateFood(self, snake_list):
        self.randomFoodX = random.randint(0, self.display_width / self.pSize - 1) * 10
        self.randomFoodY = random.randint(0, self.display_height / self.pSize - 1) * 10

        while [self.randomFoodX, self.randomFoodY] in snake_list:
            self.randomFoodX = random.randint(0, self.display_width / self.pSize - 1) * 10
            self.randomFoodY = random.randint(0, self.display_height / self.pSize - 1) * 10

    def display(self):
        # https://realpython.com/lessons/using-blit-and-flip/
        # drawing food on screen
        self.gameBox.blit(self.food, [self.randomFoodX, self.randomFoodY, self.foodSize, self.foodSize])



#Reinforcement Learning Snake (Agent)
class RL(Snake):
    def changeDirection(self, action):
        lookatPos = {"up": 0, "right": 1, "left": -1}
        number = lookatPos[action]

#UP
        if self.direction == "up":
            if number != 0:
                if number == -1:
                    self.direction = "left"
                else:
                    self.direction = "right"
            else:
                self.direction = "up"


#DOWN
        elif self.direction == "down":
            if number != 0:
                if number == -1:
                    self.direction = "right"
                else:
                    self.direction = "left"
            else:
                self.direction = "down"


#LEFT
        elif self.direction == "left":
            if number != 0:
                if number == -1:
                    self.direction = "down"
                else:
                    self.direction = "up"
            else:
                self.direction = "left"


#RIGHT
        elif self.direction == "right":
            if number != 0:
                if number == -1:
                    self.direction = "up"
                else:
                    self.direction = "down"
            else:
                self.direction = "right"



    def get_state(self, target):
        head_x, head_y = self.snakeHead()
        start = [head_x, head_y]
        state = []

        if self.direction == "up":
            nextMove = [[start[0] - self.foodSize, start[1]], [start[0], start[1] - self.foodSize], [start[0] + self.foodSize, start[1]]]

        elif self.direction == "down":
            nextMove = [[start[0] + self.foodSize, start[1]], [start[0], start[1] + self.foodSize], [start[0] - self.foodSize, start[1]]]


        elif self.direction == "left":
            nextMove = [[start[0], start[1] + self.foodSize], [start[0] - self.foodSize, start[1]], [start[0], start[1] - self.foodSize]]


        elif self.direction == "right":
            nextMove = [[start[0], start[1] - self.foodSize], [start[0] + self.foodSize, start[1]], [start[0], start[1] + self.foodSize]]



        for i in nextMove:
            if i == target:
                result = 2

            elif [i[0], i[1]] in self.sList or i[0] < 0 or i[0] >= self.display_width or i[1] < 0 or i[1] >= self.display_height:
                result = 1

            else:
                result = 0


            state.append(result)

        spot = [target[0] - start[0], target[1] - start[1]]


        if self.direction == "up":
            pass


        elif self.direction == "right":
            temp = spot[0]
            spot[0] = spot[1]
            spot[1] = -temp


        elif self.direction == "down":
            temp = spot[0]
            spot[0] = -spot[1]
            spot[1] = -temp


        elif self.direction == "left":
            temp = spot[0]
            spot[0] = -spot[1]
            spot[1] = temp


        state.append(tuple(spot))

        return state

