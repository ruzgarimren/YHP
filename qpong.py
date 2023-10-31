import pygame

from assets.circuit_grid import CircuitGrid
from assets import globals

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():
    # initialize the game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)

    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        # framerate
        clock.tick(60)

        # update game



        # draw demonstration    
        pygame.display.flip()
        circuit_grid.draw(screen)



if __name__ == '__main__':
    main()