def display_grid(grid):
    for row in grid:
        print('|'.join(row))
    return


# ... validate the input

def get_valid_input(message):
    while True:
        value = int(input(message))
        try:
            if 0 <= value <= 2:
                return value
            else:
                print("Invalid Input. Please try again.")
        except ValueError:
            print("Invalid Input. Please enter a valid number")


# .........................
# i asked for help to write is_win() and is_draw() functions.
# ** i tried too much in these functions but my code always doesn't fit all the game cases :(
# but the rest of code is completely wrote by myself
def is_win(grid, player):
    # check win for rows
    for row in grid:
        if all(cell == player for cell in row):
            return True

    # check win for cols
    for col in range(3):
        if all(grid[row][col] == player for row in range(3)):
            return True

    # check win for diagonals
    if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
        return True

    # no wins
    return False


def is_draw(grid):
    # iterate over rows
    for row in grid:
        # iterate over cells
        for cell in row:
            if cell == ' ':
                return False
    # if all cells are occupied then, the game is draw
    return True


def main():
    grid = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    display_grid(grid)

    value = input("Please choose a symbol X or O: ").upper()
    while value not in ('X', 'O'):
        print("Invalid symbol. Please choose X or O")
        value = input()
    player_symbols = [value]
    if value == 'O':
        player_symbols.append('X')
    else:
        player_symbols.append('O')

    player_idx = 0  # the current player index

    while True:
        row = get_valid_input('Enter the row in range (0-2)')
        col = get_valid_input('Enter the col in range (0-2)')

        if grid[row][col] != ' ':
            print("Cell already occupied. Please choose another cell")
            continue

        grid[row][col] = player_symbols[player_idx]
        display_grid(grid)

        if is_win(grid, player_symbols[player_idx]):
            print(f"Player {player_symbols[player_idx]} wins!")
            break

        if is_draw(grid):
            print("It's a draw!")
            break

        player_idx = 1 - player_idx  # the second player turn


if __name__ == "__main__":
    main()
