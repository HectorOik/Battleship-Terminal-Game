# should probably make all this into a class

import string
import random
# Available Ships:
# 1 x Destroyer (2 spaces)
# 1 x Submarine (3 spaces)
# 1 x Cruiser (3 spaces)
# 1 x Battleship (4 spaces)
# 1 x Carrier (5 spaces)
ships = {"Destroyer": 2, "Submarine": 3, "Cruiser": 3, "Battleship": 4, "Carrier": 5} # grid_dictionary of ships and their lengths
directions = ['U', 'D', 'R', 'L'] # up, down, right, left 
ROWS = 10
COLS = 10
  
def setup(ships):
    column_labels = string.ascii_uppercase[:COLS]
    grid_dict = {}

    for col in column_labels:
        for row in range(1, ROWS+1):
            grid_dict[f'{col}{row}'] = None

    grid_dict = setup_robot(ships, grid_dict)
    # print(grid_dict)

def setup_robot(ships, grid_dict):
    for ship, length in ships.items():
        print(ship)
        print(length)
        bow = random.choice(list(grid_dict.keys()))
        direction = random.choice(directions)
        while not check_space(bow, direction, length, grid_dict):
            bow = random.choice(list(grid_dict.keys()))
            direction = random.choice(directions)
            if check_space(bow, direction, length, grid_dict):
                break
        grid_dict = add_ship(grid_dict, ship, bow, direction, length)

    return grid_dict

def check_space(bow, direction, length_of_ship, grid_dict):
    if grid_dict[bow] != None:
        # return "Ship already exists"
        return False
    if direction == 'U':
        if int(bow[1:]) - length_of_ship < 0:
            # return "Out of bounds"
            return False
        for i in range(1, length_of_ship-1):
            if grid_dict[f'{bow[0]}{int(bow[1:])-i}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    elif direction == 'D':
        if int(bow[1:]) + length_of_ship > (ROWS + 1):
            # return "Out of bounds"
            return False
        for i in range(1, length_of_ship-1):
            if grid_dict[f'{bow[0]}{int(bow[1:])+i}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    elif direction == 'R':
        if letter_to_number(bow[0]) + length_of_ship > (COLS + 1):
            # return "Out of bounds"
            return False
        for i in range(1, length_of_ship-1):
            if grid_dict[f'{number_to_letter(letter_to_number(bow[0])+i)}{bow[1:]}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    elif direction == 'L':
        if letter_to_number(bow[0]) - length_of_ship < 0:
            # return "Out of bounds"
            return False
        for i in range(1, length_of_ship-1):
            if grid_dict[f'{number_to_letter(letter_to_number(bow[0])-i)}{bow[1:]}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    else:
        return "Invalid Direction"

def add_ship(grid_dict, ship, bow, direction, length):
    if direction == 'U':
        add_ship_up(grid_dict, ship, bow, length)
    if direction == 'D':
        add_ship_down(grid_dict, ship, bow, length)
    if direction == 'R':
        add_ship_right(grid_dict, ship, bow, length)
    if direction == 'L':
        add_ship_left(grid_dict, ship, bow, length)
    return grid_dict

def add_ship_up(grid_dict, ship, bow, length):
    for i in range(length):
        grid_dict[f'{bow[0]}{int(bow[1:])+i}'] = ship
    return grid_dict
def add_ship_down(grid_dict, ship, bow, length):
    for i in range(length):
        grid_dict[f'{bow[0]}{int(bow[1:])-i}'] = ship
    return grid_dict
def add_ship_right(grid_dict, ship, bow, length):
    for i in range(length):
        grid_dict[f'{number_to_letter(letter_to_number(bow[0])+i)}{bow[1:]}'] = ship
    return grid_dict
def add_ship_left(grid_dict, ship, bow, length):
    for i in range(length):
        grid_dict[f'{number_to_letter(letter_to_number(bow[0])-i)}{bow[1:]}'] = ship
    return grid_dict

def letter_to_number(letter):
    return ord(letter) - ord('A') + 1

def number_to_letter(number):
    return chr(ord('A') + number - 1)




setup(ships)