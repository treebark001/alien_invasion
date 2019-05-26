

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.05

        # Full screen?
        self.full_screen = False

        # Allow ship to move up and down
        self.up_and_down = True

        # Allow ship speed to be adjusted
        self.ship_speed_adjust = True
