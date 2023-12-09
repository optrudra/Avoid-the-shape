import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
SHAPE_WIDTH, SHAPE_HEIGHT = 30, 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Shapes!")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player properties
player_x = (WIDTH - PLAYER_WIDTH) // 2
player_y = HEIGHT - PLAYER_HEIGHT - 10
player_speed = 5

# List to store falling shapes
shapes = []

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, PLAYER_WIDTH, PLAYER_HEIGHT])

# Function to draw a falling shape
def draw_shape(x, y):
    pygame.draw.rect(screen, RED, [x, y, SHAPE_WIDTH, SHAPE_HEIGHT])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
        player_x += player_speed

    # Add a new shape at the top
    if random.randint(0, 100) < 5:
        shape_x = random.randint(0, WIDTH - SHAPE_WIDTH)
        shape_y = 0
        shapes.append((shape_x, shape_y))

    # Move shapes down
    for i in range(len(shapes)):
        shapes[i] = (shapes[i][0], shapes[i][1] + 5)

    # Check for collisions with the player
    for shape in shapes:
        if (
            player_x < shape[0] + SHAPE_WIDTH
            and player_x + PLAYER_WIDTH > shape[0]
            and player_y < shape[1] + SHAPE_HEIGHT
            and player_y + PLAYER_HEIGHT > shape[1]
        ):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Remove shapes that are out of the screen
    shapes = [shape for shape in shapes if shape[1] < HEIGHT]

    # Clear the screen
    screen.fill(BLACK)

    # Draw the player
    draw_player(player_x, player_y)

    # Draw the falling shapes
    for shape in shapes:
        draw_shape(shape[0], shape[1])

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)
