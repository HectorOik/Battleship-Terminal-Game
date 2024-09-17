# should probably make all this into a class

import string
import random

from grid import print_grid, name
# Available Ships:
# 1 x Destroyer (2 spaces)
# 1 x Submarine (3 spaces)
# 1 x Cruiser (3 spaces)
# 1 x Battleship (4 spaces)
# 1 x Carrier (5 spaces)
ships = {"Destroyer": 2, "Submarine": 3, "Cruiser": 3, "Battleship": 4, "Carrier": 5} # grid_computerionary of ships and their lengths
directions = ['U', 'D', 'R', 'L'] # up, down, right, left 
ROWS = 10
COLS = 10
  
def setup(ships):
    column_labels = string.ascii_uppercase[:COLS]
    grid_computer = {}
    grid_human = {}

    for col in column_labels:
        for row in range(1, ROWS+1):
            grid_computer[f'{col}{row}'] = None
            grid_human[f'{col}{row}'] = None

    print("SETTING UP SHIPS...")
    grid_computer = setup_robot(ships, grid_computer)
    print("The computer has setup its ships. Now it's you turn.\n")
    setup_human(ships, grid_human)
    # print(grid_computer)

def setup_robot(ships, grid_computer):
    for ship, length in ships.items():
        bow = random.choice(list(grid_computer.keys()))
        direction = random.choice(directions)
        while not check_space(bow, direction, length, grid_computer):
            bow = random.choice(list(grid_computer.keys()))
            direction = random.choice(directions)
            if check_space(bow, direction, length, grid_computer):
                break
        grid_computer = add_ship(grid_computer, ship, bow, direction, length)

    return grid_computer

def setup_human(ships, grid_human):
    print("You will place your ships by first typing the square the bow (front of the ship) will be in.")
    print("For example, type 'B2' to place the bow of your ship on B2\n")
    for ship, length in ships.items():
        bow = input(f"Where would you like to place your {ship.upper()}? ")
        i = 1
        while not bow in grid_human.keys():
            print("Please enter a valid square...")
            bow = input(f"Where would you like to place your {ship.upper()}? ")
            # show the board again so player remembers where they have placed the ships
            if i % 3 == 0:
                print_grid(ROWS, COLS, name)
        print(f"Perfect! {bow} it is!")
        direction = input(f"In which direction would like to place your {ship.upper()}? ('U', 'D', 'R', 'L') ")
        j = 1
        while not direction in directions:
            print("Please enter a valid direction...")
            direction = input(f"In which direction would like to place your {ship.upper()}? ('U', 'D', 'R', 'L') ")
            if j % 3 == 0:
                print_grid(ROWS, COLS, name)



        

def check_space(bow, direction, length_of_ship, grid_computer):
    if grid_computer[bow] != None:
        # return "Ship already exists"
        return False
    if direction == 'U':
        if int(bow[1:]) - length_of_ship < 0:
            # return "Out of bounds"
            return False
        for i in range(1, length_of_ship-1):
            if grid_computer[f'{bow[0]}{int(bow[1:])-i}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    elif direction == 'D':
        if int(bow[1:]) + length_of_ship > (ROWS + 1):
            # return "Out of bounds"
            return False
        for i in range(1, length_of_ship-1):
            if grid_computer[f'{bow[0]}{int(bow[1:])+i}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    elif direction == 'R':
        if letter_to_number(bow[0]) + length_of_ship > (COLS + 1):
            # return "Out of bounds"
            return False
        for i in range(1, length_of_ship-1):
            if grid_computer[f'{number_to_letter(letter_to_number(bow[0])+i)}{bow[1:]}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True
    elif direction == 'L':
        if letter_to_number(bow[0]) - length_of_ship < 0:
            # return "Out of bounds"
            return False
        for i in range(1, length_of_ship-1):
            if grid_computer[f'{number_to_letter(letter_to_number(bow[0])-i)}{bow[1:]}'] is None:
                continue
                # return "Space already occupied"
            return False
        return True

def add_ship(grid_computer, ship, bow, direction, length):
    if direction == 'U':
        add_ship_up(grid_computer, ship, bow, length)
    if direction == 'D':
        add_ship_down(grid_computer, ship, bow, length)
    if direction == 'R':
        add_ship_right(grid_computer, ship, bow, length)
    if direction == 'L':
        add_ship_left(grid_computer, ship, bow, length)
    return grid_computer

def add_ship_up(grid_computer, ship, bow, length):
    for i in range(length):
        grid_computer[f'{bow[0]}{int(bow[1:])+i}'] = ship
    return grid_computer
def add_ship_down(grid_computer, ship, bow, length):
    for i in range(length):
        grid_computer[f'{bow[0]}{int(bow[1:])-i}'] = ship
    return grid_computer
def add_ship_right(grid_computer, ship, bow, length):
    for i in range(length):
        grid_computer[f'{number_to_letter(letter_to_number(bow[0])+i)}{bow[1:]}'] = ship
    return grid_computer
def add_ship_left(grid_computer, ship, bow, length):
    for i in range(length):
        grid_computer[f'{number_to_letter(letter_to_number(bow[0])-i)}{bow[1:]}'] = ship
    return grid_computer

def letter_to_number(letter):
    return ord(letter) - ord('A') + 1

def number_to_letter(number):
    return chr(ord('A') + number - 1)




setup(ships)