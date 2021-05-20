input_int = int(input().split()[1])

tiles = []
tiles.extend([int(i) for i in input().split()])

this_sum = 0
if 3 in tiles:
    flag = -1
    index = tiles.index(3)

    for i in range(input_int):
        if index == (input_int - 2) or index == 0:
            flag *= -1
        if tiles[index] == 0:
            this_sum += 1
        index += flag
else:
    flag = +1
    index = tiles.index(2)
    for i in range(input_int):
        if index == (input_int - 2) or index == 0:
            flag *= -1
        if tiles[index] == 0:
            this_sum += 1
        index += flag

print(this_sum)
