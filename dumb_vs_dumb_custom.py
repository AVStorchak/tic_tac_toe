from ai_options import make_dumb_move
from check_functions import check_tie, check_win


def create_grid(rows, columns):
    flat_grid = list(range(rows * columns))
    transformed_grid = []
    for i in range(rows):
        transformed_grid.append(flat_grid[(columns*i):columns*(i+1)])
    return transformed_grid


def show_grid(grid, turn):
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
                if count % COLUMNS == 0:
                    print("\n")


def make_move(grid, move, mark):
    row = move // COLUMNS
    column = move % COLUMNS
    position = [row, column]
    grid[position[0]][position[1]] = mark
    return position


def cycle_ai_turn(grid, player=1, opponent=2, turn=0):
    name = PLAYERS[player][0]
    mark = PLAYERS[player][1]
    while check_tie(grid) is False:
        show_grid(grid, turn)
        turn += 1
        move = make_dumb_move(grid)
        position = make_move(grid, move, mark)

        if check_win(grid, mark, position, MARKS_TO_WIN):
            show_grid(grid, turn)
            print(f"The {name} won!")
            exit()
        elif check_tie(grid):
            show_grid(grid, turn)
            print("This is a tie!")
        else:
            cycle_ai_turn(grid, opponent, player, turn)


if __name__ == "__main__":
    ROWS = 4
    COLUMNS = 4
    MARKS_TO_WIN = 3
    PLAYERS = {1: ("AI1", "X"), 2: ("AI2", "O")}
    initial_grid = create_grid(ROWS, COLUMNS)
    cycle_ai_turn(initial_grid)
