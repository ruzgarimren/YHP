import pygame
import numpy as np
import os


import globals, resources

def draw_statevector_grid(screen):
    font = resources.Font()
    basis_states = [
        '|000>',
        '|001>',
        '|010>',
        '|011>',
        '|100>',
        '|101>',
        '|110>',
        '|111>'
    ]
    statevector_height = int(round(globals.FIELD_HEIGHT / len(basis_states)))

    for i in range(len(basis_states)):
        text = font.vector_font.render(basis_states[i], 1, globals.WHITE)
        screen.blit(text, (globals.WINDOW_WIDTH - text.get_width(),
                           i*statevector_height + text.get_height()))


# Draw superposition animation
def draw_superposition_animation(screen):
    radius = 20
    x = np.sin(pygame.time.get_ticks() * 0.002) * 100 + screen.get_width() / 2
    y = screen.get_height() / 2
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), radius)

# Create quantum entanglement effect
def draw_entanglement_effect(screen):
    start_pos = (100, 100)
    end_pos = (200, 200)
    pygame.draw.line(screen, (0, 255, 0), start_pos, end_pos, 2)

# Draw dynamic quantum background
def draw_quantum_background(screen):
    for i in range(0, screen.get_width(), 20):
        amplitude = 20
        wave_length = 100
        y = np.sin(i / wave_length) * amplitude + screen.get_height() / 2
        pygame.draw.circle(screen, (0, 0, 255), (i, int(y)), 5)

# Draw base-2 numeral system (binary) animation
def draw_binary(screen, binary_value, position, font, color=(255, 255, 255)):
    binary_text = font.render(binary_value, font, color)
    screen.blit(binary_text, position)

# Draw current score
def draw_score(screen, classical_score, quantum_score):
    font = resources.Font()

    text = font.player_font.render("Classical Computer", 1, globals.GRAY)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH*0.3, globals.WIDTH_UNIT*2))
    screen.blit(text, text_pos)

    text = font.score_font.render(str(classical_score), 1, globals.GRAY)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH*0.3, globals.WIDTH_UNIT*8))
    screen.blit(text, text_pos)

    text = font.player_font.render("Quantum Computer", 1, globals.GRAY)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH*0.7, globals.WIDTH_UNIT*2))
    screen.blit(text, text_pos)

    text = font.score_font.render(str(quantum_score), 1, globals.GRAY)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH*0.7, globals.WIDTH_UNIT*8))
    screen.blit(text, text_pos)

def draw_dashed_line(screen):
    for i in range(10, globals.FIELD_HEIGHT, 2 * globals.WIDTH_UNIT): 
        pygame.draw.rect(
            screen,
            globals.GRAY,
            (globals.WINDOW_WIDTH // 2 - 5, i, 0.5 * globals.WIDTH_UNIT, globals.WIDTH_UNIT),
            0,
        )


def draw_lose_scene(screen):
    
    font = resources.Font()

    gameover_text = "Game Over"
    text = font.gameover_font.render(gameover_text, 1, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*10))
    screen.blit(text, text_pos)

    gameover_text = "Classical Computer"
    text = font.replay_font.render(gameover_text, 5, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*22))
    screen.blit(text, text_pos)

    gameover_text = "Still rules the world"
    text = font.replay_font.render(gameover_text, 5, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*27))
    screen.blit(text, text_pos)

