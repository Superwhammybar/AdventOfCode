# Extract dependencies into dictionary
# Start with dependencies of 0
# Once added to a list for the answer, remove the letter as a dependency from all others
# Repeat for the new 0 dependencies

import re

pattern = ' [A-Z]{1} '

compiled = re.compile(pattern)

dependencies = {}

with open('test-inputs') as txtfile:
    for row in txtfile:
        found_chars = compiled.findall(row)

        for num, chars in enumerate(found_chars):
            char = chars.replace(' ', '')
            if num == 0:
                dep_char = char
            if num == 1:
                c = char

        if c not in dependencies.keys():
            dependencies[c] = [dep_char]
        else:
            dependencies[c].append(dep_char)

        if dep_char not in dependencies.keys():
            dependencies[dep_char] = []

print(dependencies)

final_list = []

complete = False
while complete is False:

    current_zeros = []
    for char, dep in dependencies.items():
        if len(dep) == 0:
            current_zeros.append(char)

    current_zeros.sort()

    for z in current_zeros[0]:
        final_list.append(z)
        del dependencies[z]

        for k,v in dependencies.items():
            if z in v:
                v.remove(z)

    if len(dependencies) == 0:
        complete = True

print(''.join(final_list))
