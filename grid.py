import string

# from helper_function import number_to_letter

# we use variables rows and cols for easy generalization
def print_grid(rows, cols, player_name, grid): # add a TRUE / FALSE parameter for whether computer's screen will be displayed
    column_labels = string.ascii_uppercase[:cols]

    print("  ", end="")
    for label in column_labels:
        print(f'   {label}', end='')
    print()

    for row in range(1, rows+1):
        print("   +", end="")
        for col in range(cols):
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
    for col in range(cols):
        print("---+", end="")
        # if col == (cols/2):
        #     print("YOU")
    print()
    
    grid_width = cols * 4 + 3
    name_padding = (grid_width - len(player_name)) // 2
    print("   " + " " * name_padding + player_name)