"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # board is list of list
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #print("player:", board)
    x_count = 0
    o_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1

    if x_count == 0 and o_count == 0:
        return X
    elif x_count + o_count == 9:
        return 0 
    elif x_count > o_count:
        return O
    elif o_count == x_count:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
    else:
        return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise NotImplementedError("Invalid Input")
    else:
        # A shallow copy: stores the reference of the original elements.
        # A deep copy: recursively adds the copies of nested objects that present in the original elements.
        new_board = copy.deepcopy(board)
        # To get the position, can use "print(action[0], action[1])"
        new_board[action[0]][action[1]] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """ 
    j = 0
    for i in range(3):
        # Checking for horizontal winner
        if board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2]:
            return board[i][j]

        # Checking for vertical winner
        elif board[j][i] == board[j+1][i] and board[j+1][i] == board[j+2][i]:
            return board[j][i]
    
    # Checking for diagonal winner
    # For (0,0), (1,1), (2,2)
    if board[j][j] == board[j+1][j+1] and board[j+1][j+1] == board[j+2][j+2]:
        return board[j][j]
    
    # For (0,2), (1,1), (2,0)
    if board[j][j+2] == board[j+1][j+1] and board[j+1][j+1] == board[j+2][j]: 
        return board[j][j+2]
            
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
           return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def max_value(board):
    if terminal(board):                                                                                                                                                               
        return utility(board), None

    # score as a negative infinite integer
    score = float('-inf')
    tem_move = None

    # if this actions(board) got return 9 move posibilities
    # there will be 8 loops for 9 different "action" in actions(board) 
    for action in actions(board):   
        tem_board = result(board, action) 
        # result(board, action) will return a new_board
        value, move = min_value(tem_board)
        if value > score:
            score = value
            tem_move = action
    return score, tem_move


def min_value(board):
    if terminal(board):
        return utility(board), None

    # score as a positive infinite integer
    score = float('inf')
    tem_move = None

    for action in actions(board):
        tem_board = result(board, action) 
        value, move = max_value(tem_board)
        if value < score:
            score = value
            tem_move = action
    return score, tem_move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None

    ai_play = player(board) 

    # In the beginning, X has 9 posibilities
    if ai_play == X:
        
        final_score, move = max_value(board) 
        return move

    # In the beginning, O has 8 posibilities
    elif ai_play == O:
        
        final_score, move = min_value(board)
        return move
