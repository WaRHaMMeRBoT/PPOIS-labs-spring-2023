import time
import json
import pygame
import random

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((970, 600))
pygame.display.set_caption("Jewel Quest")
icon = pygame.image.load('Images/Icon.png')
pygame.display.set_icon(icon)

max_result = 0
with open('Record.json', 'r') as json_file:
    max_res = json.load(json_file)
    max_result = max_res['Record']

background = pygame.image.load('Images/Background.png')
screen.blit(background, (0, 0))
start = pygame.image.load('Images/Start.png')
screen.blit(start, (420, 70))
reference = pygame.image.load('Images/Reference.png')
screen.blit(reference, (420, 200))
leaderboard = pygame.image.load('Images/Leaderboard.png')
screen.blit(leaderboard, (420, 330))
ex = pygame.image.load('Images/Exit.png')
screen.blit(ex, (420, 460))
mode1 = pygame.image.load('Images/Mode1.png')
mode2 = pygame.image.load('Images/Mode2.png')

myFont = pygame.font.Font('RobotoSlab-ExtraBold.ttf', 65)
rules = myFont.render('Правила:', True, 'Black')

myFont1 = pygame.font.Font('RobotoSlab-ExtraBold.ttf', 40)
text_reference1 = myFont1.render('1 режим - игра на время.', True, 'Black')
text_reference2 = myFont1.render('2 режим - игра на очки.', True, 'Black')
text_reference3 = myFont1.render('2 режим содержит ещё 3 режима: ', True, 'Black')
text_reference4 = myFont1.render('Режим с полем 5x5.', True, 'Black')
text_reference5 = myFont1.render('Режим с полем 7x7.', True, 'Black')
text_reference6 = myFont1.render('Режим с полеме 10x10.', True, 'Black')

record = myFont.render('Рекорд: ', True, 'Black')
result = myFont.render('Прошлый результат: ', True, 'Black')

myFont2 = pygame.font.Font('RobotoSlab-ExtraBold.ttf', 30)
score = myFont2.render('Score', True, (220, 220, 220))

stone1 = pygame.image.load('Images/Stone1.png')
stone2 = pygame.image.load('Images/Stone2.png')
stone3 = pygame.image.load('Images/Stone3.png')
stone4 = pygame.image.load('Images/Stone4.png')
stone5 = pygame.image.load('Images/Stone5.png')
stone6 = pygame.image.load('Images/Stone6.png')

timer = pygame.image.load('Images/Timer.png')

plate = pygame.image.load('Images/Plate.png')

sound = pygame.mixer.Sound('Music.mp3')
sound.play()

game_points = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

game_points_temp = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

game_field = [[]]

game_field_temp = [[]]

left = 0
right = 0
top = 0
bottom = 0

points = 0
limit = 0
FPS = 60
textTime = myFont2.render('Время:', True, (220, 220, 220))

field = pygame.Surface((560, 560))
field.fill((244, 164, 96))


def newMenu():
    screen.blit(background, (0, 0))
    screen.blit(mode1, (420, 120))
    screen.blit(mode2, (420, 250))


def createPlate():
    screen.blit(plate, (740, 190))
    screen.blit(score, (807, 195))


def getCell(ind_y, ind_x):
    cell = [0, 0]
    if 20 < ind_y < 580:
        cell[0] = int((ind_y - 20) / 70)
    if 170 < ind_x < 730:
        cell[1] = int((ind_x - 170) / 70)
    return cell


def getCords(ind_x, ind_y):
    dott = [175, 25]
    number_x = 0
    number_y = 0
    for i in range(ind_x):
        number_x += 70
    for i in range(ind_y):
        number_y += 70
    dott[0] = 175 + number_x
    dott[1] = 25 + number_y
    return dott


def genBack():
    screen.blit(background, (0, 0))


