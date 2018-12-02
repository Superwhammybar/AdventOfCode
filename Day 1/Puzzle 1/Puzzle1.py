inputs = []

with open('d2-inputs') as txt:
    for row in txt:
        inputs.append(row)

value = 0
for adjustments in inputs:
    value += int(adjustments)

print(value)