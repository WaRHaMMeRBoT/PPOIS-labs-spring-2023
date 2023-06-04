import pygame, sys, random, csv, os, pydot


def reloading():
    if cursor.is_reloading:
        if current_time - pressed_time > 2000:
            cursor.is_reloading = False
            reload_sound.play()
            cursor.reload()


def display_time():
    time_surface = game_font.render(str(time_to_finish), True, (255, 255, 255))
    time_rect = time_surface.get_rect(center=(100, 30))
    screen.blit(time_surface, time_rect)


def end_of_game():
    if time_to_finish <= 0:
        score_manager.read_highscores_file()
        score_manager.get_highscores_graphic(game_font)
        return "highscore"
    else:
        return "main"


def display_intro_text():
    intro_surface = intro_font.render("Are You Ready?...", True, (255, 255, 255))
    intro_rect = intro_surface.get_rect(center=(SCREEN_W / 2, SCREEN_H / 2))
    screen.blit(intro_surface, intro_rect)


def decrease_light():
    surf = pygame.Surface((SCREEN_W, SCREEN_H))
    surf.fill((0, 0, 0))
    surf.set_alpha((100))
    screen.blit(surf, (0, 0))


def add_chick_to_group(chicken):
    if chicken.size <= 39:
        chicken_group_20_39.add(chicken)
    elif chicken.size <= 59:
        chicken_group_40_59.add(chicken)
    elif chicken.size <= 79:
        chicken_group_60_79.add(chicken)
    elif chicken.size <= 99:
        chicken_group_80_99.add(chicken)
    elif chicken.size <= 125:
        chicken_group_100_125.add(chicken)


def draw_all_chickens():
    for chicken_group in all_chickens_group:
        chicken_group.draw(screen)


def update_all_chickens():
    for chicken_group in all_chickens_group:
        chicken_group.update()


def create_all_chickens_group():
    all_chickens_group.append(chicken_group_20_39)
    all_chickens_group.append(chicken_group_40_59)
    all_chickens_group.append(chicken_group_60_79)
    all_chickens_group.append(chicken_group_80_99)
    all_chickens_group.append(chicken_group_100_125)


pygame.init()
pygame.font.init()
pygame.mouse.set_visible(False)
SCREEN_W = 1000
SCREEN_H = 700
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('Comic Sans MS', 40)
intro_font = pygame.font.SysFont('Arial', 60)


class Background():
    def __init__(self, screen):
        self.screen = screen
        self.ground = pygame.image.load("images/background/ground.png").convert_alpha()
        self.ground = pygame.transform.scale(self.ground, (1000, 700))
        self.sky = pygame.image.load("images/background/sky.png").convert_alpha()
        self.sky = pygame.transform.scale(self.sky, (1000, 700))
        self.foreground = pygame.image.load("images/background/foreground.png").convert_alpha()
        self.foreground = pygame.transform.scale(self.foreground, (1000, 700))

    def draw_ground(self):
        self.screen.blit(self.ground, (0, 0))

    def draw_sky(self):
        self.screen.blit(self.sky, (0, 0))

    def draw_foreground(self):
        self.screen.blit(self.foreground, (0, 0))


