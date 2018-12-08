# Extract dependencies into dictionary
# Start with dependencies of 0
# Assign a worker that dependency and time to complete
# Iterate until complete and then remove dependency
# Repeat for the new 0 dependencies

import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

time_check = {}
for num, a in enumerate(alphabet):
    time_check[a] = num + 61

pattern = ' [A-Z]{1} '

compiled = re.compile(pattern)

dependencies = {}

with open('d7-inputs') as txtfile:
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

final_time = 0

complete = False

workers = {'me': [False, ''],
           'elf1': [False, ''],
           'elf2': [False, ''],
           'elf3': [False, ''],
           'elf4': [False, '']
           }

counter = -1
while complete is False:
    print(dependencies)
    print(counter, workers['me'], workers['elf1']
          , workers['elf2'], workers['elf3'], workers['elf4'])
    active_dependencies = []
    active_workers = 0
    for worker, val in workers.items():
        if val[0] is False:
            continue
        else:
            workers[worker][0] = workers[worker][0] - 1
            if workers[worker][0] == 0:
                workers[worker][0] = False
                del dependencies[val[1]]
                for k, v in dependencies.items():
                    if val[1] in v:
                        v.remove(val[1])
                workers[worker][1] = ''
            else:
                active_dependencies.append(val[1])
                active_workers += 1
    if len(workers) == active_workers:
        counter += 1
        continue

    current_zeros = []
    for char, dep in dependencies.items():
        if len(dep) == 0:
            current_zeros.append(char)

    current_zeros.sort()

    for num, z in enumerate(current_zeros):
        if num == len(workers) - active_workers:
            break

        for worker, val in workers.items():
            if val[0] is False and z not in active_dependencies:
                workers[worker][0] = time_check[z.lower()]
                workers[worker][1] = z
                break

    if len(dependencies) == 0 and active_workers == 0:
        complete = True

    counter += 1

print(counter)
