import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake initial position, length, and speed
snake_pos = [(WIDTH // 2, HEIGHT // 2)]
snake_length = 1
speed = 5
direction = 'RIGHT'

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
                
     # Move the snake
    if direction == 'UP':
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - speed)
    elif direction == 'DOWN':
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + speed)
    elif direction == 'LEFT':
        snake_pos[0] = (snake_pos[0][0] - speed, snake_pos[0][1])
    elif direction == 'RIGHT':
        snake_pos[0] = (snake_pos[0][0] + speed, snake_pos[0][1])