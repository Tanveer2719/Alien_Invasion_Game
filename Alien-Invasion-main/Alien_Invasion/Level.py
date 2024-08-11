import pygame.font

class Level:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font
        self.font = pygame.font.SysFont(None, 15)
        self.font_color = (30, 30, 30)

        # build level label
        self.build_level()

    def build_level(self):
        self.level = "Level:" + str(self.stats.level)
        self.level_img = self.font.render(self.level,True,self.font_color,self.settings.bg_color)

        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 60

    def draw_level(self):
        self.screen.blit(self.level_img,self.level_rect)