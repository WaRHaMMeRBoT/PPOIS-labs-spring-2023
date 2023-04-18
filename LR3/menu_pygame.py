import pygame
import sys
from pygame.locals import *
import random
import time
import datetime
import sqlite3
import math
import os
from ScoreTable import formalize_rows as rows
from ScoreTable import find_max,insert

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Jewel quest')
screen = pygame.display.set_mode((400, 425),0,32)
s = 'sound'
width = 400
height = 400
scoreboard_height = 25
complete_level = pygame.mixer.Sound(os.path.join(s,'complete_level.wav'))
gem_match = pygame.mixer.Sound(os.path.join(s,'gem_match.wav'))

start_ticks=pygame.time.get_ticks() 

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
gem_colors = ['blue', 'green', 'orange', 'pink', 'purple', 'red', 'teal', 'yellow'] 
gem_width = 40
gem_height = 40
gem_size = (gem_width, gem_height)

class Gem:
    
    def __init__(self, row_num, col_num):
        # set the gem's position on the board
        self.row_num = row_num
        self.col_num = col_num
        # assign a random image
        self.color = random.choice(gem_colors)
        image_name = f'swirl_{self.color}.png'
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.smoothscale(self.image, gem_size)
        self.rect = self.image.get_rect()
        self.rect.left = col_num * gem_width
        self.rect.top = row_num * gem_height
    def draw(self):
        screen.blit(self.image, self.rect)

    def snap(self):
        self.snap_row()
        self.snap_col()
        
    def snap_row(self):
        self.rect.top = self.row_num * gem_height
        
    def snap_col(self):
        self.rect.left = self.col_num * gem_width
