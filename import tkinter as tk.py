import pygamesnipp
import time
import random

# Initialize the game
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the snake and food dimensions
snake_size = 20
snake_speed = 15

# Set the font style and size
font_style = pygame.font.SysFont(None, 50)

# Function to display the score on the screen
def show_score(score):
    score_value = font_style.render("Score: " + str(score), True, black)
    game_display.blit(score_value, [10, 10])

# Function to draw the snake on the screen
def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], snake_size, snake_size])

# Function to run the game
def game_loop():
    game_over = False
    game_exit = False

    # Set the starting position of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Set the initial change in position of the snake
    x1_change = 0
    y1_change = 0

    # Create the snake list
    snake_list = []
    snake_length = 1

    # Generate the initial food position
    food_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0

    # Game loop
    while not game_exit:
        while game_over:
            # Display the game over message
            game_display.fill(white)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            game_display.blit(message, [screen_width / 6, screen_height / 3])
            show_score(snake_length - 1)
            pygame.display.update()

            # Event handling for game over screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling for game screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size