class Cursor(pygame.sprite.Sprite):
    def __init__(self, score_manager):
        super().__init__()
        self.image = pygame.image.load("images/crosshair.png").convert_alpha()
        self.ammo_image_orig = pygame.image.load("images/ammo.png").convert_alpha()
        self.ammo_image = pygame.transform.rotozoom(self.ammo_image_orig, -15, 1.7)
        self.ammo_out_image = pygame.transform.rotozoom(self.ammo_image_orig, -15, 1.7)
        self.ammo_out_image.set_alpha(100)

        self.ammo_rect = self.ammo_image.get_rect(center=(580, 620))

        self.score_manager = score_manager
        self.rect = self.image.get_rect()

        self.ammo = 6
        self.is_reloading = False

        self.hit = False

    def draw_ammo(self, screen):
        # draw blank patrols
        self.ammo_rect.x = 580
        for i in range(6):
            self.ammo_rect.x += 50
            screen.blit(self.ammo_out_image, self.ammo_rect)
        # draw full patrols
        self.ammo_rect.x = 580
        for i in range(self.ammo):
            self.ammo_rect.x += 50
            screen.blit(self.ammo_image, self.ammo_rect)

    def shoot(self, all_chickens, shot_sound, chicken_hit_sound):
        x = 0
        y = 0
        size = 0
        if not self.is_reloading:
            if self.ammo > 0:
                shot_sound.play()
                self.ammo -= 1
                # if the chicken is hit increase the score and delete the chicken
                for chickens in all_chickens:
                    for chicken in chickens:
                        if self.rect.colliderect(chicken.rect) and chicken.alive:
                            score_manager.update_score(chicken)
                            chicken_hit_sound.play()
                            chicken.alive = False
                            chicken.blood = False
                            chicken.set_dead_image()
                            self.hit = True
                            x = self.rect.centerx
                            y = self.rect.centery
                            size = chicken.size
                        else:
                            pass  # SOUND WHEN MISS SHOT
            else:
                pass  # SOUND WHEN RELOADING AND TRYING TO SHOT
        return self.hit, x, y, size

    def reload(self):
        self.ammo = 6

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Chicken(pygame.sprite.Sprite):
    def __init__(self, pos_y):
        super().__init__()
        # Images
        self.chicken_right_surf = [
            pygame.image.load(f"images/chicken_fly_right/chicken_fly_right{x}.png").convert_alpha() for x in range(7)]
        self.chicken_left_surf = [pygame.image.load(f"images/chicken_fly_left/chicken_fly_left{x}.png").convert_alpha()
                                  for x in range(7)]
        self.chicken_dead_surf = [pygame.image.load(f"images/chicken_dead/chicken_dead{x}.png").convert_alpha() for x in
                                  range(2)]

        # Atributes
        self.blood = True
        self.alive = True
        self.direction = self.set_direction()
        self.size = self.set_size()
        self.speed = self.set_speed()
        self.vertical_intensity = self.set_vertical_intensity()
        self.movement = self.speed * self.direction
        self.pos_x = self.set_x_position(self.movement)
        self.pos_y = pos_y
        self.falling_movement = self.set_falling_movement()
        self.fly_up_or_down = random.choice([0, 1, 2])

        self.image_index = 0
        self.images = self.set_images_sequence()
        self.image = pygame.transform.scale(self.images[self.image_index], (self.size, self.size))
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

    def set_falling_movement(self):
        if self.direction == -1:
            return self.movement
        else:
            return self.movement * (-1)

    def set_dead_image(self):
        if self.direction == 1:
            self.image = pygame.transform.scale(self.chicken_dead_surf[0], (self.size, self.size))
        else:
            self.image = pygame.transform.scale(self.chicken_dead_surf[1], (self.size, self.size))

        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

    def index_update(self):
        self.image_index += 0.3
        if self.image_index > 6:
            self.image_index = 0

    def animation(self):
        new_image = self.images[int(self.image_index)]
        new_image = pygame.transform.scale(new_image, (self.size, self.size))
        new_rect = new_image.get_rect(center=(self.rect.centerx, self.rect.centery))
        return new_image, new_rect

    # Fly Up, straight or Down with 33% on spawn
    def fly(self):
        # Fly Up
        if self.fly_up_or_down == 1:
            if random.randint(-7, 2) > 0:
                self.rect.move_ip(self.movement, -1)
            else:
                self.rect.move_ip(self.movement, 0)
        # Fly Straight
        elif self.fly_up_or_down == 0:
            self.rect.move_ip(self.movement, 0)
        # Fly Down
        else:
            if random.randint(-7, 2) > 0:
                self.rect.move_ip(self.movement, 1)
            else:
                self.rect.move_ip(self.movement, 0)

    def update(self):
        # Flying animation
        if self.alive:
            self.index_update()
            self.image, self.rect = self.animation()

        self.pos_x = self.rect.centerx
        self.pos_y = self.rect.centery

        # Flying Speed and Movement
        self.fly()

        # Dead Falling Speed
        if not self.alive:
            self.falling_movement += 0.2
            self.rect.move_ip(0, self.falling_movement)
            if self.direction == 1 and self.movement >= 0:
                self.movement -= 0.05
            elif self.direction == -1 and self.movement <= 0:
                self.movement += 0.05

        # Deleting if out of the screen
        self.delete_chicken()

    def set_images_sequence(self):
        if self.direction == 1:
            return self.chicken_right_surf
        else:
            return self.chicken_left_surf

    def set_x_position(self, move):
        if move > 0:
            return 0
        else:
            return 1000  # SCREEN_WIDTH

    def set_size(self):
        return random.randint(20, 125)

    # -1 = left, 1 = right
    def set_direction(self):
        return random.choice([-1, 1])

    def set_speed(self):
        return random.uniform(1, 5)

    def set_vertical_intensity(self):
        return random.randint(1, 2)

    def delete_chicken(self):
        # Stands for the chickens with size 60+
        if self.size >= 60:
            if self.rect.centery > 750 or self.rect.centery < -50:
                self.kill()
            if self.movement > 0:
                if self.rect.left > 1000:
                    self.kill()
            else:
                if self.rect.right < 0:
                    self.kill()
        # Stands for the chickens with size lower than 60
        else:
            if self.rect.centery > 550 or self.rect.centery < 100:
                self.kill()
            if self.movement > 0:
                if self.rect.left > 1000:
                    self.kill()
            else:
                if self.rect.right < 0:
                    self.kill()


