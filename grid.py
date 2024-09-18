import string

from setup import setup_robot, column_labels, ROWS, COLS, grid_computer

# we use variables ROWS and COLS for easy generalization
def print_single_grid(player_name, grid): # add a TRUE / FALSE parameter for whether computer's screen will be displayed
    print("  ", end="")
    for label in column_labels:
        print(f'   {label}', end='')
    print()

    for row in range(1, ROWS+1):
        print("   +", end="")
        for col in range(COLS):
            print("---+", end="")
        print()

        print(f'{row:2} ', end="")

        # need to make it so ships you place are shown (what would be a good symbol for this?)
        print("|", end="")
        for col in column_labels:
            symbol = ' '
            if grid[f'{col}{row}'] != None:
                symbol = '*'
            print(f" {symbol} |", end="")
        print()

    print("   +", end="")
    for col in range(COLS):
        print("---+", end="")
        # if col == (COLS/2):
        #     print("YOU")
    print()
    
    grid_width = COLS * 4 + 3
    name_padding = (grid_width - len(player_name)) // 2
    print("   " + " " * name_padding + player_name)

# in the future could possible adjust to make player vs player instead of always versus computer
# would be easier in C++ because print statements don't automatically change line
def print_both_grids(player_1, grid_1, player_2, grid_2):
    print("  ", end="")
    for i in range(2):
        for label in column_labels:
            print(f'   {label}', end='')
        if i == 0:
            print(" " * 11, end="")
    print()

    for row in range(1, ROWS+1):
        print("   +", end="")
        for col in range(COLS):
            print("---+", end="")
        print(" " * 10 + "+", end="")
        for col in range(COLS):
            print("---+", end="")
        print()

        print(f'{row:2} ', end="")
        print("|", end="")
        for col in column_labels:
            symbol = ' '
            # if grid_1[f'{col}{row}'] != None:
                # symbol = '*'
            print(f" {symbol} |", end="")
        print(" " * 7, end="")
        print(f'{row:2} ', end="")
        print("|", end="")
        for col in column_labels:
            symbol = ' '
            # if grid_2[f'{col}{row}'] != None:
                # symbol = '*'
            print(f' {symbol} |', end='')
        print()

    for i in range(2):
        print("   +", end="")
        for col in range(COLS):
            print("---+", end="")
            # if col == (COLS/2):
            #     print("YOU")
        if i == 0:
            print(' ' * 7, end='')
    print()
    
    grid_width = COLS * 4 + 3
    player_1_padding = (grid_width - len(player_1)) // 2
    print("   " + " " * player_1_padding + player_1 + " " * player_1_padding, end='')
    player_2_padding = (grid_width - len(player_2)) // 2
    print(' ' * 7, end='')
    print('   ' + ' ' * player_2_padding + player_2)

# grid_computer = setup_robot()

print_both_grids("Hector", grid_computer, "Hector 2", grid_computer)