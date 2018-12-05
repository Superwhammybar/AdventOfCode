with open('d5-inputs') as txtfile:
    for row in txtfile:
        input_string = row

# Choose a character from list of all characters in alphabet
# Remove all those from the string (both upper and lower)
# Iterate over string
# Compare current to next character
# If same character and different case, eliminate
# Start from next character to compare so we avoid using an eliminated character - use a flag?
# Repeat iteration until no eliminations occur
# Store character and length
# Iterate over those and find the shortest length

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

results = []

for a in alphabet:
    print(a)
    string = input_string

    string = string.replace(a.upper(), '')
    string = string.replace(a, '')

    complete = False
    while complete is False:
        to_eliminate = []
        compare_char = None

        for num, character in enumerate(string):
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
            complete = True
            results.append((a, len(string)))

        to_eliminate.reverse()
        character_string = []
        for character in string:
            character_string.append(character)

        for elim in to_eliminate:
            del character_string[elim]

        string = ''.join(character_string)


results.sort(key=lambda x: x[1])
print(results[0])