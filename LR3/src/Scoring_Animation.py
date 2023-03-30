from .Balloon import *


Board_font = pygame.font.SysFont("Showcard Gothic", 25)

ColorList = []
for i in range(len(Balloon_idle_Set)):
    tmp_img = Balloon_idle_Set[i][0]
    pixel_position = (32, 1)
    ColorList.append(tmp_img.get_at(pixel_position))
DARK_RED = (205, 70, 80)


class ScoringAnimation(pygame.sprite.Sprite):
    def __init__(self, position, offset_y, color_index, scoring_amplifier, delta_time):
        super().__init__()
        self.image = Board_font.render(f'+{scoring_amplifier}', True, pygame.Color(ColorList[color_index]))
        self.rect = self.image.get_rect()
        self.initialY = position[1] - offset_y
        self.rect.center = self.position = Vector2(position[0], self.initialY)
        self.velocity = Vector2(0, -0.2)
        self.d_t = delta_time

    def update(self):
        self.position += self.velocity * self.d_t
        self.rect.center = self.position

        if self.position.y - self.initialY <= -50:
            self.kill()
