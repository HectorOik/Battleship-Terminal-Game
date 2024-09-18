#this is a file for all the constants used. They are stored here to avoid circular import.
import string

SHIPS = {"Destroyer": 2, "Submarine": 3, "Cruiser": 3, "Battleship": 4, "Carrier": 5} # dictionary of SHIPS and their lengths
DIRECTIONS = ['U', 'D', 'R', 'L'] # up, down, right, left 
ROWS = 10
COLS = 10
column_labels = string.ascii_uppercase[:COLS]