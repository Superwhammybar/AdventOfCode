list_of_info = []

with open('..\d3-inputs') as txtfile:
    for line in txtfile:
        line_info = []
        line = line.replace('#', '')
        split_line = line.split(' @ ')
        number = split_line[0]

        split_line = split_line[1].split(': ')
        coords_list = split_line[0].split(',')
        coords = []
        for i in coords_list:
            coords.append(int(i))


        area_list = split_line[1].split('x')
        area_list[1] = area_list[1].replace('\n', '')
        area = []
        for a in area_list:
            area.append(int(a))

        list_of_info.append([int(number), coords, area])


print(list_of_info)

board = []
for i in range(2000):
    row = []
    for k in range(2000):
        row.append(0)
    board.append(row)

for info in list_of_info:

    x_coord = info[1][0] # First coord to pass
    y_coord = info[1][1] # Second coord to pass

    x_width = info[2][0]
    y_height = info[2][1]
    for height in range(y_height):
        for width in range(x_width):
            location = board[y_coord + height][x_coord + width]

            board[y_coord + height][x_coord + width] += 1


for info in list_of_info:
    fail = False
    x_coord = info[1][0]  # First coord to pass
    y_coord = info[1][1]  # Second coord to pass

    x_width = info[2][0]
    y_height = info[2][1]
    for height in range(y_height):
        for width in range(x_width):
            if board[y_coord + height][x_coord + width]  >= 2:
                fail = True
    if fail is False:
        print(info[0])
