def letter_to_number(letter):
    return ord(letter) - ord('A') + 1

def number_to_letter(number):
    return chr(ord('A') + number - 1)

def answer_is_yes_or_no(answer):
    while answer not in ['Yes', 'No']:
        answer = input("Please enter 'Yes' or 'No': ")
    return answer