def genReference():
    genBack()
    screen.blit(rules, (350, 20))
    screen.blit(text_reference1, (10, 100))
    screen.blit(text_reference2, (10, 140))
    screen.blit(text_reference3, (10, 180))
    screen.blit(text_reference4, (25, 220))
    screen.blit(text_reference5, (25, 260))
    screen.blit(text_reference6, (25, 300))


def genESC():
    genBack()
    screen.blit(start, (420, 70))
    screen.blit(reference, (420, 200))
    screen.blit(leaderboard, (420, 330))
    screen.blit(ex, (420, 460))


def genTable():
    screen.blit(field, (170, 20))
    pygame.draw.rect(screen, (0, 0, 0), (165, 15, 570, 570), 5)
    pointer_x = 240
    for index1 in range(8):
        pygame.draw.line(screen, (0, 0, 0), [pointer_x, 20], [pointer_x, 580])
        pointer_x += 70

    pointer_y = 90
    for index1 in range(8):
        pygame.draw.line(screen, (0, 0, 0), [170, pointer_y], [730, pointer_y])
        pointer_y += 70


def createField():
    game_field.clear()
    genTable()

    cord_x = 175
    cord_y = 25
    for index1 in range(8):
        timeGameField = []
        for j in range(8):
            if getRandomNumber() == 1:
                game_points[index1][j] = 1
                screen.blit(stone1, (cord_x, cord_y))
                timeGameField.append(stone1)
            elif getRandomNumber() == 2:
                game_points[index1][j] = 2
                screen.blit(stone2, (cord_x, cord_y))
                timeGameField.append(stone2)
            elif getRandomNumber() == 3:
                game_points[index1][j] = 3
                screen.blit(stone3, (cord_x, cord_y))
                timeGameField.append(stone3)
            elif getRandomNumber() == 4:
                game_points[index1][j] = 4
                screen.blit(stone4, (cord_x, cord_y))
                timeGameField.append(stone4)
            elif getRandomNumber() == 5:
                game_points[index1][j] = 5
                screen.blit(stone5, (cord_x, cord_y))
                timeGameField.append(stone5)
            else:
                game_points[index1][j] = 6
                screen.blit(stone6, (cord_x, cord_y))
                timeGameField.append(stone6)
            cord_x += 70
        game_field.append(timeGameField)
        cord_x = 175
        cord_y += 70


def genNewField():
    cord_x = 175
    cord_y = 25
    for index1 in range(8):
        for j in range(8):
            screen.blit(game_field[index1][j], (cord_x, cord_y))
            cord_x += 70
        cord_x = 175
        cord_y += 70


def create_new_table_line(line):
    global left
    global right
    while left < right + 1:
        if getRandomNumber() == 1:
            game_points[line][left] = 1
            game_field[line][left] = stone1
        elif getRandomNumber() == 2:
            game_points[line][left] = 2
            game_field[line][left] = stone2
        elif getRandomNumber() == 3:
            game_points[line][left] = 3
            game_field[line][left] = stone3
        elif getRandomNumber() == 4:
            game_points[line][left] = 4
            game_field[line][left] = stone4
        elif getRandomNumber() == 5:
            game_points[line][left] = 5
            game_field[line][left] = stone5
        else:
            game_points[line][left] = 6
            game_field[line][left] = stone6
        left += 1


def create_new_table_column(column):
    global bottom
    global top
    while bottom < top + 1:
        if getRandomNumber() == 1:
            game_points[bottom][column] = 1
            game_field[bottom][column] = stone1
        elif getRandomNumber() == 2:
            game_points[bottom][column] = 2
            game_field[bottom][column] = stone2
        elif getRandomNumber() == 3:
            game_points[bottom][column] = 3
            game_field[bottom][column] = stone3
        elif getRandomNumber() == 4:
            game_points[bottom][column] = 4
            game_field[bottom][column] = stone4
        elif getRandomNumber() == 5:
            game_points[bottom][column] = 5
            game_field[bottom][column] = stone5
        else:
            game_points[bottom][column] = 6
            game_field[bottom][column] = stone6
        bottom += 1


