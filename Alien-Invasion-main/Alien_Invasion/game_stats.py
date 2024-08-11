import pygame

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False


    def reset_stats(self):
        self.ships_left = self.settings.ship_remaining
        self.settings.initial_speed_settings()
        self.level = 1
        self.score = 0