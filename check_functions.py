def check_win(grid, mark, position, marks_to_win):
    """

    Checks win condition through the row, column, and two diagonals
    related to the current move

    Parameters:
        grid (list): the current game grid
        mark (str): the player's mark
        position (list): the coordinates of the current move
        marks_to_win (int): the number of marks to win

    Returns:
        True of False according to the current win condition

    """
    if check_row(grid, mark, position, marks_to_win):
        return True
    if check_column(grid, mark, position, marks_to_win):
        return True
    if check_diagonals(grid, mark, position, marks_to_win):
        return True
    return False


def check_tie(grid):
    """

    Checks tie condition.

    Parameters:
        grid (list): the current game grid

    Returns:
        True of False according to the current tie condition

    """
    available_grid = [i for row in grid for i in row if isinstance(i, int)]
    if len(available_grid) == 0:
        return True
    return False


def check_diagonals(grid, mark, position, marks_to_win):
    """

    Checks win condition for two diagonals related to the current move

    Parameters:
        grid (list): the current game grid
        mark (str): the player's mark
        position (list): the coordinates of the current move
        marks_to_win (int): the number of marks to win

    Returns:
        True of False according to the current win condition

    """
    row, column = position
    row_number = len(grid)
    col_number = len(grid[0]) if row_number > 0 else 0

    d1_i = min(row + column, row_number - 1)
    d1_j = max(column - (row_number - 1 - row), 0)
    d1_len = min(d1_i + 1, col_number - d1_j)
    diag1 = [grid[d1_i - k][d1_j + k] for k in range(d1_len)]
    str_diag1 = "".join([str(i) for i in diag1])
    if (mark * marks_to_win) in str_diag1:
        return True

    d2_i = max(row - column, 0)
    d2_j = max(column - row, 0)
    d2_len = min(row_number - d2_i, col_number - d2_j)
    diag2 = [grid[d2_i + k][d2_j + k] for k in range(d2_len)]
    str_diag2 = "".join([str(i) for i in diag2])
    if (mark * marks_to_win) in str_diag2:
        return True

    return False


def check_row(grid, mark, position, marks_to_win):
    """

    Checks win condition for the row related to the current move

    Parameters:
        grid (list): the current game grid
        mark (str): the player's mark
        position (list): the coordinates of the current move
        marks_to_win (int): the number of marks to win

    Returns:
        True of False according to the current win condition

    """
    str_row = "".join([str(i) for i in grid[position[0]]])
    if (mark * marks_to_win) in str_row:
        return True
    return False


def check_column(grid, mark, position, marks_to_win):
    """

    Checks win condition for the column related to the current move

    Parameters:
        grid (list): the current game grid
        mark (str): the player's mark
        position (list): the coordinates of the current move
        marks_to_win (int): the number of marks to win

    Returns:
        True of False according to the current win condition

    """
    column = [row[position[1]] for row in grid]
    str_column = "".join([str(i) for i in column])
    if (mark * marks_to_win) in str_column:
        return True
    return False
