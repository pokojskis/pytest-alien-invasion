class Settings:
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        self.ship_speed = 10.0
        self.ship_limit = 3
        self.bullet_speed = 15.0
        self.bullet_width = 300  # todo: change back
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10  # todo: change back
        self.alien_speed = 5
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

