import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # button create
        self.width, self.height = 200, 50
        self.button_color = (0,230,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        # build buttons rect object
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # print msg
        self.message(msg)

    def message(self, msg):
        # turn msg into a picture in the button
        self.img_text = self.font.render(msg,True,self.text_color,self.button_color)

        # get the rectangle and make the image at the center of the button
        self.img_text_rect = self.img_text.get_rect()
        self.img_text_rect.center = self.rect.center


    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.img_text, self.img_text_rect)

