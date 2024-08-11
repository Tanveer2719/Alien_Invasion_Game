import pygame.font
class Live:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font
        self.font = pygame.font.SysFont(None, 15)
        self.font_color = (30, 30, 30)

        # build level life
        self.build_life()

    def build_life(self):
        self.level = "Life:" + str(self.stats.ships_left)
        self.level_img = self.font.render(self.level,True,self.font_color,self.settings.bg_color)

        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 100

    def draw_life(self):
        self.screen.blit(self.level_img, self.level_rect)
