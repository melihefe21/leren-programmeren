import pygame
import os

# Initialization
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mens Erger Je Niet")

# Colors
WHITE = (255, 255, 255)

# File paths
current_dir = os.path.dirname(os.path.realpath(__file__))
board = os.path.dirname(os.path.realpath(__file__)) + 'board.png'
red_pawn = os.path.dirname(os.path.realpath(__file__)) + 'red_pawn.png'
green_pawn = os.path.dirname(os.path.realpath(__file__)) + 'green_pawn.png'
blue_pawn = os.path.dirname(os.path.realpath(__file__)) + 'blue_pawn.png'
yellow_pawn = os.path.dirname(os.path.realpath(__file__)) + 'yellow_pawn.png'

# Board and pawn positions
BOARD_X, BOARD_Y = 50, 50
RED_X, RED_Y = 300, 550
GREEN_X, GREEN_Y = 350, 550
BLUE_X, BLUE_Y = 300, 500
YELLOW_X, YELLOW_Y = 350, 500

# Load images
board_image = pygame.image.load(board)
# bord
red_pawn_image = pygame.image.load(red_pawn)
green_pawn_image = pygame.image.load(green_pawn)
blue_pawn_image = pygame.image.load(blue_pawn)
yellow_pawn_image = pygame.image.load(yellow_pawn)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen
    screen.fill(WHITE)

    # Draw the board
    screen.blit(board_image, (BOARD_X, BOARD_Y))

    # Draw pawns
    screen.blit(red_pawn_image, (RED_X, RED_Y))
    screen.blit(green_pawn_image, (GREEN_X, GREEN_Y))
    screen.blit(blue_pawn_image, (BLUE_X, BLUE_Y))
    screen.blit(yellow_pawn_image, (YELLOW_X, YELLOW_Y))

    # Update the screen
    pygame.display.update()

# Quit the game
pygame.quit()