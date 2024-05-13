import pygame

# Initiate the game
pygame.init()

# Display
screen1 = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('mafia.jpg')

# Title and Icon#
pygame.display.set_caption("Mafiaso")
icon = pygame.image.load('mafia.jpg')
pygame.display.set_icon(icon) 


# Game loop
running = True 
while running:
    
    screen1.fill((171,137,71))

    screen1.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False