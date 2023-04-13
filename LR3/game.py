import json
import math
import os
import random

import pygame

import draw
import sound


def init_2DArray(width, height):
    return [[random.randrange(1, 7) for x in range(width)] for y in range(height)]


def match_exists(board):
    # Checks rows
    for y in range(len(board)):
        streak = 1
        for x in range(1, len(board[y])):
            if board[y][x] == board[y][x - 1] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak >= 3:  # A streak of 3 matching tiles
                return True
    # Checks columns
    for x in range(len(board[0])):
        streak = 1
        for y in range(1, len(board)):
            if board[y][x] == board[y - 1][x] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak >= 3:
                return True
    return False


# Sets up the board to have no matches
def format_board(board):
    while match_exists(board):
        for y in range(len(board)):
            for x in range(len(board[y])):
                board[y][x] = random.randrange(1, 7)
    return board


# Displays the text-based array representation of the board
def show_board(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end=" ")
        print()


# Updates and pauses the screen
def display_pause(clock, x):
    pygame.display.flip()  # updates screen
    clock.tick(x)  # stops execution for 1/x seconds since the last tick


# Checks if the second selected tile is beside the first tile
def isAdjacent(selected_x, selected_y, x, y):
    if selected_x + 1 == x and selected_y == y:
        return True
    elif selected_x - 1 == x and selected_y == y:
        return True
    elif selected_y + 1 == y and selected_x == x:
        return True
    elif selected_y - 1 == y and selected_x == x:
        return True
    return False


def swap(array, x1, y1, x2, y2):
    temp = array[y1][x1]
    array[y1][x1] = array[y2][x2]
    array[y2][x2] = temp


def elim_matches(board):
    elim_list = []
    # Checks the rows for matches
    for y in range(len(board)):
        streak = 1
        for x in range(1, len(board[y])):
            if board[y][x] == board[y][x - 1] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak == 3:
                elim_list += [[y, x - 2]]
                elim_list += [[y, x - 1]]
                elim_list += [[y, x]]
            elif streak > 3:
                elim_list += [[y, x]]
    # Checks columns for matches
    for x in range(len(board[0])):
        streak = 1
        for y in range(1, len(board)):
            if board[y][x] == board[y - 1][x] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak == 3:
                elim_list += [[y - 2, x]]
                elim_list += [[y - 1, x]]
                elim_list += [[y, x]]
            elif streak > 3:
                elim_list += [[y, x]]

    # Turns all the found matches to zero
    for i in range(len(elim_list)):
        y = elim_list[i][0]
        x = elim_list[i][1]
        board[y][x] = 0

    return len(elim_list)


# Returns if the board has any empty tiles
def board_filled(board):
    for y in range(len(board)):
        if 0 in board[y]:  # 0 is an empty tile
            return False
    return True


# Drops any tiles with an empty space under by one
# Traverses the 2D array from the bottom left corner up each column
def drop_tiles(board):
    for x in range(len(board[0])):
        for y in range(len(board) - 2, -1, -1):  # goes bottom to top of each column
            if board[y + 1][x] == 0 and board[y][x] != 0:
                swap(board, x, y + 1, x, y)


# Fills any empty tiles at the top of the board
def fill_top(board):
    for x in range(len(board[0])):
        if board[0][x] == 0:
            board[0][x] = random.randrange(1, 7)


def main():
    with open("difficulty.json") as file:
        difficulty = json.load(file)
        file.close()
    # Initial game variables
    WIDTH = 7
    HEIGHT = 9
    BOX_LENGTH = 70
    selected = False
    selected_x = None
    selected_y = None
    score = 0
    turns_left = int(10 * difficulty)
    GOAL_SCORE = 100 * difficulty
    exit_game = False
    gameover_displayed = False

    os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centers the window that will be generated

    board = init_2DArray(WIDTH, HEIGHT)
    format_board(board)

    pygame.init()  # loads all pygame modules
    sound.load()
    global screen
    global gui_font
    gui_font = pygame.font.Font(None, 30)
    screen = draw.create_screen(WIDTH, HEIGHT, BOX_LENGTH)
    clock = pygame.time.Clock()

    button1 = Button('Menu', 100, 40, (500, 500), 5)

    draw.window(board, turns_left, score, GOAL_SCORE)
    pygame.display.flip()  # updates screen

    # Game Loop
    while not exit_game:
        while turns_left > 0 and not exit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # window exit button
                    exit_game = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    coord_pair = pygame.mouse.get_pos()  # tuple from the left-click
                    x = math.floor(coord_pair[0] / BOX_LENGTH)
                    y = math.floor(coord_pair[1] / BOX_LENGTH)
                    if x < WIDTH and y < HEIGHT:
                        if selected == False:  # No tile was previously selected
                            selected = True
                            selected_x = x
                            selected_y = y
                            draw.selected(x, y)
                        elif selected == True:
                            if isAdjacent(selected_x, selected_y, x, y):
                                swap(board, selected_x, selected_y, x, y)
                                draw.window(board, turns_left, score, GOAL_SCORE)
                                display_pause(clock, 2.5)

                                if match_exists(board):
                                    turns_left -= 1
                                    turn_score = 0
                                    combo_count = 1

                                    # Loops until no more matches
                                    while match_exists(board):
                                        turn_score += elim_matches(board)
                                        draw.window(board, turns_left, score,
                                                    GOAL_SCORE)
                                        sound.play_effect("pop")
                                        display_pause(clock, 2.5)

                                        while not board_filled(board):
                                            # Drops tiles and fills board until full
                                            drop_tiles(board)
                                            fill_top(board)
                                            draw.window(board, turns_left, score,
                                                        GOAL_SCORE)
                                            display_pause(clock, 2.5)

                                        combo_count += 1

                                    combo_count -= 1
                                    score += turn_score * combo_count
                                    draw.window(board, turns_left, score,
                                                GOAL_SCORE)
                                    pygame.display.flip()

                                    if combo_count > 1:
                                        sound.play_combo(combo_count)
                                        draw.combo_msg(combo_count)
                                        pygame.display.flip()
                                        pygame.time.delay(2000)
                                        draw.window(board, turns_left, score,
                                                    GOAL_SCORE)
                                        pygame.display.flip()


                                elif not match_exists(board):
                                    # swaps tiles back
                                    swap(board, selected_x, selected_y, x, y)
                                    draw.window(board, turns_left, score,
                                                GOAL_SCORE)
                                    pygame.display.flip()

                            elif not isAdjacent(selected_x, selected_y, x, y):
                                # Visually deselects the first tile
                                draw.window(board, turns_left, score, GOAL_SCORE)
                                pygame.display.flip()

                            selected = False
                            selected_x = None
                            selected_y = None

                if button1.pressed:
                    exit_game = True

            button1.draw()

            pygame.display.update()
            display_pause(clock, 60)

        if button1.pressed:
            print(button1.pressed)
            button1.pressed = False
            exit_game = True
        else:
            if not gameover_displayed:
                if score >= GOAL_SCORE:
                    draw.win()
                    sound.play_effect("win")
                else:
                    draw.lose()
                    sound.play_effect("lose")
                gameover_displayed = True
                pygame.display.flip()

                a = pygame.time.get_ticks() + 5000
                while True:
                    if pygame.time.get_ticks() > a or exit_game == True:
                        break

                exit_game = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # window exit button
                exit_game = True


class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'
        # text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'
