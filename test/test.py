map_sokoban = {
    "size_x":10,
    "size_y":10
}
destinations = [
    {"x":5,"y":5},
    {"x":4,"y":3},
    {"x":8,"y":8}
    ]
for y in range (map_sokoban["size_y"]):
    for x in range (map_sokoban["size_x"]):
        pic = '- '
        for des in destinations:
            if des["x"] == x and des["y"] == y:
                pic = 'D '
        print (pic, end='')
    print()