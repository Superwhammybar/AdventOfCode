import matplotlib.pyplot as plt
import re

pattern = '-?[0-9]{1,6}'
compiled = re.compile(pattern)

coords = {}

with open('d10-inputs') as txtfile:
    for num, row in enumerate(txtfile):
        find = compiled.findall(row)

        x = int(find[0])
        y = int(find[1])

        vel_x = int(find[2])
        vel_y = int(find[3])
        print(x, y, vel_x, vel_y)
        coords[num] = [[x, y], [vel_x, vel_y]]


counter = 0
plt.show()

scat = plt.scatter(0, 0)

while True:
    if counter % 10 == 0:
        if scat:
            scat.remove()
        for key, val in coords.items():
            scat = plt.scatter(val[0][0], val[0][1])
        plt.pause(0.05)

    for key, val in coords.items():
        coords[key][0][0] = coords[key][0][0] + coords[key][1][0]
        coords[key][0][1] = coords[key][0][1] + coords[key][1][1]


    counter += 1
