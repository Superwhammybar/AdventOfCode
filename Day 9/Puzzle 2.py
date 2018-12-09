import re

players = 0
max_marble = 0

pattern = '[0-9]{1,10}'
compiled = re.compile(pattern)
with open('d9-inputs') as txtfile:
    for row in txtfile:
        ans = compiled.findall(row)

        players = int(ans[0])
        max_marble = int(ans[1])*100

print(players, max_marble)

marbles = [0, 1]
current_marble = 1

current_marble_worth = 2
current_player = 2

player_list = {}
for player in range(players):
    player_list[player+1] = 0

while current_marble_worth <= max_marble:
    placement = current_marble + 2
    if placement > len(marbles):
        placement -= len(marbles)

    if current_marble_worth % 23 == 0:
        player_list[current_player] = player_list[current_player] + current_marble_worth

        extra_score = current_marble - 7
        if extra_score < 0:
            extra_score = current_marble - 7 + len(marbles)

        player_list[current_player] = player_list[current_player] + marbles[extra_score]

        if extra_score + 1 >= len(marbles):
            current_marble = marbles[extra_score + 1 - len(marbles)]
        else:
            current_marble = extra_score

        marbles.remove(marbles[extra_score])

    else:
        marbles.insert(placement, current_marble_worth)
        current_marble = placement


    current_marble_worth += 1
    current_player += 1
    if current_player > players:
        current_player = 1


best_score = 0
winner = 0
for k,v in player_list.items():
    if v > best_score:
        best_score = v
        winner = k

print(winner, best_score)
