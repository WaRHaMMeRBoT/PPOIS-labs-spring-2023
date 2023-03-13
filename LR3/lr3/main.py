import pygame

from lr3.board import Board
from lr3.constants import player_img, WIDTH, SCALE, HEIGHT, FPS, BLACK
from lr3.walls import Wall


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.last_update = 0
        self.speedy = 0
        self.speedx = 0
        self.image = pygame.transform.scale(player_img[0], (SCALE, SCALE))
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH / 2), HEIGHT / 2)
        self.iter = 0
        self.pos = 0

    def update(self):

        now = pygame.time.get_ticks()
        if now - self.last_update > 60:
            self.last_update = now
            self.image = pygame.transform.rotate(player_img[self.iter], self.pos)
            self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        # вращение спрайтов
        if self.iter >= 2:
            self.iter = 0
        else:
            self.iter += 1
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.speedy = 0
            self.pos = 180
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.speedy = 0
            self.pos = 0
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
            self.speedx = 0
            self.pos = 270
        if keystate[pygame.K_UP]:
            self.speedy = -8
            self.speedx = 0
            self.pos = 90

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.bottom < self.rect.height:
            self.rect.bottom = self.rect.height
        self.rect.x += self.speedx
        self.rect.y += self.speedy


# Создаем игру и окно
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

personalities = pygame.sprite.Group()


player = Player()

personalities.add(player)


pacman = pygame.sprite.Group()

board = Board()
pacman.add(board.getBoard(), personalities)


# Цикл игры


def run():
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        collide_right = pygame.sprite.spritecollide(player, board.right_walls_group, dokill=False)
        collide_left = pygame.sprite.spritecollide(player, board.left_walls_group, dokill=False)
        collide_down = pygame.sprite.spritecollide(player, board.down_walls_group, dokill=False)
        collide_up = pygame.sprite.spritecollide(player, board.up_walls_group, dokill=False)
        # If the objects are colliding
        # then changing the y coordinate
        if collide_right:
            print("right")
            player.speedx = 0
            player.speedy = 0
            player.rect.right = collide_right[0].rect.left
        elif collide_left:
            print("left")
            player.speedx = 0
            player.speedy = 0
            player.rect.left = collide_left[0].rect.right
        elif collide_down:
            print("down")
            player.speedx = 0
            player.speedy = 0
            player.rect.top = collide_down[0].rect.bottom
        elif collide_up:
            print("top")
            player.speedx = 0
            player.speedy = 0
            player.rect.bottom = collide_up[0].rect.top
        # If the objects are colliding
        # then changing the y coordinate

        # Обновление
        personalities.update()
        pacman.update()
        # Рендеринг
        screen.fill(BLACK)
        personalities.draw(screen)
        pacman.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    run()
