import pygame

from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image
        self.image = pygame.image.load("Images/Alien.bmp")
        self.rect = self.image.get_rect()

        # alien will show at the top left corner
        self.rect.x = 0
        self.rect.y = 10

        self.x = float(self.rect.x)


    def check_edges(self):
        self.screen_rect = self.screen.get_rect()

        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        self.x += (self.settings.alien_horizontal_speed * self.settings.moving_direction)
        self.rect.x = self.x

