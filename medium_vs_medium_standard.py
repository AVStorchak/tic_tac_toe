from ai_options import make_reasonable_move
from check_functions import check_tie, check_win


def create_grid(rows, columns):
    """

    Creates initial grid based on the passed parameters

    Parameters:
        rows (int): the number of rows
        columns (int): the number of rows

    Returns:
        transformed_grid (list): 2D-grid

    """
    flat_grid = list(range(rows * columns))
    transformed_grid = []
    for i in range(rows):
        transformed_grid.append(flat_grid[(columns*i):columns*(i+1)])
    return transformed_grid


def show_grid(grid, turn):
    """

    Displays the grid and the turn number

    Parameters:
        grid (list): the updated grid
        turn (int): the turn number

    """
    count = 0
    if turn == 0:
        print("The game starts!\n")
    else:
        print(f"Turn {turn}:\n")
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count += 1
                if isinstance(grid[i][j], int):
                    print("·", end="  ")
                else:
                    print(grid[i][j], end="  ")
                if count % 3 == 0:
                    print("\n")


def make_move(grid, move, mark):
    """

    Calculates mark coordinates in the grid
    and updates the grid

    Parameters:
        grid (list): the grid to be updated
        move (int): the number of grid cell to be updated
        mark (str): the mark to be placed

    Returns:
        position (list): the coordinates of the placed mark

    """
    row = move // 3
    column = move % 3
    position = [row, column]
    grid[position[0]][position[1]] = mark
    return position


def cycle_ai_turn(grid, player=1, opponent=2, turn=0):
    """

    Cycles AI turns until a win or a tie is achieved

    Parameters:
        grid (list): the game grid
        player (int): the number of the active player
        opponent (int): the number of the inactive player
        turn (int): the turn number

    """
    name = PLAYERS[player][0]
    mark = PLAYERS[player][1]
    opponent_mark = PLAYERS[opponent][1]
    while check_tie(grid) is False:
        show_grid(grid, turn)
        turn += 1
        move = make_reasonable_move(grid, mark, opponent_mark, marks_to_win)
        position = make_move(grid, move, mark)

        if check_win(grid, mark, position, marks_to_win):
            show_grid(grid, turn)
            print(f"The {name} won!")
            exit()
        elif check_tie(grid):
            show_grid(grid, turn)
            print("This is a tie!")
        else:
            cycle_ai_turn(grid, opponent, player, turn)


if __name__ == "__main__":
    rows = 3
    columns = 3
    marks_to_win = 3
    PLAYERS = {1: ("AI1", "X"), 2: ("AI2", "O")}
    initial_grid = create_grid(rows, columns)
    cycle_ai_turn(initial_grid)