board = []
for row_num in range(height // gem_height):
    
    # add a new row to the board
    board.append([])
    
    for col_num in range(width // gem_width):
        
        # create the gem and add it to the board
        gem = Gem(row_num, col_num)
        board[row_num].append(gem)
        


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 



def swap(gem1, gem2):
    
    temp_row = gem1.row_num
    temp_col = gem1.col_num
    
    gem1.row_num = gem2.row_num
    gem1.col_num = gem2.col_num
    
    gem2.row_num = temp_row
    gem2.col_num = temp_col
    
    # update the candies on the board list
    board[gem1.row_num][gem1.col_num] = gem1
    board[gem2.row_num][gem2.col_num] = gem2
    
    # snap them into their board positions
    gem1.snap()
    gem2.snap()
    

def find_matches(gem, matches):
    
    # add the gem to the set
    matches.add(gem)
    
    # check the gem above if it's the same color
    if gem.row_num > 0:
        neighbor = board[gem.row_num - 1][gem.col_num]
        if gem.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    # check the gem below if it's the same color
    if gem.row_num < height / gem_height - 1:
        neighbor = board[gem.row_num + 1][gem.col_num]
        if gem.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    # check the gem to the left if it's the same color
    if gem.col_num > 0:
        neighbor = board[gem.row_num][gem.col_num - 1]
        if gem.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    # check the gem to the right if it's the same color
    if gem.col_num < width / gem_width - 1:
        neighbor = board[gem.row_num][gem.col_num + 1]
        if gem.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    return matches
    

def match_three(gem):
    
    matches = find_matches(gem, set())
    if len(matches) >= 3:
        return matches
    else:
        return set()
    

def main_menu():
    while True:
 
        screen.fill((173, 216, 230))
        draw_text('Game mode', font, (0,0,0), screen, 150, 40)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(150, 100, 100, 50)
        button_2 = pygame.Rect(150, 180, 100, 50)
        button_3 = pygame.Rect(150, 260, 100, 50)
        button_4 = pygame.Rect(150, 340, 100, 50)
        button_5 = pygame.Rect(10, 100, 100, 50)
        button_6 = pygame.Rect(10, 180, 100, 50)
        button_7 = pygame.Rect(10, 260, 100, 50)
        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                level_1()
        if button_3.collidepoint((mx, my)):
            if click:
                level_2()
        if button_4.collidepoint((mx, my)):
            if click:
                level_3()
        if button_5.collidepoint((mx, my)):
            if click:
                score()
        if button_6.collidepoint((mx, my)):
            if click:
                help()
        if button_7.collidepoint((mx, my)):
            if click:
                pygame.quit()        
        pygame.draw.rect(screen, (139, 0, 139), button_1)
        pygame.draw.rect(screen, (106, 90, 205), button_2)
        pygame.draw.rect(screen, (75, 0, 130), button_3)
        pygame.draw.rect(screen, (72, 61, 139), button_4)
        pygame.draw.rect(screen, (148,0,211), button_5)
        pygame.draw.rect(screen, (153,0,76), button_6)
        pygame.draw.rect(screen, (235,60,95), button_7)
        #writing text on top of button
        draw_text('Time ', font, (255,255,255), screen, 170, 115)
        draw_text(' Score 1', font, (255,255,255), screen, 155, 195)
        draw_text(' Score 2', font, (255,255,255), screen, 155, 275)
        draw_text(' Score 3', font, (255,255,255), screen, 155, 355)
        draw_text(' Highscore', font, (255,255,255), screen, 5, 115)
        draw_text('     Help', font, (255,255,255), screen, 5, 195)
        draw_text('    Close', font, (255,255,255), screen, 5, 275)



        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        
 
"""
This function is called when the "Time" button is clicked.
"""
 
    
def game():
    
    screen.fill((139, 0, 139))
    score = 0
    moves = 0
    time_limit = 60
    swapped_gem = None
    clicked_gem = None
    click_x = None
    click_y = None
    running = True
    def draw():
    
    # draw the background
        pygame.draw.rect(screen, (173, 216, 230), (0, 0, width, height + scoreboard_height))
        
        # draw the candies
        for row in board:
            for gem in row:
                gem.draw()
        
        # display the score and moves
        font = pygame.font.SysFont('monoface', 18)
        score_text = font.render(f'Score: {score}', 1, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(width / 4, height + scoreboard_height / 2))
        screen.blit(score_text, score_text_rect)
        
        timer_text = font.render(f'Timer: {seconds_format}', 1, (0, 0, 0))
        timer_text_rect = timer_text.get_rect(center=(width * 2 / 4, height + scoreboard_height / 2))
        screen.blit(timer_text, timer_text_rect)

        moves_text = font.render(f'Moves: {moves}', 1, (0, 0, 0))
        moves_text_rect = moves_text.get_rect(center=(width * 3 / 4, height + scoreboard_height / 2))
        screen.blit(moves_text, moves_text_rect)   
    while running:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        seconds_format = math.trunc(seconds)  
        if seconds>time_limit:
            running = False
            if score > find_max(): 
                pygame.mixer.Sound.play(complete_level)
                win_screen(score)
            else:
                pygame.mixer.Sound.play(complete_level)
                complete_level_screen()
            # 
            #         insert('Kain',score)
        # set of matching candies
        matches = set()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
                
            # detect mouse click
            if clicked_gem is None and event.type == MOUSEBUTTONDOWN:
                
                # get the gem that was clicked on
                for row in board:
                    for gem in row:
                        if gem.rect.collidepoint(event.pos):
                            
                            clicked_gem = gem
                            
                            # save the coordinates of the point where the user clicked
                            click_x = event.pos[0]
                            click_y = event.pos[1]
                            
            # detect mouse motion
            if clicked_gem is not None and event.type == MOUSEMOTION:
                
                # calculate the distance between the point the user clicked on
                # and the current location of the mouse cursor
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])
                
                # reset the position of the swapped gem if direction of mouse motion changed
                if swapped_gem is not None:
                    swapped_gem.snap()
                    
                # determine the direction of the neighboring gem to swap with
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'
                    
                # if moving left/right, snap the clicked gem to its row position
                # otherwise, snap it to its col position
                if direction in ['left', 'right']:
                    clicked_gem.snap_row()
                else:
                    clicked_gem.snap_col()
                    
                # if moving the clicked gem to the left,
                # make sureit's not on the first col
                if direction == 'left' and clicked_gem.col_num > 0:
                    
                    # get the gem to the left
                    swapped_gem = board[clicked_gem.row_num][clicked_gem.col_num - 1]
                    
                    # move the two candies
                    clicked_gem.rect.left = clicked_gem.col_num * gem_width - distance_x
                    swapped_gem.rect.left = swapped_gem.col_num * gem_width + distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.left <= swapped_gem.col_num * gem_width + gem_width / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem to the right,
                # make sure it's not on the last col
                if direction == 'right' and clicked_gem.col_num < width / gem_width - 1:
                    
                    # get the gem to the right
                    swapped_gem = board[clicked_gem.row_num][clicked_gem.col_num + 1]
                    
                    # move the two candies
                    clicked_gem.rect.left = clicked_gem.col_num * gem_width + distance_x
                    swapped_gem.rect.left = swapped_gem.col_num * gem_width - distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.left >= swapped_gem.col_num * gem_width - gem_width / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem up,
                # make sure it's not on the first row
                if direction == 'up' and clicked_gem.row_num > 0:
                    
                    # get the gem above
                    swapped_gem = board[clicked_gem.row_num - 1][clicked_gem.col_num]
                    
                    # move the two candies
                    clicked_gem.rect.top = clicked_gem.row_num * gem_height - distance_y
                    swapped_gem.rect.top = swapped_gem.row_num * gem_height + distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.top <= swapped_gem.row_num * gem_height + gem_height / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem down,
                # make sure it's not on the last row
                if direction == 'down' and clicked_gem.row_num < height / gem_height - 1:
                    
                    # get the gem below
                    swapped_gem = board[clicked_gem.row_num + 1][clicked_gem.col_num]
                    
                    # move the two candies
                    clicked_gem.rect.top = clicked_gem.row_num * gem_height + distance_y
                    swapped_gem.rect.top = swapped_gem.row_num * gem_height - distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.top >= swapped_gem.row_num * gem_height - gem_height / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
            # detect mouse release
            if clicked_gem is not None and event.type == MOUSEBUTTONUP:
                
                # snap the candies back to their original positions on the grid
                clicked_gem.snap()
                clicked_gem = None
                if swapped_gem is not None:
                    swapped_gem.snap()
                    swapped_gem = None
                
        draw()
        pygame.display.update()
        
        # check if there's at least 3 matching candies
        if len(matches) >= 3:
            
            # add to score
            score += len(matches)
            
            # animate the matching candies shrinking
            while len(matches) > 0:
                
                clock.tick(100)
                
                # decrease width and height by 1
                for gem in matches:
                    new_width = gem.image.get_width() - 1
                    new_height = gem.image.get_height() - 1
                    new_size = (new_width, new_height)
                    gem.image = pygame.transform.smoothscale(gem.image, new_size)
                    gem.rect.left = gem.col_num * gem_width + (gem_width - new_width) / 2
                    gem.rect.top = gem.row_num * gem_height + (gem_height - new_height) / 2
                    
                # check if the candies have shrunk to zero size
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        gem = board[row_num][col_num]
                        if gem.image.get_width() <= 0 or gem.image.get_height() <= 0:
                            matches.remove(gem)
                            
                            # generate a new gem
                            board[row_num][col_num] = Gem(row_num, col_num)
                # pygame.mixer.Sound.play(gem_match)            
                draw()
       
                pygame.display.update()
        

