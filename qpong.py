import pygame

from circuit_grid import CircuitGrid
import globals, ui, paddle

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():
    # Initialize the game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)
    classical_paddle = paddle.Paddle()
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(classical_paddle)


    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        # Framerate
        

        # Update game (in progress)


        # Draw demo
        circuit_grid.draw(screen)
        ui.draw_statevector_grid(screen)
        circuit_grid.draw(screen)
        pygame.display.flip()
        

        # Set framerate
        clock.tick(60)


if __name__ == '__main__':
    main()