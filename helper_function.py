def letter_to_number(letter):
    return ord(letter) - ord('A') + 1

def number_to_letter(number):
    return chr(ord('A') + number - 1)