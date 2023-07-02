import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint Program")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the drawing variables
drawing = False
last_pos = None
radius = 10

window.fill(WHITE)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                pygame.draw.line(window, BLACK, last_pos, current_pos, radius)
                last_pos = current_pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Press 'q' key to quit
                running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
