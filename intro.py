from helper_function import answer_is_yes_or_no

def greeting():
    return input("Hi! Welcome to BATTLESHIP! What is your name? ")

def start_game(name):
    want_to_play = answer_is_yes_or_no(input(f"Hi, {name}! Do you want to play BATTLESHIP? "))
    if want_to_play == 'Yes':
        familiar_with_game = answer_is_yes_or_no(input("Nice! Are you familiar with the rules of the game? "))
        if familiar_with_game == 'No':
            print("I don't have an explanation ready at the moment but here is a useful link: https://en.wikipedia.org/wiki/Battleship_(game)")
            want_to_play = answer_is_yes_or_no(input("Do you still want to play? "))
            if want_to_play == 'Yes':
                return True
            else:
                return False
        else:
            print("Okay let's start")
            return True
    else:
        return False
