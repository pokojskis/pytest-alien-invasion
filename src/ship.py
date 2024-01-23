import pygame


class Ship:
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ships/1.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.settings = ai_game.settings
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_down = False
        self.is_moving_up = False

    def update_movement(self):
        if self.is_moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.is_moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        elif self.is_moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
        elif self.is_moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed

        # self.rect.x = self.pos_x
        # self.rect.y = self.pos_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)