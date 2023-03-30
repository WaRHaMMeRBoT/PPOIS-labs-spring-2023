import pygame
from pygame.math import Vector2
from pygame import mixer


def load_balloon(condition, color_name):
    res = []
    for count in range(1, 5):
        im = pygame.image.load(f"res/balloon/{condition}_{color_name}_{count}.png")
        res.append(im.convert_alpha())
    return res


pygame.init()
clock = pygame.time.Clock()
FPS_value = 60

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Balloon Shooting Game')

channel3 = mixer.Channel(2)
hit_sound = mixer.Sound('res/audio/Hit.ogg')
RedBalloon_idle_list = load_balloon("idle", "red")
RedBalloon_quit_list = load_balloon("explode", "red")
BlueBalloon_idle_list = load_balloon("idle", "blue")
BlueBalloon_quit_list = load_balloon("explode", "blue")
GreenBalloon_idle_list = load_balloon("idle", "lightgreen")
GreenBalloon_quit_list = load_balloon("explode", "lightgreen")
Balloon_idle_Set = [RedBalloon_idle_list, BlueBalloon_idle_list, GreenBalloon_idle_list]
Balloon_quit_Set = [RedBalloon_quit_list, BlueBalloon_quit_list, GreenBalloon_quit_list]


class Balloon(pygame.sprite.Sprite):
    def __init__(self, random_number, position, velocity, scale, delta_time):
        super().__init__()
        img_idle_list = Balloon_idle_Set[random_number]
        img_quit_list = Balloon_quit_Set[random_number]
        img_width, img_height = img_idle_list[0].get_rect().size
        img_width = int(img_width * scale)
        img_height = int(img_height * scale)
        self.ColorIndex = random_number
        self.ImgIdle_list_scaled = []
        self.ImgQuit_list_scaled = []

        for list_num in range(len(img_idle_list)):
            tmp_image = img_idle_list[list_num]
            tmp_image = pygame.transform.smoothscale(tmp_image, (img_width, img_height))
            self.ImgIdle_list_scaled.append(tmp_image)
        for list_num in range(len(img_quit_list)):
            tmp_image = img_quit_list[list_num]
            tmp_image = pygame.transform.smoothscale(tmp_image, (img_width, img_height))
            self.ImgQuit_list_scaled.append(tmp_image)

        self.image = self.ImgIdle_list_scaled[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.d_t = delta_time
        self.mask = pygame.mask.from_surface(self.image)
        self.quit_trigger = False
        self.time_counter = 0
        self.frame = 0
        self.ani_frametime = self.d_t * 60 * 0.05

    def update(self, env_movement):
        if self.quit_trigger:
            self.quit_animation()
        else:
            self.idle_animation()
            self.position += self.velocity * self.d_t

        self.position += env_movement
        self.rect.center = self.position

        if self.rect.bottom <= 0:
            self.kill()

    def set_quit_trigger(self):
        self.quit_trigger = True
        self.time_counter = 0
        self.frame = 0
        channel3.play(hit_sound)

    def require_parameters(self):
        return self.position, self.rect.height, self.ColorIndex

    def idle_animation(self):
        self.time_counter += self.d_t
        if self.time_counter >= self.ani_frametime * 4:
            self.frame += 1
            self.time_counter = 0
        if self.frame > len(self.ImgIdle_list_scaled) - 1:
            self.frame = 0
        self.image = self.ImgIdle_list_scaled[self.frame]

    def quit_animation(self):
        self.time_counter += self.d_t
        if self.frame <= len(self.ImgQuit_list_scaled) - 1:
            self.image = self.ImgQuit_list_scaled[self.frame]
            if self.time_counter >= self.ani_frametime:
                self.frame += 1
                self.time_counter = 0
            quit_velocity = Vector2(self.velocity.x, 0.05)
            self.position += quit_velocity * self.d_t
        elif self.frame > len(self.ImgQuit_list_scaled) - 1:
            self.kill()
            self.time_counter = 0
            self.frame = 0
            self.quit_trigger = False

    def is_quit_trigger(self):
        return self.quit_trigger
