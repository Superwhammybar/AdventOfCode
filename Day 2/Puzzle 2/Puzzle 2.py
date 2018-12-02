all_entries = []

with open('..\d2-inputs') as txt:
    for row in txt:
        all_entries.append(row.strip('\n'))


final_words = []
for word in all_entries:
    for compare_word in all_entries:
        diff = []
        for num, cha in enumerate(word):
            if cha == compare_word[num]:
                continue
            else:
                diff.append([cha, num])

        if len(diff) == 1:
            final_words.append([word, diff])

final_list = []
for letter in final_words[0][0]:
    final_list.append(letter)

final_list.pop(final_words[0][1][0][1])

final_word = ''.join(final_list)

print(final_word)