def genField(stone, dots, move1, move2):
    x = 175
    y = 25
    for i in range(8):
        for j in range(8):
            if i == dots[0] and y == dots[1]:
                screen.blit(game_field[i][j], (move1, move2))
            else:
                screen.blit(game_field[i][j], (x, y))
            x += 70
        x = 175
        y += 70


def getRandomNumber():
    return random.randint(1, 6)


flag = True
bool_replace = True


def findMatchesLine(num1, num2):
    global left
    global right
    now_game_point = game_points[num1][num2]
    count = 0
    item = num2
    while game_points[num1][num2] == game_points[num1][item]:
        count += 1
        right = item
        if item < 7:
            item += 1
        else:
            break
    item = num2 - 1
    while game_points[num1][num2] == game_points[num1][item]:
        count += 1
        left = item
        if item > 1:
            item -= 1
        else:
            break
    return count


def findMatchesColumn(num1, num2):
    global bottom
    global top
    now_game_point = game_points[num1][num2]
    count = 0
    item = num1
    while game_points[num1][num2] == game_points[item][num2]:
        count += 1
        top = item
        if item < 7:
            item += 1
        else:
            break
    item = num1 - 1
    while game_points[num1][num2] == game_points[item][num2]:
        count += 1
        bottom = item
        if item > 0:
            item -= 1
        else:
            break
    return count


def replacement(square1, square2):
    dot = getCords(square1[1], square1[0])

    temp1 = game_points[square1[0]][square1[1]]
    temp2 = game_field[square1[0]][square1[1]]

    game_points[square1[0]][square1[1]] = game_points[square2[0]][square2[1]]
    game_field[square1[0]][square1[1]] = game_field[square2[0]][square2[1]]

    if abs(square1[0] - square2[0]) == 1:
        index_x = dot[0] - 70
        while index_x < dot[0]:
            genBack()
            genTable()
            createPlate()
            genTimer()
            genField(game_field[square1[0]][square1[1]], dot, index_x, dot[1])
            index_x += 8

    elif abs(square1[1] - square2[1]) == 1:
        index_y = dot[1] - 70
        while index_y < dot[1]:
            genBack()
            genTable()
            createPlate()
            genTimer()
            genField(game_field[square1[0]][square1[1]], dot, dot[0], index_y)
            index_y += 8

    dot = getCords(square2[1], square2[0])

    game_points[square2[0]][square2[1]] = temp1
    game_field[square2[0]][square2[1]] = temp2

    if abs(square1[0] - square2[0]) == 1:
        index_x = dot[0] - 70
        while index_x < dot[0]:
            genBack()
            genTable()
            createPlate()
            genTimer()
            genField(game_field[square2[0]][square2[1]], dot, index_x, dot[1])
            index_x += 8

    elif abs(square1[1] - square2[1]) == 1:
        index_y = dot[1] - 70
        while index_y < dot[1]:
            genBack()
            genTable()
            createPlate()
            genTimer()
            genField(game_field[square2[0]][square2[1]], dot, dot[0], index_y)
            index_y += 8
    # if abs(square1[0] - square2[0]) == 1:
    #     index_x = dot[0] - 70
    #     while index_x < dot[0]:
    #         screen.blit(game_field[square2[0]][square2[1]], (index_x, dot[1]))
    #         index_x += 1
    #         time.sleep(0.005)
    # elif abs(square1[1] - square2[1]) == 1:
    #     index_y = dot[1] - 70
    #     while index_y < dot[1]:
    #         screen.blit(game_field[square2[0]][square2[1]], (dot[0], index_y))
    #         index_y += 1
    #         time.sleep(0.005)
    # screen.blit(game_field[square2[0]][square2[1]], (dot[0], dot[1]))


pre_points = 0


def getLeaderboard():
    rec = myFont.render(str(max_result), True, 'Black')
    now_res = myFont.render(str(pre_points), True, 'Black')
    screen.blit(rec, (430, 195))
    screen.blit(now_res, (430, 450))


