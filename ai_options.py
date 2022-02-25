import copy
import random

from check_functions import check_win


def make_dumb_move(grid):
    """

    Makes the simpliest random move.

    Parameters:
        grid (list): the current game grid

    Returns:
        move(int): the next move

    """
    options = [i for row in grid for i in row if isinstance(i, int)]
    move = random.choice(options)
    return move


def make_reasonable_move(grid, mark, opponent_mark, marks_to_win):
    """

    Makes a move based on ensuring self win or preventing opponent's win

    Parameters:
        grid (list): the current game grid
        mark (str): the player's mark
        opponent_mark (str): the opponent's mark
        marks_to_win (int): the number of marks to win

    Returns:
        move(int): the next move

    """
    options = [i for row in grid for i in row if isinstance(i, int)]
    for option in options:
        dummy_board = copy.deepcopy(grid)
        row = option // 3
        column = option % 3
        position = [row, column]

        dummy_board[position[0]][position[1]] = mark
        if check_win(dummy_board, mark, position, marks_to_win):
            return option

        dummy_board[position[0]][position[1]] = opponent_mark
        if check_win(dummy_board, opponent_mark, position, marks_to_win):
            return option

    move = random.choice(options)
    return move
