import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create the bullet
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_length)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the value of the position of the bullet
        self.bullet_y = float(self.rect.y)


    # update the bullet position
    def update(self):
        self.bullet_y -= self.settings.bullet_speed
        self.rect.y = self.bullet_y

    # draw the bullet in the screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

