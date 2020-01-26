class Settings():
    # A class to store all the settings of alien_invasion
    def __init__(self):
        # initialize the game's static settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # ship settings
        self.ship_limit = 2

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # alien settings
        self.fleet_drop_speed = 100

        #how quickly the game speeds up
        self.speedup_scale = 1.1

        #scoring
        self.alien_points = 50


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # initialize settings that change throughout the game
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 1
        # fleet direction of 1 rep right, -1 rep left
        self.fleet_direction = 1
        # how quickly the alien points value increases
        self.score_scale = 1.5

    def increase_speed(self):
        # increase speed settings
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)