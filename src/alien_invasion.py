import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption('Alien Invasion')
        
        self.ship = Ship(self)
        
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update_movement()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.is_moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.is_moving_left = True
        elif event.key == pygame.K_DOWN:
            self.ship.is_moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.is_moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.is_moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.is_moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.is_moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.is_moving_up = False

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    