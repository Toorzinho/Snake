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
snake_segments = [(WIDTH // 2, HEIGHT // 2)]
snake_length = 1
speed = 10
direction = 'RIGHT'

# Food initial position
food_pos = (random.randint(0, (WIDTH - 10) // 10) * 10, random.randint(0, (HEIGHT - 10) // 10) * 10)

# Game loop
running = True
clock = pygame.time.Clock()
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
        new_head = (snake_segments[0][0], snake_segments[0][1] - speed)
    elif direction == 'DOWN':
        new_head = (snake_segments[0][0], snake_segments[0][1] + speed)
    elif direction == 'LEFT':
        new_head = (snake_segments[0][0] - speed, snake_segments[0][1])
    elif direction == 'RIGHT':
        new_head = (snake_segments[0][0] + speed, snake_segments[0][1])

    snake_segments.insert(0, new_head)

    # Draw the snake
    for segment in snake_segments:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], 10, 10))

    # Check if snake eats the food
    if snake_segments[0] == food_pos:
        snake_length += 1
        food_pos = (random.randint(0, (WIDTH - 10) // 10) * 10, random.randint(0, (HEIGHT - 10) // 10) * 10)

    # Update snake's length
    while len(snake_segments) > snake_length:
        snake_segments.pop()

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(15)

pygame.quit()
