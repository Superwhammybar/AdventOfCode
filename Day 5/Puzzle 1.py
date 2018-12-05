with open('d5-inputs') as txtfile:
    for row in txtfile:
        input_string = row

# Iterate over string
# Compare current to next character
# If same character and different case, eliminate
# Start from next character to compare so we avoid using an eliminated character - use a flag?
# Repeat iteration until no eliminations occur

complete = False


while complete is False:
    to_eliminate = []
    compare_char = None

    for num, character in enumerate(input_string):
        if compare_char is None:
            compare_char = character
            continue

        current_char = character
        if compare_char.upper() == current_char.upper():
            if compare_char.isupper() and current_char.islower() or compare_char.islower() and current_char.isupper():
                to_eliminate.append(num-1)
                to_eliminate.append(num)
                compare_char = None
                continue

        compare_char = character

    if not to_eliminate:
        print(input_string)
        print(len(input_string))
        complete = True

    to_eliminate.reverse()
    character_string = []
    for character in input_string:
        character_string.append(character)

    for elim in to_eliminate:
        del character_string[elim]

    input_string = ''.join(character_string)