"""
This functions is called when the "level *" button is clicked.
"""
def level_1():
    screen.fill((106, 90, 205))
    score = 0
    moves = 0
    score_limit = 10
    swapped_gem = None
    clicked_gem = None
    click_x = None
    click_y = None
    running = True
    def draw():
    
    # draw the background
        pygame.draw.rect(screen, (173, 216, 230), (0, 0, width, height + scoreboard_height))
        
        # draw the candies
        for row in board:
            for gem in row:
                gem.draw()
        
        # display the score and moves
        font = pygame.font.SysFont('monoface', 18)
        score_text = font.render(f'Score: {score} / {score_limit}', 1, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(width / 5, height + scoreboard_height / 2))
        screen.blit(score_text, score_text_rect)
        
        timer_text = font.render(f'Timer: {seconds_format}', 1, (0, 0, 0))
        timer_text_rect = timer_text.get_rect(center=(width * 2 / 5, height + scoreboard_height / 2))
        screen.blit(timer_text, timer_text_rect)

        moves_text = font.render(f'Moves: {moves} ', 1, (0, 0, 0))
        moves_text_rect = moves_text.get_rect(center=(width * 3 / 5, height + scoreboard_height / 2))
        screen.blit(moves_text, moves_text_rect)

        level_text = font.render(f'Level 1 ', 1, (0, 0, 0))
        level_text_rect = level_text.get_rect(center=(width * 4 / 5, height + scoreboard_height / 2))
        screen.blit(level_text, level_text_rect)

        
    while running:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        seconds_format = math.trunc(seconds)  #calculate how many seconds
        if score > score_limit:
            running = False
            pygame.mixer.Sound.play(complete_level)
            complete_level_screen()
    
        # set of matching candies
        matches = set()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
            # detect mouse click
            if clicked_gem is None and event.type == MOUSEBUTTONDOWN:
                
                # get the gem that was clicked on
                for row in board:
                    for gem in row:
                        if gem.rect.collidepoint(event.pos):
                            
                            clicked_gem = gem
                            
                            # save the coordinates of the point where the user clicked
                            click_x = event.pos[0]
                            click_y = event.pos[1]
                            
            # detect mouse motion
            if clicked_gem is not None and event.type == MOUSEMOTION:
                
                # calculate the distance between the point the user clicked on
                # and the current location of the mouse cursor
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])
                
                # reset the position of the swapped gem if direction of mouse motion changed
                if swapped_gem is not None:
                    swapped_gem.snap()
                    
                # determine the direction of the neighboring gem to swap with
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'
                    
                # if moving left/right, snap the clicked gem to its row position
                # otherwise, snap it to its col position
                if direction in ['left', 'right']:
                    clicked_gem.snap_row()
                else:
                    clicked_gem.snap_col()
                    
                # if moving the clicked gem to the left,
                # make sureit's not on the first col
                if direction == 'left' and clicked_gem.col_num > 0:
                    
                    # get the gem to the left
                    swapped_gem = board[clicked_gem.row_num][clicked_gem.col_num - 1]
                    
                    # move the two candies
                    clicked_gem.rect.left = clicked_gem.col_num * gem_width - distance_x
                    swapped_gem.rect.left = swapped_gem.col_num * gem_width + distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.left <= swapped_gem.col_num * gem_width + gem_width / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem to the right,
                # make sure it's not on the last col
                if direction == 'right' and clicked_gem.col_num < width / gem_width - 1:
                    
                    # get the gem to the right
                    swapped_gem = board[clicked_gem.row_num][clicked_gem.col_num + 1]
                    
                    # move the two candies
                    clicked_gem.rect.left = clicked_gem.col_num * gem_width + distance_x
                    swapped_gem.rect.left = swapped_gem.col_num * gem_width - distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.left >= swapped_gem.col_num * gem_width - gem_width / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem up,
                # make sure it's not on the first row
                if direction == 'up' and clicked_gem.row_num > 0:
                    
                    # get the gem above
                    swapped_gem = board[clicked_gem.row_num - 1][clicked_gem.col_num]
                    
                    # move the two candies
                    clicked_gem.rect.top = clicked_gem.row_num * gem_height - distance_y
                    swapped_gem.rect.top = swapped_gem.row_num * gem_height + distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.top <= swapped_gem.row_num * gem_height + gem_height / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem down,
                # make sure it's not on the last row
                if direction == 'down' and clicked_gem.row_num < height / gem_height - 1:
                    
                    # get the gem below
                    swapped_gem = board[clicked_gem.row_num + 1][clicked_gem.col_num]
                    
                    # move the two candies
                    clicked_gem.rect.top = clicked_gem.row_num * gem_height + distance_y
                    swapped_gem.rect.top = swapped_gem.row_num * gem_height - distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.top >= swapped_gem.row_num * gem_height - gem_height / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
            # detect mouse release
            if clicked_gem is not None and event.type == MOUSEBUTTONUP:
                
                # snap the candies back to their original positions on the grid
                clicked_gem.snap()
                clicked_gem = None
                if swapped_gem is not None:
                    swapped_gem.snap()
                    swapped_gem = None
                
        draw()
        pygame.display.update()
        
        # check if there's at least 3 matching candies
        if len(matches) >= 3:
            
            # add to score
            score += len(matches)
            
            # animate the matching candies shrinking
            while len(matches) > 0:
                
                clock.tick(100)
                
                # decrease width and height by 1
                for gem in matches:
                    new_width = gem.image.get_width() - 1
                    new_height = gem.image.get_height() - 1
                    new_size = (new_width, new_height)
                    gem.image = pygame.transform.smoothscale(gem.image, new_size)
                    gem.rect.left = gem.col_num * gem_width + (gem_width - new_width) / 2
                    gem.rect.top = gem.row_num * gem_height + (gem_height - new_height) / 2
                    
                # check if the candies have shrunk to zero size
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        gem = board[row_num][col_num]
                        if gem.image.get_width() <= 0 or gem.image.get_height() <= 0:
                            matches.remove(gem)
                            
                            # generate a new gem
                            board[row_num][col_num] = Gem(row_num, col_num)
                pygame.mixer.Sound.play(gem_match)                        
                draw()
       
                pygame.display.update()
