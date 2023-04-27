import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self, bg_path: str):
        super(CameraGroup, self).__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2

        # camera box setup
        self.camera_borders = {'left': self.display_surface.get_width() // 20,
                               'right': self.display_surface.get_width() // 20,
                               'top': 0,
                               'bottom': 0}
        left = self.camera_borders['left']
        top = self.camera_borders['top']
        width = self.display_surface.get_width() - (self.camera_borders['left'] + self.camera_borders['right'])
        height = self.display_surface.get_height() - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(left, top, width, height)

        # camera speed
        self.mouse_speed = round(self.display_surface.get_width() / 250, 2)

        # background init
        self.bg_surf = pygame.image.load(bg_path).convert_alpha()
        self.bg_surf = pygame.transform.scale(self.bg_surf, (self.display_surface.get_width() * 3,
                                                             self.display_surface.get_height()))
        self.bg_rect = self.bg_surf.get_rect(topleft=(0, 0))

    def mouse_control(self):
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_offset_vector = pygame.math.Vector2()

        left_border = self.camera_borders['left']
        right_border = self.display_surface.get_width() - self.camera_borders['right']
        top_border = self.camera_borders['top']
        bottom_border = self.display_surface.get_height() - self.camera_borders['bottom']

        # check mouse for movement
        if top_border < mouse.y < bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector.x = mouse.x - left_border
                pygame.mouse.set_pos((left_border, mouse.y))
            if mouse.x > right_border:
                mouse_offset_vector.x = mouse.x - right_border
                pygame.mouse.set_pos((right_border, mouse.y))
        elif mouse.y < top_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2((left_border, top_border))
                pygame.mouse.set_pos((left_border, top_border))
            elif mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2((right_border, top_border))
                pygame.mouse.set_pos((left_border, top_border))
        elif mouse.y > top_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2((left_border, bottom_border))
                pygame.mouse.set_pos((left_border, top_border))
            elif mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2((right_border, bottom_border))
                pygame.mouse.set_pos((left_border, top_border))
        if left_border < mouse.x < right_border:
            if mouse.y < top_border:
                mouse_offset_vector.y = mouse.y - top_border
                pygame.mouse.set_pos((mouse.x, top_border))
            if mouse.y > bottom_border:
                mouse_offset_vector.y = mouse.y - bottom_border
                pygame.mouse.set_pos((mouse.x, bottom_border))

        self.offset += mouse_offset_vector * self.mouse_speed
        if self.offset.x < 0:
            self.offset.x = 0
        elif self.offset.x > self.bg_rect.w:
            self.offset.x = self.bg_rect.w
        if self.offset.y < 0:
            self.offset.y = 0
        elif self.offset.y > self.bg_rect.h:
            self.offset.y = self.bg_rect.h

    def upgrade_mouse_control(self):
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())

        left_border = self.camera_borders['left']
        right_border = self.display_surface.get_width() - self.camera_borders['right']
        top_border = self.camera_borders['top']
        bottom_border = self.display_surface.get_height() - self.camera_borders['bottom']

        if top_border < mouse.y < bottom_border:
            if mouse.x < left_border:
                self.offset.x -= self.mouse_speed
            if mouse.x > right_border:
                self.offset.x += self.mouse_speed
        if left_border < mouse.x < right_border:
            if mouse.y < top_border:
                self.offset.x -= self.mouse_speed
            if mouse.y > bottom_border:
                self.offset.y += self.mouse_speed

        if self.offset.x < 0:
            self.offset.x = 0
        elif self.offset.x > self.bg_rect.w - self.display_surface.get_width():
            self.offset.x = self.bg_rect.w - self.display_surface.get_width()
        if self.offset.y < 0:
            self.offset.y = 0
        elif self.offset.y > self.bg_rect.h - self.display_surface.get_height():
            self.offset.y = self.bg_rect.h - self.display_surface.get_height()

    def custom_draw(self):
        # self.mouse_control()
        self.upgrade_mouse_control()

        # background draw
        bg_offset = self.bg_rect.topleft - self.offset
        self.display_surface.blit(self.bg_surf, bg_offset)

        # active sprites
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.bottom):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
