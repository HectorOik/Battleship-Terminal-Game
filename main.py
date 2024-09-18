from setup import setup
from gameplay import gameplay
from intro import greeting, start_game
from end import outro

def main():
    name = greeting()
    will_play = start_game(name)
    if will_play:
        grid_human, grid_computer, ships_human, ships_computer = setup()
        winner = gameplay(grid_human, grid_computer, ships_human, ships_computer)
        outro(winner)
    else:
        print("Please come back another time")

main()