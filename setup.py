# should probably make all this into a class

import string
import random

# from grid import print_single_grid
from helper_function import letter_to_number, number_to_letter
# Available SHIPS:
# 1 x Destroyer (2 spaces)
# 1 x Submarine (3 spaces)
# 1 x Cruiser (3 spaces)
# 1 x Battleship (4 spaces)
# 1 x Carrier (5 spaces)
SHIPS = {"Destroyer": 2, "Submarine": 3, "Cruiser": 3, "Battleship": 4, "Carrier": 5} # dictionary of SHIPS and their lengths
DIRECTIONS = ['U', 'D', 'R', 'L'] # up, down, right, left 
ROWS = 10
COLS = 10
column_labels = string.ascii_uppercase[:COLS]
name = "Hector"
  
def setup():

    print("SETTING UP SHIPS...")
    grid_computer = setup_robot(SHIPS, grid_computer)
    print("The computer has setup its SHIPS. Now it's you turn.\n")
    # print_single_grid(ROWS, COLS, 'COMPUTER', grid_computer)
    grid_human = setup_human(SHIPS)

def setup_robot():
    grid_computer = {}
    for col in column_labels:
        for row in range(1, ROWS+1):
            grid_computer[f'{col}{row}'] = None

    for ship, length in SHIPS.items():
        bow = random.choice(list(grid_computer.keys()))
        direction = random.choice(DIRECTIONS)
        while not check_space(bow, direction, length, grid_computer):
            bow = random.choice(list(grid_computer.keys()))
            direction = random.choice(DIRECTIONS)
            if check_space(bow, direction, length, grid_computer):
                break
        grid_computer, _ = add_ship(grid_computer, ship, bow, direction, length)

    return grid_computer

def setup_human():
    grid_human = {}
    for col in column_labels:
        for row in range(1, ROWS+1):
            grid_human[f'{col}{row}'] = None

    print_single_grid(ROWS, COLS, name, grid_human)
    print("You will place your SHIPS by first typing the square the bow (front of the ship) will be in.")
    print("For example, type 'B2' to place the bow of your ship on B2\n")
    for ship, length in SHIPS.items():
        bow = input(f"Now, where would you like to place your {ship.upper()} (length {length})? ")
        i = 1
        space_exits = False
        while not bow in grid_human.keys() or grid_human[bow] != None or not space_exits:
            # show the board again so player remembers where they have placed the SHIPS
            if i % 3 == 0:
                print_single_grid(ROWS, COLS, name)
            if bow not in grid_human.keys():
                print()
                print("Please enter a valid square")
            elif grid_human[bow] != None:
                print()
                print("That square is already occupied")
            elif not space_exits:
                for direction in DIRECTIONS:
                    if check_direction(grid_human, bow, direction, length): #instead of constantly checking DIRECTIONS save direction check result in a variable
                        space_exits = True
                        break
                # could there be an issue with an infinte loop because a ship can't fit anywhere?
                if space_exits == False:
                    print(f"There is no space for {ship.upper()} here in any direction")
                else:
                    break
            bow = input(f"Where would you like to place your {ship.upper()} (length {length})? ")
            i += 1
        print(f"Perfect! {bow} it is!")
        print()
        # make list of DIRECTIONS and remove the ones for which there is no space left
        direction = input(f"In which direction would like to place your {ship.upper()} (length {length})? ('U', 'D', 'R', 'L') ")
        j = 1
        while direction not in DIRECTIONS or not check_direction(grid_human, bow, direction, length):
            if j % 3 == 0:
                print_single_grid(ROWS, COLS, name)
            if direction not in DIRECTIONS:
                print("Please enter a valid direction...")
                direction = input(f"In which direction would like to place your {ship.upper()}? ('U', 'D', 'R', 'L') ")
            if not check_direction(grid_human, bow, direction, length):
                print("There is no space in that direction")
                # should be able to remove DIRECTIONS in which there is no space
                direction = input(f"In which direction would like to place your {ship.upper()}? ('U', 'D', 'R', 'L') ")
            j += 1
        print()
        grid_human, list_of_keys = add_ship(grid_human, ship, bow, direction, length)
        print(f'Perfect! Placing {ship.upper()} on {list_of_keys}')
        print_single_grid(ROWS, COLS, name, grid_human)

    return grid_human



        

def check_space(bow, direction, length_of_ship, grid):
    return check_bow(grid, bow) and check_direction(grid, bow, direction, length_of_ship)
    
def check_bow(grid, bow):
    if grid[bow] != None:
        # square already occupied
        return False
    else:
        return True
    
def check_direction(grid, bow, direction, length):
    if direction == 'U':
        if int(bow[1:]) - length < 0:
            # return "Out of bounds"
            return False
        for i in range(1, length):
            if grid[f'{bow[0]}{int(bow[1:])-i}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    elif direction == 'D':
        if int(bow[1:]) + length > (ROWS + 1):
            # return "Out of bounds"
            return False
        for i in range(1, length):
            if grid[f'{bow[0]}{int(bow[1:])+i}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    elif direction == 'R':
        if letter_to_number(bow[0]) + length > (COLS + 1):
            # return "Out of bounds"
            return False
        for i in range(1, length):
            if grid[f'{number_to_letter(letter_to_number(bow[0])+i)}{bow[1:]}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    elif direction == 'L':
        if letter_to_number(bow[0]) - length < 0:
            # return "Out of bounds"
            return False
        for i in range(1, length):
            if grid[f'{number_to_letter(letter_to_number(bow[0])-i)}{bow[1:]}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True

def add_ship(grid, ship, bow, direction, length):
    if direction == 'U':
        grid, list_of_keys = add_ship_up(grid, ship, bow, length)
    if direction == 'D':
        grid, list_of_keys = add_ship_down(grid, ship, bow, length)
    if direction == 'R':
        grid, list_of_keys = add_ship_right(grid, ship, bow, length)
    if direction == 'L':
        grid, list_of_keys = add_ship_left(grid, ship, bow, length)
    return grid, list_of_keys

def add_ship_up(grid_computer, ship, bow, length):
    list_of_keys = []
    for i in range(length):
        grid_computer[f'{bow[0]}{int(bow[1:])-i}'] = ship
        list_of_keys += [f'{bow[0]}{int(bow[1:])-i}']
    return grid_computer, list_of_keys
def add_ship_down(grid_computer, ship, bow, length):
    list_of_keys = []
    for i in range(length):
        grid_computer[f'{bow[0]}{int(bow[1:])+i}'] = ship
        list_of_keys += [f'{bow[0]}{int(bow[1:])+i}']
    return grid_computer, list_of_keys
def add_ship_right(grid_computer, ship, bow, length):
    list_of_keys = []
    for i in range(length):
        grid_computer[f'{number_to_letter(letter_to_number(bow[0])+i)}{bow[1:]}'] = ship
        list_of_keys += [f'{number_to_letter(letter_to_number(bow[0])+i)}{bow[1:]}']
    return grid_computer, list_of_keys
def add_ship_left(grid_computer, ship, bow, length):
    list_of_keys = []
    for i in range(length):
        grid_computer[f'{number_to_letter(letter_to_number(bow[0])-i)}{bow[1:]}'] = ship
        list_of_keys += [f'{number_to_letter(letter_to_number(bow[0])+i)}{bow[1:]}']
    return grid_computer, list_of_keys

grid_computer = setup_robot()