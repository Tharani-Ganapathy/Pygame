class GameStats: # track statistics for alien invasion
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.reset_stats()
        # start game in an inactive state
        self.game_active = False


    def reset_stats(self): # initialize statistics that can change during the game
        self.ship_left = self.game_settings.ship_limit
        self.score = 0
        self.high_score = 0
        self.level = 1

