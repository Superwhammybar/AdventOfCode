all_entries = []

with open('p1-inputs') as txt:
    for row in txt:
        all_entries.append(row.strip('\n'))

only_2 = []
only_3 = []

for num, word in enumerate(all_entries):
    letter_dict = {}
    for letter in word:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] = letter_dict[letter]+1

    if 2 in letter_dict.values():
        only_2.append(word)
        print(str(num), str(2), word)

    if 3 in letter_dict.values():
        only_3.append(word)
        print(str(num), str(3), word)

twos = len(only_2)
threes = len(only_3)

check_sum = twos * threes

print(check_sum)