def level_2():
    screen.fill((106, 90, 205))
    score = 0
    moves = 0
    score_limit = 50
    swapped_gem = None
    clicked_gem = None
    click_x = None
    click_y = None
    running = True
    def draw():
    
    # draw the background
        pygame.draw.rect(screen, (173, 216, 230), (0, 0, width, height + scoreboard_height))
        
        # draw the candies
        for row in board:
            for gem in row:
                gem.draw()
        
        # display the score and moves
        font = pygame.font.SysFont('monoface', 18)
        score_text = font.render(f'Score: {score} / {score_limit}', 1, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(width / 5, height + scoreboard_height / 2))
        screen.blit(score_text, score_text_rect)
        
        timer_text = font.render(f'Timer: {seconds_format}', 1, (0, 0, 0))
        timer_text_rect = timer_text.get_rect(center=(width * 2 / 5, height + scoreboard_height / 2))
        screen.blit(timer_text, timer_text_rect)

        moves_text = font.render(f'Moves: {moves} ', 1, (0, 0, 0))
        moves_text_rect = moves_text.get_rect(center=(width * 3 / 5, height + scoreboard_height / 2))
        screen.blit(moves_text, moves_text_rect)

        level_text = font.render(f'Level 2 ', 1, (0, 0, 0))
        level_text_rect = level_text.get_rect(center=(width * 4 / 5, height + scoreboard_height / 2))
        screen.blit(level_text, level_text_rect)

        
    while running:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        seconds_format = math.trunc(seconds)  #calculate how many seconds
        if score > score_limit:
            running = False
            pygame.mixer.Sound.play(complete_level)
            complete_level_screen()
        # set of matching candies
        matches = set()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
            # detect mouse click
            if clicked_gem is None and event.type == MOUSEBUTTONDOWN:
                
                # get the gem that was clicked on
                for row in board:
                    for gem in row:
                        if gem.rect.collidepoint(event.pos):
                            
                            clicked_gem = gem
                            
                            # save the coordinates of the point where the user clicked
                            click_x = event.pos[0]
                            click_y = event.pos[1]
                            
            # detect mouse motion
            if clicked_gem is not None and event.type == MOUSEMOTION:
                
                # calculate the distance between the point the user clicked on
                # and the current location of the mouse cursor
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])
                
                # reset the position of the swapped gem if direction of mouse motion changed
                if swapped_gem is not None:
                    swapped_gem.snap()
                    
                # determine the direction of the neighboring gem to swap with
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'
                    
                # if moving left/right, snap the clicked gem to its row position
                # otherwise, snap it to its col position
                if direction in ['left', 'right']:
                    clicked_gem.snap_row()
                else:
                    clicked_gem.snap_col()
                    
                # if moving the clicked gem to the left,
                # make sureit's not on the first col
                if direction == 'left' and clicked_gem.col_num > 0:
                    
                    # get the gem to the left
                    swapped_gem = board[clicked_gem.row_num][clicked_gem.col_num - 1]
                    
                    # move the two candies
                    clicked_gem.rect.left = clicked_gem.col_num * gem_width - distance_x
                    swapped_gem.rect.left = swapped_gem.col_num * gem_width + distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.left <= swapped_gem.col_num * gem_width + gem_width / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem to the right,
                # make sure it's not on the last col
                if direction == 'right' and clicked_gem.col_num < width / gem_width - 1:
                    
                    # get the gem to the right
                    swapped_gem = board[clicked_gem.row_num][clicked_gem.col_num + 1]
                    
                    # move the two candies
                    clicked_gem.rect.left = clicked_gem.col_num * gem_width + distance_x
                    swapped_gem.rect.left = swapped_gem.col_num * gem_width - distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.left >= swapped_gem.col_num * gem_width - gem_width / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem up,
                # make sure it's not on the first row
                if direction == 'up' and clicked_gem.row_num > 0:
                    
                    # get the gem above
                    swapped_gem = board[clicked_gem.row_num - 1][clicked_gem.col_num]
                    
                    # move the two candies
                    clicked_gem.rect.top = clicked_gem.row_num * gem_height - distance_y
                    swapped_gem.rect.top = swapped_gem.row_num * gem_height + distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.top <= swapped_gem.row_num * gem_height + gem_height / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem down,
                # make sure it's not on the last row
                if direction == 'down' and clicked_gem.row_num < height / gem_height - 1:
                    
                    # get the gem below
                    swapped_gem = board[clicked_gem.row_num + 1][clicked_gem.col_num]
                    
                    # move the two candies
                    clicked_gem.rect.top = clicked_gem.row_num * gem_height + distance_y
                    swapped_gem.rect.top = swapped_gem.row_num * gem_height - distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.top >= swapped_gem.row_num * gem_height - gem_height / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
            # detect mouse release
            if clicked_gem is not None and event.type == MOUSEBUTTONUP:
                
                # snap the candies back to their original positions on the grid
                clicked_gem.snap()
                clicked_gem = None
                if swapped_gem is not None:
                    swapped_gem.snap()
                    swapped_gem = None
                
        draw()
        pygame.display.update()
        
        # check if there's at least 3 matching candies
        if len(matches) >= 3:
            
            # add to score
            score += len(matches)
            
            # animate the matching candies shrinking
            while len(matches) > 0:
                
                clock.tick(100)
                
                # decrease width and height by 1
                for gem in matches:
                    new_width = gem.image.get_width() - 1
                    new_height = gem.image.get_height() - 1
                    new_size = (new_width, new_height)
                    gem.image = pygame.transform.smoothscale(gem.image, new_size)
                    gem.rect.left = gem.col_num * gem_width + (gem_width - new_width) / 2
                    gem.rect.top = gem.row_num * gem_height + (gem_height - new_height) / 2
                    
                # check if the candies have shrunk to zero size
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        gem = board[row_num][col_num]
                        if gem.image.get_width() <= 0 or gem.image.get_height() <= 0:
                            matches.remove(gem)
                            
                            # generate a new gem
                            board[row_num][col_num] = Gem(row_num, col_num)
                pygame.mixer.Sound.play(gem_match)                        
                draw()
       
                pygame.display.update()        

