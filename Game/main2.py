import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('My Pygame Window')

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Other game logic or drawing goes here

        # Update the display
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
