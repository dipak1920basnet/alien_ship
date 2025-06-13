import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """
    Initialize game, settings and create a screen object.
    """

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Set the background color
    # bg_color = (230,230,230)

    # Start the main loop for the game.
    while True:
        # Watch for keybord and mouse events.
        gf.check_events()

        # Re-draw the screen during each pass through the loop
        gf.update_screen(ai_settings,screen,ship)


run_game()
