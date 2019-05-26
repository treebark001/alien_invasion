import sys, pygame
from settings import Settings
from ship import Ship

# 246 (284 of 248) - last page was working on

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()



        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            #self.settings.screen_width = self.screen.get_rect().width
            #self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width,
                self.settings.screen_height))



        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)



    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_screen()


    def _check_events(self):
        '''Respond to key presses and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True
        elif self.settings.up_and_down:
            if event.key == pygame.K_UP:
                # Move the ship to the left.
                self.ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                # Move the ship to the left.
                self.ship.moving_down = True
        if self.settings.ship_speed_adjust:
            if event.key == 269 and self.settings.ship_speed > 0.15:
                self.settings.ship_speed -= 0.1
            elif event.key == 270:
                self.settings.ship_speed += 0.1



    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
                self.ship.moving_down = False


    def _update_screen(self):
        '''Update images on the screen, fill to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
