class Stats:
    """Track game stats"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
    def reset_stats(self):
        self.ships_left = self.settings.lives
        self.score = 0
        
        
        
