# Tic Tac Toe Game
Hello, my friends. Ever wonder to create your first AI game? 


## How to implement a tic-tac-toe?
Using minimax as the algorithm and pygame to display the graphics, it means you can play on your PC :shipit:

## Project objective:
Developing a simple game based on minimax algorithm to get a taste of artificial intelligent.    

## Technologies:
```
Python
Pygame
OpenSans
```
Algorithm
```
Minimax
```

## What is Minimax?
It is a type of adversarial search which has an agent and its oposite agent. Both agents will fight with each other to win the game.
To implement minimax, there's a few important functions:
**Initial state**
- A empty set of tic-tac-toe game

**Player**
- To return whether the current stage is player X or player O

**Notion of actions**
- To return all the actions that can be taken
- It regulates which square on the board is empty after every single move

**Transition Model**
- Input the current board state and action, result an updated board after adding the action to board.
- Any illegal action will be rejected.

**Goal Test**
- To check if the current state is the final board.
- It indicates there should be a winner or tie.

**Marks**
- Utility has a role to transform the "X" as 1, "O" as -1 and tie as "0"

## Requirement:
1. Install python3 in Visual Studio Code
2. Install Pygame
``pip3 install pygame``
3. Download the whole package in this master branch
4. Run
``python3 runner.py``

#### Special appreciation to CS50

