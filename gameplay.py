import random
from grid import print_both_grids
from specifications import SHIPS

empty_set = set()

def gameplay(grid_human, grid_computer, ships_human, ships_computer):
    game_over = False
    while not game_over:
        # need to import name
        print_both_grids("You", grid_human, "Computer", grid_computer)
        print("\nYour turn. ", end="")
        game_over, winner = human_turn(grid_human, grid_computer, ships_computer)
        if game_over:
            break
        print("\nNow my turn. ", end="")
        game_over, winner = computer_turn(grid_human, grid_computer, ships_human)
        # computer_turn
    print_both_grids("You", grid_human, "Computer", grid_computer)
    return winner

def human_turn(grid_human, grid_computer, ships_computer):
    already_tried = True
    square = input("Which square would you like to hit? ")
    while square not in grid_computer.keys() or already_tried:
        if square not in grid_computer.keys():
            print("Please enter a valid square...")
            square = input("Which square would you like to hit? ")
        else:
            if grid_computer[square] == None or not grid_computer[square][-1] == 'X':
                already_tried = False
                break
            # elif grid_computer[square] == 'X' or grid_computer[square][-1] == 'X':
            #     already_tried = True
            if already_tried:
                print(f"You've already hit {square}.")
                square = input("Which square would you like to hit? ")
            else:
                break
    if grid_computer[square] == None:
        print("No luck") #need list to randomize responses
        grid_computer[square] = 'X'
    elif grid_computer[square] != None and grid_computer[square] != 'X':
        print("Nice shot") #need list to randomize responses
        ship_name = grid_computer[square]
        grid_computer[square] += ' X'
        ships_computer[ship_name].remove(square)
        if ships_computer[ship_name] == empty_set:
            del ships_computer[ship_name]
        if ships_computer == {}:
            return True, 1
        print_both_grids("You", grid_human, "Computer", grid_computer)
        print("\nYou get to play again! ", end="")
        grid_computer = human_turn(grid_human, grid_computer, ships_computer)
    return False, ''

#need to make it so computer tries nearby squares instead of fully random when it hits
def computer_turn(grid_human, grid_computer, ships_human):
    square = random.choice(list(grid_human.keys()))
    while grid_human[square] != None and grid_human[square][-1] == 'X':
        square = random.choice(list(grid_human.keys()))
    print(f"I'll hit {square}")
    if grid_human[square] == None:
        print("I missed %^#()%")
        grid_human[square] = 'X'
    else:
        print("Right on!")
        ship_name = grid_human[square]
        grid_human[square] += ' X'
        ships_human[ship_name].remove(square)
        if ships_human[ship_name] == empty_set:
            del ships_human[ship_name]
        if ships_human == {}:
            return True, 2
        print("I get to go again. Hehe. ", end="")
        grid_human = computer_turn(grid_human, grid_computer, ships_human)
    return False, ''