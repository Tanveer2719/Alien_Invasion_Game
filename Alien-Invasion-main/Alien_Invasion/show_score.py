import pygame.font

class ShowScore:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font
        self.font_color = (30,30,30)
        self.font = pygame.font.SysFont(None,15)

        # create font
        self.prep_score()

    def prep_score(self):
        self.score = "Score :" + str(self.stats.score)
        self.score_img = self.font.render(self.score,True,self.font_color,self.settings.bg_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw_scoreboard(self):
        self.screen.blit(self.score_img,self.score_rect)