def level_3():
    screen.fill((106, 90, 205))
    score = 0
    moves = 0
    score_limit = 500
    swapped_gem = None
    clicked_gem = None
    click_x = None
    click_y = None
    running = True
   
    def draw():
    
    # draw the background
        pygame.draw.rect(screen, (173, 216, 230), (0, 0, width, height + scoreboard_height))
        
        # draw the candies
        for row in board:
            for gem in row:
                gem.draw()
        
        # display the score and moves
        font = pygame.font.SysFont('monoface', 18)
        score_text = font.render(f'Score: {score} / {score_limit}', 1, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(width / 5, height + scoreboard_height / 2))
        screen.blit(score_text, score_text_rect)
        
        timer_text = font.render(f'Timer: {seconds_format}', 1, (0, 0, 0))
        timer_text_rect = timer_text.get_rect(center=(width * 2 / 5, height + scoreboard_height / 2))
        screen.blit(timer_text, timer_text_rect)

        moves_text = font.render(f'Moves: {moves} ', 1, (0, 0, 0))
        moves_text_rect = moves_text.get_rect(center=(width * 3 / 5, height + scoreboard_height / 2))
        screen.blit(moves_text, moves_text_rect)

        level_text = font.render(f'Level 3 ', 1, (0, 0, 0))
        level_text_rect = level_text.get_rect(center=(width * 4 / 5, height + scoreboard_height / 2))
        screen.blit(level_text, level_text_rect)

        
    while running:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        seconds_format = math.trunc(seconds)  #calculate how many seconds
        if score > score_limit:
            running = False
            pygame.mixer.Sound.play(complete_level)
            complete_level_screen()
        # set of matching candies
        matches = set()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
            # detect mouse click
            if clicked_gem is None and event.type == MOUSEBUTTONDOWN:
                
                # get the gem that was clicked on
                for row in board:
                    for gem in row:
                        if gem.rect.collidepoint(event.pos):
                            
                            clicked_gem = gem
                            
                            # save the coordinates of the point where the user clicked
                            click_x = event.pos[0]
                            click_y = event.pos[1]
                            
            # detect mouse motion
            if clicked_gem is not None and event.type == MOUSEMOTION:
                
                # calculate the distance between the point the user clicked on
                # and the current location of the mouse cursor
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])
                
                # reset the position of the swapped gem if direction of mouse motion changed
                if swapped_gem is not None:
                    swapped_gem.snap()
                    
                # determine the direction of the neighboring gem to swap with
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'
                    
                # if moving left/right, snap the clicked gem to its row position
                # otherwise, snap it to its col position
                if direction in ['left', 'right']:
                    clicked_gem.snap_row()
                else:
                    clicked_gem.snap_col()
                    
                # if moving the clicked gem to the left,
                # make sureit's not on the first col
                if direction == 'left' and clicked_gem.col_num > 0:
                    
                    # get the gem to the left
                    swapped_gem = board[clicked_gem.row_num][clicked_gem.col_num - 1]
                    
                    # move the two candies
                    clicked_gem.rect.left = clicked_gem.col_num * gem_width - distance_x
                    swapped_gem.rect.left = swapped_gem.col_num * gem_width + distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.left <= swapped_gem.col_num * gem_width + gem_width / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem to the right,
                # make sure it's not on the last col
                if direction == 'right' and clicked_gem.col_num < width / gem_width - 1:
                    
                    # get the gem to the right
                    swapped_gem = board[clicked_gem.row_num][clicked_gem.col_num + 1]
                    
                    # move the two candies
                    clicked_gem.rect.left = clicked_gem.col_num * gem_width + distance_x
                    swapped_gem.rect.left = swapped_gem.col_num * gem_width - distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.left >= swapped_gem.col_num * gem_width - gem_width / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem up,
                # make sure it's not on the first row
                if direction == 'up' and clicked_gem.row_num > 0:
                    
                    # get the gem above
                    swapped_gem = board[clicked_gem.row_num - 1][clicked_gem.col_num]
                    
                    # move the two candies
                    clicked_gem.rect.top = clicked_gem.row_num * gem_height - distance_y
                    swapped_gem.rect.top = swapped_gem.row_num * gem_height + distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.top <= swapped_gem.row_num * gem_height + gem_height / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
                # if moving the clicked gem down,
                # make sure it's not on the last row
                if direction == 'down' and clicked_gem.row_num < height / gem_height - 1:
                    
                    # get the gem below
                    swapped_gem = board[clicked_gem.row_num + 1][clicked_gem.col_num]
                    
                    # move the two candies
                    clicked_gem.rect.top = clicked_gem.row_num * gem_height + distance_y
                    swapped_gem.rect.top = swapped_gem.row_num * gem_height - distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_gem.rect.top >= swapped_gem.row_num * gem_height - gem_height / 4:
                        swap(clicked_gem, swapped_gem)
                        matches.update(match_three(clicked_gem))
                        matches.update(match_three(swapped_gem))
                        moves += 1
                        clicked_gem = None
                        swapped_gem = None
                        
            # detect mouse release
            if clicked_gem is not None and event.type == MOUSEBUTTONUP:
                
                # snap the candies back to their original positions on the grid
                clicked_gem.snap()
                clicked_gem = None
                if swapped_gem is not None:
                    swapped_gem.snap()
                    swapped_gem = None
                
        draw()
        pygame.display.update()
        
        # check if there's at least 3 matching candies
        if len(matches) >= 3:
            
            # add to score
            score += len(matches)
            
            # animate the matching candies shrinking
            while len(matches) > 0:
                
                clock.tick(100)
                
                # decrease width and height by 1
                for gem in matches:
                    new_width = gem.image.get_width() - 1
                    new_height = gem.image.get_height() - 1
                    new_size = (new_width, new_height)
                    gem.image = pygame.transform.smoothscale(gem.image, new_size)
                    gem.rect.left = gem.col_num * gem_width + (gem_width - new_width) / 2
                    gem.rect.top = gem.row_num * gem_height + (gem_height - new_height) / 2
                    
                # check if the candies have shrunk to zero size
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        gem = board[row_num][col_num]
                        if gem.image.get_width() <= 0 or gem.image.get_height() <= 0:
                            matches.remove(gem)
                            
                            # generate a new gem
                            board[row_num][col_num] = Gem(row_num, col_num)
                pygame.mixer.Sound.play(gem_match)                        
                draw()
       
                pygame.display.update()       

