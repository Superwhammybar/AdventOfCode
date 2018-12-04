inputs = []

with open('d1-inputs') as txt:
    for row in txt:
        inputs.append(row)

value = 0
for adjustments in inputs:
    value += int(adjustments)

print(value)