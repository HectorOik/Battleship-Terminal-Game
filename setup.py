# should probably make all this into a class
import string
import random

from grid import print_single_grid
from helper_function import letter_to_number, number_to_letter
from specifications import *
# Available SHIPS:
# 1 x Destroyer (2 spaces)
# 1 x Submarine (3 spaces)
# 1 x Cruiser (3 spaces)
# 1 x Battleship (4 spaces)
# 1 x Carrier (5 spaces)
  
def setup():
    print("SETTING UP SHIPS...")
    grid_computer, ships_computer = setup_robot()
    print("The computer has setup its SHIPS. Now it's you turn.\n")
    grid_human, ships_human = setup_human()
    print("Congratulation you have finished setting up your ships.")
    print("STARTING GAME...")
    return grid_human, grid_computer, ships_human, ships_computer

def setup_robot():
    grid_computer = {}
    for col in column_labels:
        for row in range(1, ROWS+1):
            grid_computer[f'{col}{row}'] = None
    ships_computer = {}

    for ship, length in SHIPS.items():
        bow = random.choice(list(grid_computer.keys()))
        direction = random.choice(DIRECTIONS)
        while not check_space(bow, direction, length, grid_computer):
            bow = random.choice(list(grid_computer.keys()))
            direction = random.choice(DIRECTIONS)
            if check_space(bow, direction, length, grid_computer):
                break
        grid_computer, list_of_keys = add_ship(grid_computer, ship, bow, direction, length)
        ships_computer[ship] = set(list_of_keys)

    return grid_computer, ships_computer

def setup_human():
    grid_human = {}
    for col in column_labels:
        for row in range(1, ROWS+1):
            grid_human[f'{col}{row}'] = None

    print_single_grid("You", grid_human)
    print("You will place your SHIPS by first typing the square the bow (front of the ship) will be in.")
    print("For example, type 'B2' to place the bow of your ship on B2\n")
    ships_human = {}
    for ship, length in SHIPS.items():
        bow = input(f"Now, where would you like to place your {ship.upper()} (length {length})? ")
        i = 1
        space_exits = False
        while not bow in grid_human.keys() or grid_human[bow] != None or not space_exits:
            # show the board again so player remembers where they have placed the SHIPS
            if i % 3 == 0:
                print_single_grid("You", grid_human)
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
                print_single_grid("You", grid_human)
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
        ships_human[ship] = set(list_of_keys)
        print_single_grid("You", grid_human)

    return grid_human, ships_human



        

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