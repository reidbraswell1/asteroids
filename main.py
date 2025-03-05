# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import the connect_database function
from constants import *

# import player
from player import Player



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame_clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Properly exit the loop

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = pygame_clock.tick(60) / 1000  # Keep frame rate stable

    pygame.quit()  # Ensure Pygame properly exits

    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()