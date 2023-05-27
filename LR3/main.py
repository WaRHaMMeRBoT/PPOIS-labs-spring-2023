import pygame
import random
from pygame import *
import sys

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroids Adventure")
player_img = pygame.image.load('./images/seaplane.png')
asteroid_img = pygame.image.load('./images/Afgan_combat_fighter.png')
asteroid_img = pygame.transform.flip(asteroid_img, False, True)
bullet_img = pygame.image.load('./images/bullet.png')
PowerUp_img = pygame.image.load('./images/lighting.png')


pygame.mixer.music.load('./sounds/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()


clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.rect = self.image.get_rect(center=(400, 300))
        self.speed = 5
        self.lives = 3
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(asteroid_img, (50, 38))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(bullet_img, (30, 38))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 10

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, powerup_type):
        super().__init__()
        self.image = pygame.transform.scale(PowerUp_img, (40, 38))
        self.rect = self.image.get_rect(center=(x, y))
        self.type = powerup_type

    def update(self):
        self.rect.y += 1

player = Player()
player_group = pygame.sprite.GroupSingle(player)

asteroid_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    font = pygame.font.SysFont(None, 30)
    while True:

        screen.fill((21, 137, 117))
        draw_text('Bulgarian Preflight Briefing', font, (255, 255, 255), screen, 150, 40)

        mx, my = pygame.mouse.get_pos()

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

        # creating buttons
        button_1 = pygame.Rect(150, 100, 250, 50)
        button_2 = pygame.Rect(150, 200, 250, 50)
        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                the_game()
        elif button_2.collidepoint((mx, my)):
            if click:
                scoreboard()

        pygame.draw.rect(screen, (21, 137, 117), button_1)
        pygame.draw.rect(screen, (21, 137, 117), button_2)


        # writing text on top of button
        draw_text('-- Bulgarian Corncob', font, (255, 255, 255), screen, 150, 115)
        draw_text('-- Best Bulgarian Bombers', font, (255, 255, 255), screen, 150, 210)




        pygame.display.update()

def end_menu(score):
    font = pygame.font.SysFont(None, 30)
    while True:

        screen.fill((0, 0, 0))
        draw_text('You Were Hit By An Afghan Plane', font, (255, 0, 0), screen, 150, 40)

        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(150, 100, 390, 50)
        button_2 = pygame.Rect(150, 200, 250, 50)

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

        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                the_game()
        elif button_2.collidepoint((mx, my)):
            if click:
                scoreboard(score)

        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)

        # writing text on top of button
        draw_text('-- New Bulgarian Corncob Combat Flight', font, (255, 255, 255), screen, 150, 115)
        draw_text('-- Best Bulgarian Bombers', font, (255, 255, 255), screen, 150, 210)


        pygame.display.update()


def scoreboard_buttons(scores):
    font = pygame.font.SysFont(None, 30)
    while True:

        screen.fill((0, 0, 0))
        draw_text('Top-3 Bulgarian Combat Flights', font, (255, 0, 0), screen, 150, 40)

        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(150, 100, 250, 50)
        button_2 = pygame.Rect(150, 200, 250, 50)
        button_3 = pygame.Rect(150, 200, 250, 50)
        # defining functions when a certain button is pressed
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

        if button_1.collidepoint((mx, my)):
            if click:
                main_menu()
        elif button_2.collidepoint((mx, my)):
            if click:
                main_menu()
        elif button_3.collidepoint((mx, my)):
            if click:
                main_menu()

        pygame.draw.rect(screen, (0, 255, 0), button_1)
        pygame.draw.rect(screen, (0, 10, 255), button_2)
        pygame.draw.rect(screen, (0, 10, 255), button_3)

        # writing text on top of button
        draw_text(f"1.{str(scores[0])}", font, (255, 255, 255), screen, 150, 115)
        draw_text(f"2.{str(scores[1])}", font, (255, 255, 255), screen, 150, 210)
        draw_text(f"3.{str(scores[2])}", font, (255, 255, 255), screen, 150, 310)



        pygame.display.update()

def scoreboard(score):
    scores = []
    file = open("./Scores/LeaderBoard.rtf", "r")
    for line in file:
        if "\n" in line:
            line = line[:-1]
        scores.append(int(line))
    scores.append(int(score))
    file.close()
    scores.sort(reverse=True)
    print(scores)

    file_w = open("./Scores/LeaderBoard.rtf", "w+")
    for line in scores:
        print(line)
        file_w.write(str(line) + "\n")
    file_w.close()
    scoreboard_buttons(scores)


def the_game():
    running = True
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    bullet_group.add(bullet)

        if random.random() <.02:
            asteroid = Asteroid(random.randint(0, 800), 0)
            asteroid_group.add(asteroid)

        # проверка столкновений между снарядами и астероидами
        for bullet in pygame.sprite.groupcollide(bullet_group, asteroid_group, True, True).keys():
            player.score += 100
            powerup_type = random.choice(["speedup", "slowdown", "extra_life"])
            if powerup_type == "speedup":
                PowerUp_img = pygame.image.load('./images/lighting.png')
            elif powerup_type == "slowdown":
                PowerUp_img = pygame.image.load('./images/slow-down.png')
            else:
                PowerUp_img = pygame.image.load('./images/first-aid-kit.png')
            powerup = PowerUp(bullet.rect.x, bullet.rect.y, powerup_type)
            powerup_group.add(powerup)

        # проверка столкновений между игроком и астероидами
        if pygame.sprite.spritecollide(player, asteroid_group, True):
            player.lives -= 1
            player.speed -= 2
            if player.lives == 0:
                end_menu(player.score)

        # проверка столкновений между игроком и модификаторами
        for powerup in pygame.sprite.spritecollide(player, powerup_group, True):
            if powerup.type == "speedup":
                player.speed += 1
            elif powerup.type == "slowdown":
                player.speed -= 1
            elif powerup.type == "extra_life":
                player.lives += 1

        player_group.update()
        asteroid_group.update()
        bullet_group.update()
        powerup_group.update()

        player_group.draw(screen)
        asteroid_group.draw(screen)
        bullet_group.draw(screen)
        powerup_group.draw(screen)

        font = pygame.font.Font(None, 36)
        lives_text = font.render(f"Lives: {player.lives}", 1, (255, 255, 255))
        screen.blit(lives_text, (10, 10))

        pygame.display.flip()


if __name__ == "__main__":
    main_menu()

pygame.quit()
