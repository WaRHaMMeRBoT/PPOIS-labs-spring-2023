import pygame
from pygame.locals import *
import random

pygame.init()

width = 1200
height = 720
board_height = 400
board_width = 400
scoreboard_height = 25
window_size = (width, height + scoreboard_height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Jewel Quest')
boardimg = pygame.image.load(r'board.png')
frame = pygame.image.load(r'frame.png')
tframe = pygame.image.load(r'timer_frame.png')
mframe = pygame.image.load(r'message_frame.png')
icon = pygame.image.load(r'Stone_red.png')
menubcg = pygame.image.load(r'menubcg.webp')
boardimg = pygame.transform.scale(boardimg, (board_width, board_height))
frame = pygame.transform.scale(frame, (495, 495))
mframe = pygame.transform.scale(mframe, (500, 200))
tframe = pygame.transform.scale(tframe, (150, 100))
icon = pygame.transform.scale(icon, (50, 50))
pygame.display.set_icon(icon)
mouse_pos = pygame.mouse.get_pos() 


font = pygame.font.Font(r'C:\Users\vladi\Desktop\4\PPois\JewelQuest\font\font.ttf', 100)

start_text = font.render('Start Game', True, 'Black')
quit_text = font.render('Exit', True, 'Black')
time_mode = font.render('Time Mode', True, 'Black')
score_mode = font.render('Score Mode', True, 'Black')
back_button = font.render('Back', True, 'Black')
start_rect = start_text.get_rect(topleft = (350, 200))
quit_rect = quit_text.get_rect(topleft = (500, 300))


stone_colors = ['blue', 'green', 'orange', 'pink', 'purple', 'red', 'teal', 'yellow']

stone_width = 40
stone_height = 40
stone_size = (stone_width, stone_height)
score = 0
moves = 0

class Stone:
    
    def __init__(self, row_num, col_num):
        
        self.row_num = row_num
        self.col_num = col_num
        
        self.color = random.choice(stone_colors)
        image_name = f'stone_{self.color}.png'
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.scale(self.image, stone_size)
        self.rect = self.image.get_rect()
        self.rect.left = (col_num * stone_width) + 400
        self.rect.top = (row_num * stone_height) + 160
        
    def draw(self):
        screen.blit(self.image, self.rect)
        
    def snap(self):
        self.snap_row()
        self.snap_col()
        
    def snap_row(self):
        self.rect.top = (self.row_num * stone_height) + 160
        
    def snap_col(self):
        self.rect.left = (self.col_num * stone_width) + 400
        
board = []

for row_num in range(board_height // stone_height):
    
    board.append([])
    
    for col_num in range(board_width // stone_width):
        
        stone = Stone(row_num, col_num)
        board[row_num].append(stone)
        
def draw(moves, score):
    
    pygame.draw.rect(screen, (255, 255, 255), (0, 720, 1200, 25))
    screen.blit(boardimg, (399, 160))
    screen.blit(frame, (350, 110))



    for row in board:
        for stone in row:
            stone.draw()
    
    font = pygame.font.SysFont('monoface', 18)
    score_text = font.render(f'Score: {score}', 1, (0, 0, 0))
    score_text_rect = score_text.get_rect(center=(width / 4, height + scoreboard_height / 2))
    screen.blit(score_text, score_text_rect)
    
    moves_text = font.render(f'Moves: {moves}', 1, (0, 0, 0))
    moves_text_rect = moves_text.get_rect(center=(width * 3 / 4, height + scoreboard_height / 2))
    screen.blit(moves_text, moves_text_rect)
    
def swap(stone1, stone2):
    
    temp_row = stone1.row_num
    temp_col = stone1.col_num
    
    stone1.row_num = stone2.row_num
    stone1.col_num = stone2.col_num
    
    stone2.row_num = temp_row
    stone2.col_num = temp_col
    
    board[stone1.row_num][stone1.col_num] = stone1
    board[stone2.row_num][stone2.col_num] = stone2
    
    stone1.snap()
    stone2.snap()
    
def find_matches(stone, matches):
      
    matches.add(stone)
    
    if stone.row_num > 0:
        neighbor = board[stone.row_num - 1][stone.col_num]
        if stone.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    if stone.row_num < board_height / stone_height - 1:
        neighbor = board[stone.row_num + 1][stone.col_num]
        if stone.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    if stone.col_num > 0:
        neighbor = board[stone.row_num][stone.col_num - 1]
        if stone.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    if stone.col_num < board_width / stone_width - 1:
        neighbor = board[stone.row_num][stone.col_num + 1]
        if stone.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    return matches
    
def match_three(stone):
    
    matches = find_matches(stone, set())
    if len(matches) >= 3:
        return matches
    else:
        return set()
        


def main_menu():
    engine = True
    while engine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                engine = False

        mouse_pos = pygame.mouse.get_pos() 
        screen.blit(menubcg, (0,0))

        if start_rect.collidepoint(mouse_pos):
            screen.blit(icon, (275,220))
            screen.blit(icon, (850,220))
        if quit_rect.collidepoint(mouse_pos):
            screen.blit(icon, (420,315)) 
            screen.blit(icon, (690,315))

        screen.blit(start_text, (350,200))
        screen.blit(quit_text, (500,300))

        pygame.display.update()

        if start_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            screen.blit(menubcg, (0, 0))
            mode_menu()
            

        if quit_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            engine = False  
            pygame.quit()  
        
def mode_menu():
    score_rect = score_mode.get_rect(topleft = (350, 400))
    time_rect = time_mode.get_rect(topleft = (370, 300))
    back_rect = back_button.get_rect(topleft = (0, 0))

    engine = True
    while engine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                engine = False

        mouse_pos = pygame.mouse.get_pos() 
        screen.blit(menubcg, (0,0))

        if score_rect.collidepoint(mouse_pos):
            screen.blit(icon, (275,420))
            screen.blit(icon, (850,420))

        if time_rect.collidepoint(mouse_pos):
            screen.blit(icon, (320,315)) 
            screen.blit(icon, (815,315))

        if back_rect.collidepoint(mouse_pos):
            screen.blit(icon, (225, 20))
        screen.blit(back_button, (10, 0))
        screen.blit(score_mode, (350, 400))
        screen.blit(time_mode, (390, 300))


        pygame.display.update()

        if score_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            screen.blit(menubcg, (0, 0))
            mode = 1
            game(moves, score, mode)

        if time_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            screen.blit(menubcg, (0, 0))
            mode = 2
            game(moves, score, mode)

        if back_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            main_menu()



def game(moves, score, mode):

    clicked_stone = None
    swapped_stone = None
    click_x = None
    click_y = None
    clock = pygame.time.Clock()
    time = pygame.time.get_ticks()
    engine = True

    while engine:
        matches = set()
        
        if mode == 1:
            if score >= 100:
                ok = False
                while not ok:
                    for event in pygame.event.get():
                        screen.blit(menubcg, (0,0))
                        screen.blit(mframe, (345, 270))
                        you_won = font.render('You Won', True, 'Black')
                        screen.blit(you_won, (440, 320))
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN: 
                                ok = True
                                main_menu()
                    pygame.display.update()

        if mode == 2:
            time_left = 99000
            time_passed = pygame.time.get_ticks() - time
            time_left -= time_passed
            screen.blit(tframe, (517, 20))
            text = font.render("{}".format(time_left//1000), True, 'Black')
            screen.blit(text, (545, 25))
            if time_left <= 0:
                ok = False
                while not ok:
                    for event in pygame.event.get():
                        screen.blit(menubcg, (0, 0))
                        screen.blit(mframe, (345, 270))
                        you_won = font.render('Game Over', True, 'Black')
                        screen.blit(you_won, (388, 320))
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN: 
                                ok = True
                                main_menu()
                        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine = False
                pygame.quit()


            if clicked_stone is None and event.type == pygame.MOUSEBUTTONDOWN:
                
                for row in board:
                    for stone in row:
                        if stone.rect.collidepoint(event.pos):
                            
                            clicked_stone = stone
                            
                            click_x = event.pos[0]
                            click_y = event.pos[1]
                            
            if clicked_stone is not None and event.type == pygame.MOUSEMOTION:
                
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])
                
                if swapped_stone is not None:
                    swapped_stone.snap()
                    
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'
                    
                if direction in ['left', 'right']:
                    clicked_stone.snap_row()
                else:
                    clicked_stone.snap_col()
                    
                if direction == 'left' and clicked_stone.col_num > 0:
                    
                    swapped_stone = board[clicked_stone.row_num][clicked_stone.col_num - 1]
                    
                    clicked_stone.rect.left = (clicked_stone.col_num * stone_width - distance_x) + 400
                    swapped_stone.rect.left = (swapped_stone.col_num * stone_width + distance_x) + 400
                    
                    if clicked_stone.rect.left <= (swapped_stone.col_num * stone_width + stone_width / 4) + 400:
                        swap(clicked_stone, swapped_stone)
                        matches.update(match_three(clicked_stone))
                        matches.update(match_three(swapped_stone))
                        moves += 1
                        clicked_stone = None
                        swapped_stone = None
                        
                if direction == 'right' and clicked_stone.col_num < board_width / stone_width - 1:
                    
                    swapped_stone = board[clicked_stone.row_num][clicked_stone.col_num + 1]
                    clicked_stone.rect.left = (clicked_stone.col_num * stone_width + distance_x) + 400
                    swapped_stone.rect.left = (swapped_stone.col_num * stone_width - distance_x) + 400
                    
                    if clicked_stone.rect.left >= (swapped_stone.col_num * stone_width - stone_width / 4) + 400:
                        swap(clicked_stone, swapped_stone)
                        matches.update(match_three(clicked_stone))
                        matches.update(match_three(swapped_stone))
                        moves += 1
                        clicked_stone = None
                        swapped_stone = None
                        
                if direction == 'up' and clicked_stone.row_num > 0:
                    
                    swapped_stone = board[clicked_stone.row_num - 1][clicked_stone.col_num]
                    
                    clicked_stone.rect.top = (clicked_stone.row_num * stone_height - distance_y) + 160
                    swapped_stone.rect.top = (swapped_stone.row_num * stone_height + distance_y) + 160
                    
                    if clicked_stone.rect.top <= (swapped_stone.row_num * stone_height + stone_height / 4) + 160:
                        swap(clicked_stone, swapped_stone)
                        matches.update(match_three(clicked_stone))
                        matches.update(match_three(swapped_stone))
                        moves += 1
                        clicked_stone = None
                        swapped_stone = None
                        
                if direction == 'down' and clicked_stone.row_num < board_height / stone_height - 1:
                    
                    swapped_stone = board[clicked_stone.row_num + 1][clicked_stone.col_num]
                    clicked_stone.rect.top = (clicked_stone.row_num * stone_height + distance_y) + 160
                    swapped_stone.rect.top = (swapped_stone.row_num * stone_height - distance_y) + 160
                    
                    if clicked_stone.rect.top >= (swapped_stone.row_num * stone_height - stone_height / 4) + 160:
                        swap(clicked_stone, swapped_stone)
                        matches.update(match_three(clicked_stone))
                        matches.update(match_three(swapped_stone))
                        moves += 1
                        clicked_stone = None
                        swapped_stone = None
                        
            if clicked_stone is not None and event.type == pygame.MOUSEBUTTONUP:
                
                clicked_stone.snap()
                clicked_stone = None
                if swapped_stone is not None:
                    swapped_stone.snap()
                    swapped_stone = None


        draw(moves, score)
        pygame.display.update()
        
        if len(matches) >= 3:
            
            score += len(matches)
            
            while len(matches) > 0:
                
                for stone in matches:
                    new_width = stone.image.get_width() - 1
                    new_height = stone.image.get_height() - 1
                    new_size = (new_width, new_height)
                    stone.image = pygame.transform.smoothscale(stone.image, new_size)
                    stone.rect.left = (stone.col_num * stone_width + (stone_width - new_width) / 2) + 400
                    stone.rect.top = (stone.row_num * stone_height + (stone_height - new_height) / 2) + 160
                    
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        stone = board[row_num][col_num]
                        if stone.image.get_width() <= 0 or stone.image.get_height() <= 0:
                            matches.remove(stone)
                            board[row_num][col_num] = Stone(row_num, col_num)
                draw(moves, score)
                pygame.display.update()
        clock.tick(100)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    main_menu()

pygame.quit()