def score():
    running = True
    while running:
        screen.fill((207, 140, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        draw_text('Score Table', font, (0,0,0), screen, 150, 40)
        for i in range(len(rows)):
            draw_text(rows[i], font, (255,255,255), screen, 155, 105 + 60 * i)
        
        pygame.display.update()
def win_screen(score_level):
    
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(100, 200, 200, 32)
    text = ''
    text_surface = font.render(text, True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    print("User input:", text)
                    insert(text,score_level)
                    text = ''
                    
                else:
                    text += event.unicode
                text_surface = font.render(text, True, (255, 255, 255))

        screen.fill((0, 128, 0))
        pygame.draw.rect(screen, (32, 178, 170), input_box, 2)
        screen.blit(text_surface, (input_box.x+5, input_box.y+5))
        draw_text('  Congratulations', font, (0,0,0), screen, 100, 40)
        draw_text(' This is new record', font, (0,0,0), screen, 100, 80)
        draw_text(' Enter your Name ', font, (0,0,0), screen, 90, 120)
        pygame.display.flip()

def complete_level_screen():
    font = pygame.font.Font(None, 32)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                

        screen.fill((0, 255, 153))
        
        draw_text('Level complete', font, (0,0,0), screen, 90, 200)
        
        pygame.display.flip()

def help():
    running = True
    while running:
        screen.fill((255, 242, 145))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        draw_text('Rules', font, (0,0,0), screen, 80, 40)
        draw_text('Classic match-tree rules', font, (0,0,0), screen, 80, 80)
        draw_text('Time: Play until time end', font, (0,0,0), screen, 80, 120)
        draw_text('Score *: 3 level with limit score', font, (0,0,0), screen, 80, 160)
        pygame.display.update()
 

        
        
    
    


main_menu()

