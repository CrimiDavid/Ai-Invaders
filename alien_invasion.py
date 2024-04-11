import sys
from time import sleep

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from stats import Stats


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # Game Screen setup
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()  # Group Object used to manage different spirits(in a list)
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Stats
        self.stats = Stats(self)
        self.game_active = True

    def run_game(self):
        """ Main loop """
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(144)  # frames

    def _check_events(self):
        """Checks of player input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Key press input"""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Key release input"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create bullet and add to bullet group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  # Add bullet to the bullet group list

    def _update_screen(self):
        """Draw the screen each loop"""
        self.screen.fill(self.settings.bg_colour)
        for bullet in self.bullets:
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()  # This makes the visual output the player sees

    def _create_fleet(self):
        """Draw Aliens on screen"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size  # space each alien 1 alien width apart
        self.aliens.add(alien)  # draws alien at position specified by rect

        curr_x, curr_y = alien_width, alien_height
        while curr_y < (self.settings.screen_height - 3 * alien_height):
            while curr_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(curr_x, curr_y)
                curr_x += 2 * alien_width

            # row finished reset curr_x value and increment curr_y
            curr_x = alien_width
            curr_y += 2 * alien_height

    def _change_fleet_direction(self):
        """Lower fleet and change directions (helper funtion for "_check_fleet_edges")"""
        for alien in self.aliens:
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self):
        """check if alien is at edge, if so call (_change_fleet_direction)"""
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _create_alien(self, x_position, y_position):
        """Create Aliens"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Alien movement"""
        self._check_fleet_edges()
        self.aliens.update()

        # Aliens that hit ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        for alien in self.aliens:
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():  # Iterate over copy of the loop so original list won't affect the loop
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.centre_ship()

            sleep(1)
        else:
            self.game_active = False
            print("GAME OVER")


if __name__ == '__main__':
    # Make a game instance, and run game
    ai = AlienInvasion()
    ai.run_game()
