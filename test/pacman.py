# game object:
import os
map_pacman = {
    "size_x":8,
    "size_y":8
}
dogs = [
    {'x':4,'y':0},
    {'x':7,'y':1}
    ]

player = {'x':5,'y':2}

fruits = [
    {'x':0,'y':2},
    {'x':7,'y':6},
    ]

walls = [
    {'x':2,'y':0},
    {'x':2,'y':1},
    {'x':2,'y':2},
    {'x':7,'y':4},
    {'x':6,'y':4},
    {'x':5,'y':4},
    {'x':0,'y':6},
    {'x':1,'y':6},
    {'x':2,'y':6}
    ]

###############
count = 0
playing = True
while playing:
    os.system ('clear')
    for y in range (map_pacman["size_y"]):
        for x in range (map_pacman["size_x"]):
            pic = '- '
            for fruit in fruits:
                if fruit['x'] == x and fruit['y'] == y:
                    pic = 'O '
                if fruit['x'] == player['x'] and fruit['y'] == player['y']:
                    fruit['x'] = -1
                    fruit['y'] = -1
                    count += 1
            for wall in walls:
                if wall['x'] == x and wall['y'] == y:
                    pic = '# '
            for dog in dogs :
                if dog['x'] == x and dog ['y'] == y:
                    pic = 'D '
            if player['x'] == x and player ['y'] == y:
                pic = 'P '
            print (pic, end='')
        print()

##############
    
    if count == 2:
        print ("You win")
        break

    move = input ("Your move: ")
    dx = 0
    dy = 0
    if move == 'w':
        dy = -1
    elif move == 's':
        dy = 1
    elif  move == 'a':
        dx = -1
    elif  move == 'd':
        dx = 1
    else :
        break
    dang = True
    if  0 <= player['x']+dx < map_pacman['size_x'] \
        and 0 <= player['y']+dy < map_pacman['size_y']:
        for wall in walls:
            if player['x'] + dx == wall['x'] \
            and player['y'] + dy == wall['y']:
                dang = False
        if dang:
            player ['x'] += dx
            player ['y'] += dy
            for dog in dogs:
                lx = 0
                ly = 0
                hai = True
                dat = dog['x'] - player['x']
                nghia = dog['y'] - player['y']
            
                if nghia > 0 :
                    ly = -1
                elif nghia < 0 :
                    ly = 1
                elif dat > 0:
                    lx = -1
                elif dat < 0:
                    lx = 1
                for wall in walls :
                    if wall['x'] == dog['x']+lx and wall['y'] == dog['y']+ly:
                        hai = False
                if hai:
                    dog['y'] += ly
                    dog['x'] += lx
        for dog in dogs:
            if player in dogs:
                print ('Game over')
                playing = False
                break