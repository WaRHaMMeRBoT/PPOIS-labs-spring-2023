import pygame
import game
import image_util

need_input = False
input_text = '_'
input_tick = 50


def get_input(x, y):
    global need_input, input_text, input_tick

    input_rect = pygame.Rect(x, y, 255, 50)

    mouse = pygame.mouse.get_pos()

    pygame.draw.rect(game.screen, (255, 255, 255), input_rect)

    click = pygame.mouse.get_pressed()

    if input_rect.collidepoint(mouse[0], mouse[1]) and click[0]:
        need_input = True

    if need_input:
        for event in pygame.event.get():
            if need_input and event.type == pygame.KEYDOWN:
                input_text = input_text.replace('_', '')
                input_tick = 50

                if event.key == pygame.K_RETURN:
                    need_input = False
                    message = input_text
                    input_text = ''
                    return message
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < 10:
                        input_text += event.unicode

                input_text += '_'
    if len(input_text):
        print_text(message=input_text, x=input_rect.x + 5, y=input_rect.y + 5, font_size=30, font_type='Qore.otf')
    input_tick -= 1

    if input_tick == 0:
        input_text = input_text[:-1]
    if input_tick == -50:
        input_text += '_'
        input_tick =50

    return None

def print_text(message, x, y, font_clr = (0,0,0), font_type = 'RequestPersonalUse.otf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_clr)
    game.screen.blit(text, (x,y))

def pause():
    paused = True
    pause_bg = pygame.image.load(image_util.getImage('land.png'))
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game.screen.blit(pause_bg, (0,0))
        print_text('Paused! press ENTER to continue', 110, 280, font_clr=(255, 255, 255), font_size=20)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        game.clock.tick(15)
