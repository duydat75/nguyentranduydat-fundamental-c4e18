#game object:
import os
map_sokoban = {
    "size_x":10,
    "size_y":10
}
player = {
    "x":4,
    "y":0
}
boxes = [
    {"x":2,"y":2},
    {"x":7,"y":8},
    {"x":8,"y":3}]
destinations = [
    {"x":5,"y":5},
    {"x":4,"y":3},
    {"x":8,"y":8}
    ]
walls = [
    {"x":3,"y":5},
    {"x":6,"y":7},
    {"x":6,"y":2},
    {"x":2,"y":8},
    {"x":8,"y":6},
    {"x":2,"y":7},
    {"x":2,"y":6},
    {"x":1,"y":6},
    {"x":0,"y":6},
    {'x':3,'y':4},
    {'x':3,'y':3},
    {'x':3,'y':2},
    {'x':4,'y':2},
    {'x':5,'y':2},
    {'x':6,'y':8},
    {'x':6,'y':9}
]
fruit = {'x':0,'y':7}
######################
# O LÀ FRUIT 
# ĂN FRUIT ĐỂ ĐI XUYÊN TƯỜNG

playing = True
nghia = False
while playing:
    os.system ('clear')
    for y in range (map_sokoban["size_y"]):
        for x in range (map_sokoban["size_x"]):
            pic = '- '
            for des in destinations:
                if des["x"] == x and des["y"] == y:
                    pic = 'D '
            for box in boxes:
                if box['x'] == x and box['y'] ==y:
                    pic = 'B '
            for wall in walls:
                if wall["x"] == x and wall['y'] ==y:
                    pic = "* "
            if x==fruit['x'] and y==fruit['y']:
                pic = 'O '
            if x==player["x"] and y==player["y"] :
                pic = 'P '
            print (pic, end='')
        print()       
    ##################

    win = True
    for box in boxes:
        if box not in destinations:
            win = False
    if win == True:
        print ("You win")
        playing = False
        break

    move = input ("Your move: ").upper()
    dx = 0
    dy = 0
    if move == "W":
        dy=-1
    elif move =="S":
        dy =1
    elif move == "D":
        dx =1
    elif move == "A":
        dx=-1
    else :
        playing = False
        break
    dang = True
    if 0 <= player['x'] + dx < map_sokoban['size_x'] \
        and  0 <= player['y'] + dy < map_sokoban['size_y']:
        for box in boxes:
            if player['x']+dx == box['x'] and player['y']+dy == box['y']:
                if not  0 <= (box['x'] + dx) < map_sokoban['size_x']\
                or not 0 <= (box['y']) + dy < map_sokoban['size_y']:
                    dang= False
                for wall in walls:
                    if box['x'] + dx == wall['x'] and box['y'] + dy == wall['y']:
                        dang = False
                for box2 in boxes:
                    if box['x'] + dx == box2['x'] and box['y'] + dy == box2['y']:
                        dang= False
                if dang:
                    box['y']+=dy
                    box['x']+=dx
        if player['x']==fruit['x'] and player['y']==fruit['y']:
            fruit = {'x':-1,'y':-1}
            nghia = True
        if nghia == False:
            for wall in walls:
                if (player['x'] + dx == wall['x'] and player['y'] + dy == wall['y']):
                    dang= False
        if dang:
            player['x']+=dx
            player['y']+=dy
    