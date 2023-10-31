import pygame

from circuit_grid import CircuitGrid
import globals

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():
    # Initialize the game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)

    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        # Framerate
        clock.tick(60)

        # Update game (in progress)



        # Draw demonstration    
        pygame.display.flip()
        circuit_grid.draw(screen)



if __name__ == '__main__':
    main()