# import re
# id_find = '\#[0-9]+?'
# location_find = '[0-9]+?\,[0-9]{1,3}'
# area_find = '[0-9]+?x[0-9]{1,3}'
# list_of_info = []

# with open('..\d3-inputs') as txtfile:
#     for line in txtfile:
#         # print(line)
#         line_info = []
#         id_match = re.compile(id_find)
#         i_find = id_match.findall(line)
#         if i_find:
#             # print(id_find)
#             line_info.append(int(i_find[0].replace('#', '')))
#
#         loc_match = re.compile(location_find)
#         loc_find = loc_match.findall(line)
#         if loc_find:
#             # print(loc_find)
#             loc_list = loc_find[0].split(',')
#             line_info.append((int(loc_list[0]), int(loc_list[1])))
#
#         area_match = re.compile(area_find)
#         a_find = area_match.findall(line)
#         if a_find:
#             # print(a_find)
#             area_list = a_find[0].split('x')
#             line_info.append((int(area_list[0]), int(area_list[1])))
#
#         list_of_info.append(line_info)
#         # print(line_info)

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

counter = 0
for rw in board:
    for col in rw:
        if col >= 2:
            counter += 1

print(counter)
