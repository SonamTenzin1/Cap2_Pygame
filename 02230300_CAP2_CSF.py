import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Word Puzzle Game")

# Set up the timer
TIME_LIMIT = 60
clock = pygame.time.Clock()
time_remaining = TIME_LIMIT * 1000

# Generate jumbled words
words = ["apple", "banana", "orange"]
jumbled_words = ["".join(random.sample(word, len(word))) for word in words]

# Set up the font for displaying text
font = pygame.font.SysFont(None, 50)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Draw the jumbled words on the screen
    for i, jumbled_word in enumerate(jumbled_words):
        text_surface = font.render(jumbled_word, True, (255, 255, 255))
        game_window.blit(text_surface, (50, 50 + i * 50))

    # Update the timer
    time_remaining -= clock.tick(60)
    if time_remaining <= 0:
        # End the game when time runs out
        break

    # Update the display
    pygame.display.update()

# End of game loop
final_score = 0  # TODO: Calculate the final score based on the player's performance
game_over_text = font.render(f"Game Over! Final score: {final_score}", True, (255, 255, 255))
game_window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.update()

# Wait for a few seconds before quitting the game
pygame.time.wait(3000)
pygame.quit()
sys.exit()
