import sys
import pygame
from pygame.sprite import Sprite
from game_stats import GameStats
from settings import Settings
from button import Button
from time import sleep
from lives import Live
from show_score import ShowScore
from Level import Level
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """ class to manage the overall activity """
    def __init__(self):
        """ initialize the game screen """
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((self.settings.height, self.settings.width))
        self.bg_color = (self.settings.bg_color)
        self.button = Button(self, "Play")
        self.show_score = ShowScore(self)
        self.level = Level(self)
        self.life = Live(self)
        pygame.display.set_caption("Alien Invasion")

        # create a available list of bullets
        self.bullets = pygame.sprite.Group()

        # create a list of aliens
        self.aliens = pygame.sprite.Group()
        self.create_fleet()

        """ built the ship """
        self.ship = Ship(self)

    def create_alien(self, alien_no, alien_row):
        n_alien = Alien(self)
        alien_width = n_alien.rect.width
        alien_height = n_alien.rect.height
        n_alien.x = 60 + 2 * alien_width * alien_no
        n_alien.rect.x = n_alien.x
        n_alien.rect.y = n_alien.rect.height + 2 * n_alien.rect.height * alien_row
        self.aliens.add(n_alien)

    # method for creating aliens
    def create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_horizontal_space = self.settings.width - (6*alien_width)
        possible_aliens = available_horizontal_space // alien_width

        available_vertical_space = self.settings.height - (6 * alien_height) - 200
        possible_rows = available_vertical_space // (2*alien_height)


        # draw first row of the fleet
        for alien_row in range(possible_rows):
            for alien_no in range(possible_aliens):
                self.create_alien(alien_no, alien_row)

    # method for various events
    def _check_events_(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                """ if the command is to quit then exit the system """
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._key_press(event)

            elif event.type == pygame.KEYUP:
                self._key_release(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    # fire Bullet
    def fire_bullet(self):
        self.new_bullet = Bullet(self)
        self.bullets.add(self.new_bullet)

    # Respond to key Press
    def _key_press(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_SPACE:
            if len(self.bullets) <= self.settings.max_bullet_allowed:       # limit the no. of bullets visible in the screen
                self.fire_bullet()

        if event.key == pygame.K_q:
            sys.exit()

        if event.key == pygame.K_p and not self.stats.game_active:
            self.start_game()

    # Respond to key release
    def _key_release(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # method for showing changes in the screen
    def _show_screen_(self):
        """ update the background color"""
        self.screen.fill(self.bg_color)

        """ draw the ship in the screen """
        self.ship.blitme()

        """ draw the bullets """
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        """ show aliens in the screen """
        self.aliens.draw(self.screen)

        """ make play button visible"""
        if not self.stats.game_active:
            self.button.draw_button()

        """ show scoreboard"""
        self.show_score.draw_scoreboard()

        """ show level """
        self.level.draw_level()

        "show lives"
        self.life.draw_life()

        """ Make the screen visible"""
        pygame.display.flip()

    def check_for_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_direction()
                break

    def change_direction(self):
        self.settings.moving_direction *= -1
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed

    def aliens_hitting_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self.ship_hit()
                break

    def update_aliens(self):
        self.check_for_edges()
        self.aliens.update()

    def collision(self):
        """check for bullets that have hit the aliens and remove both the aliens and the bullet"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for alien in collisions.values():
                self.stats.score += self.settings.killing_points * len(alien)
            self.show_score.prep_score()

    def update_level(self):
        self.stats.level += 1
        self.level.build_level()

    def new_alien_fleet(self):
        """if the fleet is empty then introduce more aliens"""
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()
            self.update_level()

    def update_bullets(self):
        self.bullets.update()

        # delete bullets from bullets list that go out of scope
        for bullet in self.bullets.sprites().copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.collision()
        self.new_alien_fleet()

    def ship_hit(self):
        if self.stats.ships_left>0:
            self.stats.ships_left -= 1      # reduce the live and update
            print(self.stats.ships_left)
            self.life.build_life()

            """ destroy all the bullets and the aliens remaining"""
            self.aliens.empty()
            self.bullets.empty()

            """ create new aliens and bullets"""
            self.create_fleet()
            self.ship.center_ship()

            # pause the game
            sleep(.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def start_game(self):
        self.stats.reset_stats()
        self.stats.game_active = True

        # delete all the aliens
        self.aliens.empty()
        self.bullets.empty()

        # initialize new aliens
        self.create_fleet()
        self.ship.center_ship()

        # hide the mouse
        pygame.mouse.set_visible(False)

    def check_play_button(self, mouse_pos):
        """ start the game if play clicked"""
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
           self.start_game()

    def end_game(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

    def run_game(self):
        """ start the main loop of the game """
        while True:
            self._check_events_()
            if self.stats.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_aliens()
                self.end_game()

            self._show_screen_()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


