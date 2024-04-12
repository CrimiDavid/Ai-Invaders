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
        self.alien_points = 100

        # Game stats
        self.lives = 3

        # Difficulty
        self.speed_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.alien_points *= self.speed_scale
