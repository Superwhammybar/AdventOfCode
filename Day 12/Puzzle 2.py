# Convert input to 0 and 1
# Convert rules to 0 and 1
# Create list of 100 wide?
# Apply rules to each item * 20

rules = []
start_input = ''
with open('rules') as rule:
    for row in rule:
        rule = row.split(' => ')
        rule[1] = rule[1].replace('\n', '')
        rules.append(rule)


with open('d12-inputs') as inputs:
    for row in inputs:
        row.replace('\n', '')
        start_input += row

generations = 50000000000
generation_0 = []
for i in range(1000):
    generation_0.append('.')
for x in start_input:
    if x == '\n':
        continue
    generation_0.append(x)
for i in range(900):
    generation_0.append('.')

last_gen = []
for gen in range(162):
    generation_output = []

    plants = 0
    for num, p in enumerate(last_gen):
        if p == '#':
            plants += num - 1000

    print(gen, plants)

    if not last_gen:
        last_gen = generation_0.copy()

    for num, plant in enumerate(last_gen):
        if num < 2 or num > len(last_gen)-2:
            generation_output.append('.')
            continue

        current_view = ''.join(last_gen[num-2:num+3])

        size = len(generation_output)

        for rule in rules:
            if current_view == rule[0]:
                generation_output.append(rule[1])

        if size == len(generation_output):
            generation_output.append('.')

    last_gen = generation_output.copy()


ans = ((generations - 161) * 73) + plants
print(ans)
