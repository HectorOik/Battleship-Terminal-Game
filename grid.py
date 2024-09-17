import string

# we use variables rows and cols for easy generalization
def print_grid(rows, cols, player_name):
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

        print("|", end="")
        for col in range(cols):
            print("   |", end="")
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

name = input("What's your name? ")
print_grid(10,10,name)