class Settings:

    def __init__(self):
        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        self.ship_speed = 1.5
        # bullet
        self.bullet_speed = 3
        self.bullet_width = 45
        self.bullet_height = 55
        self.bullet_allowed = 3

        # Alien ships
        self.alien_width = 59
        self.alien_height = 59
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Game stats
        self.lives = 3


