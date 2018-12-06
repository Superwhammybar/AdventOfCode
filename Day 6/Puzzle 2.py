# Split coords by ',
# Assign name to each pair
# For each letter, plot on a list of lists board and
# Mark each 'coord' in list of lists with the letter and it's distance to the letter
# Use difference between row numbers and column numbers added together for distance
# On each new letter, if the distance to the letter is shorter than the current owner of the coord then replace
# If they're equal, mark coord as sharedPuzzle 1.py
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
        board_row.append([False, False]) #Owned by coord, in the region, str
    board.append(board_row)

for c in coords:
    x = c[1]
    y = c[2]

    board[y][x][0] = True


region_counter = 0

for num, row in enumerate(board):
    for n, col in enumerate(row):
        total_distance = 0

        for coord in coords:
            x = coord[1]
            y = coord[2]

            y_dist = abs(y - num)
            x_dist = abs(x - n)

            dist = y_dist + x_dist
            total_distance += dist

        if total_distance < 10000:
            region_counter += 1
            col[1] = True

print(region_counter)
