import pygame.font


class Scoreboard:
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)  # Corrected spelling for consistency
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_colour)  # Assuming bg_color exists in settings


        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top  # Set the top position of the score; it was missing

    def show_score(self):
        """Draw scores to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_colour)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top + 5  # Adjust this value as needed

    def check_high_score(self):
        """Check if there is a new high score, and update if there is."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score  # Corrected to update the high score
            self.prep_high_score()

    def reset_score(self):
        """Reset the score to zero and update the display."""
        self.stats.score = 0  # Reset the current score to zero
        self.prep_score()  # Update the score display to reflect the reset