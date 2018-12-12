# 1 - 300
# 3x3 selection
# rack_id = x + 10
# power_level = rack_id * y
# power_level = power_level + grid_serial (input)
# power_level = power_level * rack_id
# power_level = HUNDREDS digit from power_level (12345 = 3)
# power_level = power_level - 5

grid_serial = 9435

board = []
for y in range(1, 301):
    row = []
    for x in range(1, 301):
        x_coord = x
        y_coord = y
        rack_id = x_coord + 10

        power_level = rack_id * y_coord
        power_level = power_level + grid_serial
        power_level = str(power_level * rack_id)
        power_level = power_level[-3:]
        power_level = power_level[0:1]
        power_level = int(power_level) - 5

        row.append([x_coord, y_coord, power_level])

    board.append(row)
for num, row in enumerate(board):
    if num > 43 and num < 48:
        print(row)

best3x3 = 0
best_coord = []
for row in board:
    if row[0][1] + 2 >= len(board):
        continue
    for col in row:
        if col[0] + 2 >= len(row):
            continue
        x = col[0]
        y = col[1]
        local_3x3_score = 0
        for i in range(3):
            for j in range(3):
                new_x = i + x - 1
                new_y = j + y - 1
                local_3x3_score += board[new_y][new_x][2]

        if local_3x3_score > best3x3:
            best3x3 = local_3x3_score
            best_coord = [col[0], col[1]]

print(best3x3, best_coord)