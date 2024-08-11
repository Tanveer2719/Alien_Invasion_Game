""" this is a settings class that will contain all the necessary settings """


class Settings:
    def __init__(self):
        self.width = 600
        self.height = 800
        self.bg_color = (230, 230, 230)

        # Bullet
        self.bullet_length = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.max_bullet_allowed = 4

        # Ship
        self.ship_remaining = 3
        self.alien_horizontal_speed = 0.1

        self.speed_increase = 1.1
        self.killing_points = 30
        self.points_increase = 2
        self.initial_speed_settings()


    def initial_speed_settings(self):
        self.bullet_speed = 0.5
        self.alien_drop_speed = 10.0
        self.ship_speed = 1.5

        self.moving_direction = 1  # 1 for moving right and -1 for moving left

    def increase_speed(self):
        self.bullet_speed *= self.speed_increase
        self.alien_drop_speed *= self.speed_increase
        self.ship_speed *= self.speed_increase
        self.killing_points *= self.points_increase



