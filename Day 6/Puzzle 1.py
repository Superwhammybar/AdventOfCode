# Split coords by ',
# Assign name to each pair
# For each letter, plot on a list of lists board and
# Mark each 'coord' in list of lists with the letter and it's distance to the letter
# Use difference between row numbers and column numbers added together for distance
# On each new letter, if the distance to the letter is shorter than the current owner of the coord then replace
# If they're equal, mark coord as shared
# Iterate over final board and count the number of each letter present
# Exclude any letters which touch the edge of the board from the calculation
# Most letters = winner.


coords = []
x_coords = []
y_coords = []

chars = [str(x) for x in range(50)]

with open('d6-inputs') as txtfile:
    row_counter = 0
    for row in txtfile:
        row_info = []
        row_coords = row.split(', ')
        row_char = chars[row_counter]
        row_counter += 1
        row_info.append(row_char)

        for coord in row_coords:
            row_info.append(int(coord.replace('\n', '')))

        coords.append(row_info)

        x_coords.append(int(row_coords[0]))
        y_coords.append(int(row_coords[1].replace('\n', '')))

max_x = max(x_coords)
max_y = max(y_coords)

board = []
for m_y in range(max_y+1):
    board_row = []
    for m_x in range(max_x+1):
        board_row.append(['', 1000, False]) # Owner, Shortest Distance, Shared Shortest
    board.append(board_row)

for c in coords:
    char = c[0]
    x = c[1]
    y = c[2]

    board[y][x][0] = char
    board[y][x][1] = -1

    for num, all_y in enumerate(board):
        for n, all_x in enumerate(all_y):
            y_dist = y - num
            if y_dist < 0:
                y_dist = y_dist * -1

            x_dist = x - n
            if x_dist < 0:
                x_dist = x_dist * -1

            distance = y_dist + x_dist

            if distance == all_x[1]:
                all_x[2] = True

            if distance < all_x[1]:
                all_x[0] = char
                all_x[1] = distance
                all_x[2] = False

results = {}

for row in board:
    for col in row:
        if col[2] is False:
            if col[0] not in results.keys():
                results[col[0]] = 1
            else:
                results[col[0]] = results[col[0]] + 1


exclusions = []
for num, row in enumerate(board):

    for n, col in enumerate(row):
        if num == 0 or n == 0 or num == len(board) or n == len(row):
            exclusions.append(col[0])


max_val = 0
winner = ''
for k, v in results.items():
    if k not in exclusions:
        if v > max_val:
            max_val = v
            winner = k

print(winner, max_val)