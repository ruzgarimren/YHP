import pygame

from circuit_grid import CircuitGrid
import globals, ui, paddle, ball, computer

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('QPong')
pygame.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT))
clock = pygame.time.Clock()


# Load game over sound
game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')

# Load victory sound
victory_sound = pygame.mixer.Sound('sounds/victory.wav')


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
    

    game_over_sound_playing = False
    victory_sound_playing = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        # Update game
        pong_ball.update(quantum_computer=quantum_computer, classical_computer=classical_computer)
        classical_computer.update(pong_ball)
        quantum_computer.update(pong_ball)

        # Draw game
        screen.fill(globals.BLACK)

        if classical_computer.score >= globals.WIN_SCORE:
            if not game_over_sound_playing:
                pygame.mixer.Sound.play(game_over_sound)
                game_over_sound_playing = True
            ui.draw_lose_scene(screen)
        elif quantum_computer.score >= globals.WIN_SCORE:
            if not victory_sound_playing:
                pygame.mixer.Sound.play(victory_sound)
                victory_sound_playing = True
            ui.draw_win_scene(screen)
        else:
            circuit_grid.draw(screen)
            ui.draw_statevector_grid(screen)
            ui.draw_score(screen, classical_computer.score, quantum_computer.score)
            ui.draw_dashed_line(screen)
            moving_sprites.draw(screen)
        pygame.display.flip()
        

        # Set framerate
        clock.tick(75)


if __name__ == '__main__':
    main()