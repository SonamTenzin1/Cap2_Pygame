import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Word Puzzle Game")

# Set up the font for displaying text
font = pygame.font.SysFont(None, 50)

# Set up the levels
levels = [
    {"words": ["apple", "banana", "orange"], "time_limit": 10},
    {"words": ["dog", "cat", "bird"], "time_limit": 8},
    {"words": ["python", "java", "javascript"], "time_limit": 5},
    {"words": ["car", "bus", "train"], "time_limit": 7},
    {"words": ["red", "green", "blue"], "time_limit": 6},
    {"words": ["book", "pen", "pencil"], "time_limit": 8},
    {"words": ["house", "building", "apartment"], "time_limit": 10},
    {"words": ["happy", "sad", "angry"], "time_limit": 7},
    {"words": ["sun", "moon", "star"], "time_limit": 6},
    {"words": ["water", "juice", "soda"], "time_limit": 8},
    {"words": ["football", "basketball", "tennis"], "time_limit": 9},
]

# Initialize player's score and current level
score = 0
current_level_index = 0

# Main game loop
running = True
while running:
    # Set up the current level
    current_level = levels[current_level_index]
    words = current_level["words"]
    time_limit = current_level["time_limit"]
    jumbled_words = ["".join(random.sample(word, len(word))) for word in words]

    # Set up the timer
    clock = pygame.time.Clock()
    time_remaining = time_limit * 1000

    # Initialize current word index and input word
    current_word_index = 0
    input_word = ""

    # Level loop
    level_running = True
    while level_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level_running = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    level_running = False

                # Handle player input
                elif event.key == pygame.K_BACKSPACE:
                    input_word = input_word[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_word.lower() == words[current_word_index]:
                        score += 1

                    # Move to the next word or end the level
                    current_word_index += 1
                    if current_word_index >= len(jumbled_words):
                        level_running = False

                        # Move to the next level or end the game
                        current_level_index += 1
                        if current_level_index >= len(levels):
                            running = False

        # Clear the game window
        game_window.fill((0, 0, 0))

        # Display the jumbled word and input word
        current_word = jumbled_words[current_word_index]
        text_surface = font.render(current_word, True, (255, 255, 255))
        game_window.blit(text_surface, (50, 50))
        input_text_surface = font.render(input_word, True, (255, 255, 255))
        game_window.blit(input_text_surface, (50, 150))

        # Display the score and time remaining
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        game_window.blit(score_text, (50, 250))
        time_remaining_text = font.render(f"Time Remaining: {int(time_remaining / 1000)}", True, (255, 255, 255))
        game_window.blit(time_remaining_text, (50, 350))

        # Update the display
        pygame.display.update()

        # Update the timer and check if time is up
        time_remaining -= clock.tick(60)
        if time_remaining <= 0:
            level_running = False

# End of game loop
game_over_text = font.render(f"Game Over! Final score: {score}", True, (255, 255, 255))
game_window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - game_over_text.get_height() // 2))

