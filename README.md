# SNAKE
This is group 5's implementation of the popular Snake game. Rather than having a person be in control of the snake, we decided to look at various machine learning techniques to help in implementing an Artificial Intelligent agent that will learn how to play the Snake game on its own.

game.py sets up the Snake game by using PyGame. This file also trains the agent using QLearning, a basic variant of Reinforcement Learning. game.py contains the main function to run the entire program and the user can choose if they would like to run the BFS algorithm we implemented or the QLearning Algorithm. game.py contains the helper code to access Learning.py and BFS.py. It uses backbone.py to move the agent, get the food, display using materials from PyGame.
**Note: if you are running QLearning for the first time, please comment out line 32 in game.py. After the initial run, you should uncomment line 32.** 

Learning.py runs when the user runs the QLearning_Algorithm() in game.py. It uses pickle to load data from previous runs so the agent can learn from those runs. It uses NumPY to get the location for the rewards (this includes both positive and negative rewards). It uses Random to move to a location.

BFS.py contains the actual BFS search algorithm. We utilized an algorithm found online to help in outlining our code, but we did some improvements with that code. This class uses Queue to help in finding in the shortest path of the snake head to the food. If the user runs BFS_Game() in game.py, BFS.py will be executed.

backbone.py uses Random to display food in various places. This file is the 'backbone' of the program as it contains the rules, actions, food, and states.

We created this project using Python, PyCharm, and Github. The libraries we used are: Pickle, NumPY, PyGame, Queue, and Random.

If you do not have some of the libraries listed, most IDEs such as IntelliJ, PyCharm, and Eclipse will let you import them if you hover over the import statement. If that does not work, you can try commands to install the libraries and modules:

for PyGame:
```pip install PyGame```

Pickle is a module already installed for Python2 and Python3. But just in case it does not work: 
```pip install pickle-mixin``` 
