import pygame

from circuit_grid import CircuitGrid
import globals, ui, paddle, ball, computer

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():
    # Initialize the game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)
    classical_paddle = paddle.Paddle(9*globals.WIDTH_UNIT)
    classical_computer = computer.ClassicalComputer(classical_paddle)
    quantum_paddles = paddle.QuantumPaddles(globals.WINDOW_WIDTH - 9*globals.WIDTH_UNIT)
    pong_ball = ball.Ball()
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(classical_paddle)
    moving_sprites.add(quantum_paddles.paddles)
    moving_sprites.add(pong_ball)


    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)


        pong_ball.update()
        classical_computer.update(pong_ball)

        # Framerate
        

        # Update game (in progress)


        # Draw demo
        screen.fill(globals.BLACK)
        circuit_grid.draw(screen)
        ui.draw_statevector_grid(screen)
        moving_sprites.draw(screen)
        pygame.display.flip()
        

        # Set framerate
        clock.tick(60)


if __name__ == '__main__':
    main()