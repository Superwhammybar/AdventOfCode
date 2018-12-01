inputs = []

with open('p2-inputs') as txt:
    for row in txt:
        inputs.append(row)

value = 0
frequencies = [0]
while True:
    for adjustments in inputs:
        value += int(adjustments)
        if value in frequencies:
            print(value)
            break
        else:
            frequencies.append(value)