class ScoreManager():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.highscores_raw = []
        self.highscores_surfs = []
        self.highscores_rects = []
        self.new_hs = False

    # Score during the game in the right corner
    def display_score(self, screen, game_font):
        score_surface = game_font.render(str(self.score), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(950, 30))
        screen.blit(score_surface, score_rect)

    # Increase the overall score depends on the size of the hit chicken
    def update_score(self, chicken):
        score = 0
        if chicken.size == 20:
            score = int(15 * chicken.speed)
        elif chicken.size <= 30:
            score = int(10 * chicken.speed)
        elif chicken.size <= 40:
            score = int(8 * chicken.speed)
        elif chicken.size <= 60:
            score = int(5 * chicken.speed)
        elif chicken.size <= 80:
            score = int(3 * chicken.speed)
        elif chicken.size <= 100:
            score = int(2 * chicken.speed)
        elif chicken.size <= 125:
            score = int(1 * chicken.speed)
        self.score += score

    def set_new_highscore(self):
        new_highscores = []
        overwritten = False

        for i in range(5, 0, -1):
            name, score = self.highscores_raw[i]
            if self.score > int(score) and (not overwritten):
                new_highscores.append([self.name, str(self.score)])
                self.new_hs = True
                overwritten = True
            else:
                new_highscores.append(self.highscores_raw[i])

        # Sorting table descent order by score
        header = [["Player", "HighScore"]]
        int_highscores = [[row[0], int(row[1])] for row in new_highscores]

        int_highscores.sort(key=lambda x: x[1], reverse=True)

        str_highscores = [[row[0], str(row[1])] for row in int_highscores]

        final = header + str_highscores

        self.save_new_highscores(final)

        return final

    # Read from file when object instantiate and order it. if the file doesnt exists - create it from template
    def read_highscores_file(self):
        highscores = []
        if os.path.exists("highscores.csv"):
            with open("highscores.csv", "r") as file:
                reader = csv.reader(file, delimiter="\t")
                for row in reader:
                    highscores.append(row)
        else:
            self.create_csv_file()
            with open("highscores.csv", "r") as file:
                reader = csv.reader(file, delimiter="\t")
                for row in reader:
                    highscores.append(row)

        self.highscores_raw = highscores

    def save_new_highscores(self, data):
        with open("highscores.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerows(data)

    def create_csv_file(self):
        template = [["Player", "HighScore"]]
        for i in range(5):
            template.append(["Empty", "0"])

        with open("highscores.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerows(template)

    # Get values of highscore surfaces and rectangles for drawing
    def get_highscores_graphic(self, font):
        highscores_overwritten = self.set_new_highscore()
        pos_y = 0
        for row in highscores_overwritten:
            name, score = row
            pos_y += 100
            if name == "Player":
                highscore_surface = font.render(f"{name}          {score}", True, (255, 0, 0))
            else:
                highscore_surface = font.render(f"{name}              {score}", True, (255, 255, 255))
            self.highscores_surfs.append(highscore_surface)
            self.highscores_rects.append(highscore_surface.get_rect(center=(500, pos_y)))

    # Table on the end of the game
    def draw_highscore_table(self, screen):
        if self.new_hs:
            scr, rect = self.set_hs_announce()
            screen.blit(scr, rect)
        for i in range(6):
            screen.blit(self.highscores_surfs[i], self.highscores_rects[i])

    def set_hs_announce(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        announce_surface = font.render(f"You earned your place in the Highscore table!", True, (255, 0, 0))
        announce_rect = announce_surface.get_rect(center=(500, 40))
        return announce_surface, announce_rect


class Particle():
    def __init__(self, x, y):
        self.x_vel = random.randrange(-3, 3)
        self.y_vel = random.randrange(-3, 3)
        self.lifetime = 20
        self.x = x
        self.y = y

    def draw(self, screen):
        self.lifetime -= 1
        if self.lifetime > 0:
            self.x += self.x_vel
            self.y += self.y_vel
            pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.lifetime // 2)


# Game Variables
game_state = "set_name"
user_name = ""
time_to_finish = 60
current_time = 0
pressed_time = 0
size = 0
input_active = True

# Sounds
shot_sound = pygame.mixer.Sound("sounds/shot.wav")
reload_sound = pygame.mixer.Sound("sounds/reload.aiff")
chicken_hit_sound = pygame.mixer.Sound("sounds/chicken_hit.wav")
chicken_peep_sound = pygame.mixer.Sound("sounds/chicken_sound.wav")

# Particles
blood_particles = []

# BackGround
background = Background(screen)

# Chicken groups by size
all_chickens_group = []
chicken_group_20_39 = pygame.sprite.Group()
chicken_group_40_59 = pygame.sprite.Group()
chicken_group_60_79 = pygame.sprite.Group()
chicken_group_80_99 = pygame.sprite.Group()
chicken_group_100_125 = pygame.sprite.Group()
create_all_chickens_group()

# User Events
SPAWNCHICKEN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNCHICKEN, 500)
ONESECOND = pygame.USEREVENT + 2
pygame.time.set_timer(ONESECOND, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # Main game
        if game_state == "main":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # If you hit chicken, blood particles appear
                    hit, x, y, size = cursor.shoot(all_chickens_group, shot_sound, chicken_hit_sound)
                    if hit:
                        for i in range(7):
                            blood_particles.append(Particle(x, y))
                elif event.button == 3 and not cursor.is_reloading:
                    pressed_time = pygame.time.get_ticks()
                    cursor.is_reloading = True
            if event.type == SPAWNCHICKEN:
                if random.randint(0, 1) < 1:
                    chicken = Chicken(random.randint(30, SCREEN_H - 30))
                    add_chick_to_group(chicken)
                    # 25% to play chicken peep on the chicken spawn
                    if random.randint(-2, 1) == 0:
                        chicken_peep_sound.play()
            if event.type == ONESECOND:
                time_to_finish -= 1
            # Testing
            if event.type == pygame.KEYDOWN:
                pass
        # Intro
        elif game_state == "intro":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game_state = "main"

        # Highscore Table
        elif game_state == "highscore":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Reset everything
                if event.button == 3:
                    game_state = "intro"
                    for chicken_group in all_chickens_group:
                        chicken_group.empty()
                    score_manager = ScoreManager(user_name)
                    cursor_group.empty()
                    cursor = Cursor(score_manager)
                    cursor_group.add(cursor)
                    current_time = 0
                    time_to_finish = 60

        elif game_state == "set_name":
            if event.type == pygame.MOUSEBUTTONDOWN:
                input_active = True
                user_name = ""
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    if user_name == "":
                        user_name = "Unknown"
                    score_manager = ScoreManager(user_name)
                    cursor = Cursor(score_manager)
                    cursor_group = pygame.sprite.Group()
                    cursor_group.add(cursor)
                    game_state = "intro"
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                else:
                    user_name += event.unicode

    # Main Game
    screen.fill((0, 100, 0))
    background.draw_foreground()
    background.draw_ground()

    if game_state == "set_name":
        prompt_surf = game_font.render("Type your nickname", True, (255, 255, 255))
        name_surf = game_font.render(user_name, True, (255, 255, 255))
        screen.blit(name_surf, name_surf.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2)))
        screen.blit(prompt_surf, prompt_surf.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2 - 60)))
        pygame.display.flip()

    if game_state == "main":
        current_time = pygame.time.get_ticks()

        # Game Logic
        reloading()
        game_state = end_of_game()
        update_all_chickens()

        # Drawing
        background.draw_sky()

        chicken_group_20_39.draw(screen)
        chicken_group_40_59.draw(screen)

        if size < 60:
            for particle in blood_particles:
                particle.draw(screen)

        background.draw_foreground()
        background.draw_ground()

        chicken_group_60_79.draw(screen)
        chicken_group_80_99.draw(screen)
        chicken_group_100_125.draw(screen)

        if size >= 60:
            for particle in blood_particles:
                particle.draw(screen)

        display_time()
        score_manager.display_score(screen, game_font)

        cursor.draw_ammo(screen)

        cursor_group.update()
        cursor_group.draw(screen)

        pygame.display.flip()

    # Intro Screen
    elif game_state == "intro":
        decrease_light()
        display_intro_text()

        cursor_group.update()
        cursor_group.draw(screen)

        pygame.display.flip()

    # Highscore Screen
    elif game_state == "highscore":
        decrease_light()
        score_manager.draw_highscore_table(screen)
        pygame.display.flip()

    clock.tick(60)