def genTimer():
    scorePoints = myFont2.render(str(points), True, (220, 220, 220))
    timeNow = myFont2.render(str(int(limit / 2)), True, (220, 220, 220))
    screen.blit(textTime, (30, 30))
    screen.blit(scorePoints, (835, 235))
    screen.blit(timer, (5, 75))
    screen.blit(timeNow, (75, 95))


running = True

while running:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            newMenu()

            running1 = True

            while running1:

                pygame.display.update()

                for event1 in pygame.event.get():
                    if event1.type == pygame.KEYDOWN and event1.key == pygame.K_4:
                        createField()

                        running2 = True
                        x1 = 0
                        y1 = 0
                        x2 = 0
                        y2 = 0
                        pressing = 0

                        while running2:

                            pygame.display.update()
                            createPlate()
                            genTimer()
                            time.sleep(0.5)
                            if limit == 188:
                                limit = 0
                                genESC()
                                running2 = False
                                running1 = False
                            limit += 1

                            for event2 in pygame.event.get():
                                if event2.type == pygame.MOUSEBUTTONDOWN:
                                    if pressing == 0:
                                        x1 = event2.pos[0]
                                        y1 = event2.pos[1]
                                        pressing += 1

                                    elif pressing == 1:
                                        x2 = event2.pos[0]
                                        y2 = event2.pos[1]
                                        cell1 = getCell(y1, x1)
                                        cell2 = getCell(y2, x2)

                                        if (abs(cell1[0] - cell2[0]) <= 1 and abs(cell1[1] - cell2[1]) == 0) or (
                                                abs(cell1[1] - cell2[1]) <= 1 and abs(cell1[0] - cell2[0]) == 0):
                                            replacement(cell1, cell2)

                                            amount = findMatchesLine(cell1[0], cell1[1])
                                            if amount >= 3:
                                                points += amount * game_points[cell1[0]][cell1[1]]
                                                create_new_table_line(cell1[0])
                                                bool_replace = False

                                            amount = findMatchesLine(cell2[0], cell2[1])
                                            if amount >= 3:
                                                points += amount * game_points[cell2[0]][cell2[1]]
                                                create_new_table_line(cell2[0])
                                                bool_replace = False

                                            amount = findMatchesColumn(cell1[0], cell1[1])
                                            if amount >= 3:
                                                points += amount * game_points[cell1[0]][cell1[1]]
                                                create_new_table_column(cell1[1])
                                                bool_replace = False

                                            amount = findMatchesColumn(cell2[0], cell2[1])
                                            if amount >= 3:
                                                points += amount * game_points[cell2[0]][cell2[1]]
                                                create_new_table_column(cell2[1])
                                                bool_replace = False

                                            if bool_replace:
                                                replacement(cell1, cell2)
                                            else:
                                                bool_replace = True
                                            left = 0
                                            right = 0
                                            top = 0
                                            bottom = 0
                                            genNewField()
                                            pre_points = points
                                        pressing = 0

                                elif event2.type == pygame.KEYDOWN and event2.key == pygame.K_ESCAPE:
                                    genESC()
                                    running2 = False
                                    running1 = False

                                elif event2.type == pygame.KEYDOWN and event2.key == pygame.K_0:
                                    genBack()
                                    running = False
                                    running1 = False
                                    running2 = False
                                    pygame.quit()


                    elif event1.type == pygame.KEYDOWN and event1.key == pygame.K_ESCAPE:
                        genESC()
                        running1 = False

                    elif event1.type == pygame.KEYDOWN and event1.key == pygame.K_0:
                        genBack()
                        running = False
                        running1 = False
                        pygame.quit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            genReference()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            genBack()
            screen.blit(record, (345, 80))
            screen.blit(result, (155, 333))
            getLeaderboard()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            screen.blit(background, (0, 0))
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            genESC()

        if max_result < points:
            max_result = points
        data = {'Record': max_result,
                'Latest result': pre_points
                }
        with open('Record.json', 'w') as json_file:
            json.dump(data, json_file)
        points = 0
