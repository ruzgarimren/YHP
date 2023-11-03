import pygame

from circuit_grid import CircuitGrid
import globals, ui, paddle, ball, computer

pygame.init()
screen = pygame.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_WIDTH))
pygame.display.set_caption('QPong')
pygame.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

def main():
    # Initialize the game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)
    classical_paddle = paddle.Paddle(9*globals.WIDTH_UNIT)
    classical_computer = computer.ClassicalComputer(classical_paddle)
    quantum_paddles = paddle.QuantumPaddles(globals.WINDOW_WIDTH - 9*globals.WIDTH_UNIT)
    quantum_computer = computer.QuantumComputer(quantum_paddles, circuit_grid)
    pong_ball = ball.Ball()
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(classical_paddle)
    moving_sprites.add(quantum_paddles.paddles)
    moving_sprites.add(pong_ball)
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

                
        pong_ball.update(quantum_computer=quantum_computer, classical_computer=classical_computer)
        classical_computer.update(pong_ball)
        quantum_computer.update(pong_ball)

        # Update game (in progress)


        # Draw demo
        screen.fill(globals.BLACK)
        circuit_grid.draw(screen)
        ui.draw_statevector_grid(screen)
        moving_sprites.draw(screen)
        pygame.display.flip()
        

        # Set framerate
        clock.tick(75)


if __name__ == '__main__':
    main()