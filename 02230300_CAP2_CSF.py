import pygame
import random
import sys

class JumbleWordGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the game window
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.game_window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Jumble Word Game")

        # Set up the font for displaying text
        self.font = pygame.font.SysFont(None, 50)

        # Set up the levels
        self.levels = [
            {"words": ["apple"], "time_limit": 10},
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
        self.score = 0
        self.current_level_index = 0

    def run(self):
        # Main game loop
        running = True
        while running:
            # Set up the current level
            current_level = self.levels[self.current_level_index]
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
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_BACKSPACE:
                            input_word = input_word[:-1]
                        elif event.key == pygame.K_RETURN:
                            if input_word.lower() == words[current_word_index]:
                                self.score += 1
                                current_word_index += 1
                                input_word = ""
                                if current_word_index >= len(words):
                                    self.current_level_index += 1
                                    if self.current_level_index >= len(self.levels):
                                        # End of game
                                        level_running = False
                                        running = False
                                    else:
                                        # Move to the next level
                                        level_running = False
                            else:
                                input_word = ""

                        else:
                            input_word += event.unicode
                
                # Clear the game window
                self.game_window.fill((0, 0, 0))

                # Display the current level
                level_text = self.font.render(f"Current Level: {self.current_level_index + 1}", True, (255, 255, 255))
                self.game_window.blit(level_text, (10, 10))

                # Display the jumbled word or game over text
                if current_word_index < len(jumbled_words):
                    current_word = jumbled_words[current_word_index]
                    text_surface = self.font.render(current_word, True, (255, 255, 255))
                    self.game_window.blit(text_surface, (50, 50))

                    # Display the player's input
                    input_surface = self.font.render(input_word, True, (255, 255, 255))
                    self.game_window.blit(input_surface, (50, 150))
                else:
                    game_over_text = self.font.render("Level Complete!", True, (255, 255, 255))
                    self.game_window.blit(game_over_text, (self.WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, self.WINDOW_HEIGHT // 2 - game_over_text.get_height() // 2))

                # Display the score and time remaining
                score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
                self.game_window.blit(score_text, (50, 250))
                time_text = self.font.render(f"Time: {int(time_remaining / 1000)}s", True, (255, 255, 255))
                self.game_window.blit(time_text, (50, 350))

                # Update the display
                pygame.display.update()

                # Decrease time remaining
                time_remaining -= clock.tick(60)

                # Check if time is up
                if time_remaining <= 0:
                    level_running = False
                    # Display "Level Reset" message
                    # Display "Play Again" and "Quit" options
                    play_again_text = self.font.render("Play Again", True, (255, 255, 255))
                    quit_text = self.font.render("Quit", True, (255, 255, 255))
                    self.game_window.blit(play_again_text, (self.WINDOW_WIDTH // 2 - play_again_text.get_width() // 2, self.WINDOW_HEIGHT // 2 - play_again_text.get_height() // 2))
                    self.game_window.blit(quit_text, (self.WINDOW_WIDTH // 2 - quit_text.get_width() // 2, self.WINDOW_HEIGHT // 2 + quit_text.get_height() // 2))
                    pygame.display.update()

                    # Wait for player's choice
                    waiting = True
                    while waiting:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                waiting = False
                                running = False
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = pygame.mouse.get_pos()
                                if play_again_text.get_rect(center=(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2 - play_again_text.get_height() // 2)).collidepoint(mouse_pos):
                                    waiting = False
                                    self.current_level_index = 0
                                    self.score = 0
                                elif quit_text.get_rect(center=(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2 + quit_text.get_height() // 2)).collidepoint(mouse_pos):
                                    waiting = False
                                    running = False

                    # Reset the current level to 1 if time is up
                    self.current_level_index = 0
                    self.score = 0
                    input_word = ""

        # End of game loop
        final_score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        self.game_window.blit(final_score_text, (self.WINDOW_WIDTH // 2 - final_score_text.get_width() // 2, self.WINDOW_HEIGHT // 2 - final_score_text.get_height() // 2))
        pygame.display.update()

        # Wait for a few seconds before quitting
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

# Create an instance of the game and run it
game = JumbleWordGame()
game.run()
