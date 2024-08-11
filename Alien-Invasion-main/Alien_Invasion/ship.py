import pygame
from settings import Settings

class Ship:
    def __init__(self, ai_game):        # ai_game is an object of class alienInvasion
        self.screen = ai_game.screen    # get the screen
        self.screen_rect = ai_game.screen.get_rect()    # get the screen as a rectangle

        self.image = pygame.image.load("Images/ship.bmp")   # load the image and get the rectangle of the image
        self.rect = self.image.get_rect()
        self.center_ship()

        self.moving_right = False   # flag to check if the right button is clicked
        self.moving_left = False    # flag to check if the left button is clicked

        self.setting = Settings()
        self.ship_speed = self.setting.ship_speed


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.ship_x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.ship_x -= self.ship_speed

        """update rect.x from ship_x"""
        self.rect.x = self.ship_x


    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom  # the initial position of the ship
        self.ship_x = float(self.rect.x)


    def blitme(self):
        self.screen.blit(self.image, self.rect)