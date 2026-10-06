import random
import pygame
from game.text_box import TextBox

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.play_width = 620
        self.cx=self.play_width//2
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_msg = "Enter a number between 1 and 100"
        self.feedback_color = (220, 220, 220)
        self.game_won = False
        self.max_attempts = 10
        self.game_over = False
        self.min_possible = 1
        self.max_possible = 100
        self.font_range = pygame.font.SysFont(None, 28)
        self.history = []


        self.input_box = TextBox(self.cx - 110, 150, 120, 48)
        self.submit_btn = pygame.Rect(self.cx + 25, 150, 100, 48)

        self.font_title = pygame.font.SysFont(None, 42)
        self.font_medium = pygame.font.SysFont(None, 28)
        self.font_btn = pygame.font.SysFont(None, 26)

    def submit_guess(self):
        if self.game_won or self.game_over:
            return

        text = self.input_box.text.strip()
        if not text:
            self.feedback_msg = "Please enter a number first!"
            self.feedback_color = (255, 200, 60)
            return

        guess = int(text)

        self.attempts += 1
        self.input_box.clear()

        if guess < self.secret_number:
            self.feedback_msg = f"TOO LOW! (Guess was {guess})"
            self.feedback_color = (80, 160, 240)
            self.min_possible = max(self.min_possible, guess + 1)
            self.history.insert(0, (guess, "low"))
        elif guess > self.secret_number:
            self.feedback_msg = f"TOO HIGH! (Guess was {guess})"
            self.feedback_color = (240, 100, 80)
            self.max_possible = min(self.max_possible, guess - 1)
            self.history.insert(0, (guess, "high"))
        else:
            self.feedback_msg = f"CORRECT! Found in {self.attempts} attempts."
            self.feedback_color = (80, 220, 90)
            self.game_won = True

        del self.history[5:]   # keep only the 5 most recent

        if not self.game_won and self.attempts >= self.max_attempts:
            self.game_over = True
            self.feedback_msg = f"GAME OVER! The number was {self.secret_number}"
            self.feedback_color = (240, 100, 80)   

    def reset(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_msg = "Enter a number between 1 and 100"
        self.feedback_color = (220, 220, 220)
        self.game_won = False
        self.min_possible = 1
        self.max_possible = 100
        self.input_box.clear()
        self.history = []
        self.game_over = False

    def _draw_arrow(self, screen, cx, cy, up, color):
        if up:
            points = [(cx, cy - 9), (cx - 8, cy + 7), (cx + 8, cy + 7)]
        else:
            points = [(cx, cy + 9), (cx - 8, cy - 7), (cx + 8, cy - 7)]
        pygame.draw.polygon(screen, color, points)

    def handle_event(self, event):
        self.input_box.handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.submit_guess()
            elif event.key == pygame.K_r and (self.game_won or self.game_over):
                self.reset()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.submit_btn.collidepoint(event.pos):
                self.submit_guess()

    def update(self):
        pass

    def render(self, screen):
        screen.fill((30, 34, 42))

        title_surf = self.font_title.render("Number Guessing Arena", True, (245, 245, 245))
        screen.blit(title_surf, (self.cx - title_surf.get_width() // 2, 35))

        attempts_surf = self.font_medium.render(
            f"Attempts: {self.attempts} / {self.max_attempts}", True, (180, 185, 195)
        )
        screen.blit(attempts_surf, (self.cx - attempts_surf.get_width() // 2, 95))
        self.input_box.render(screen)

        pygame.draw.rect(screen, (50, 150, 80), self.submit_btn, border_radius=6)
        pygame.draw.rect(screen, (220, 220, 220), self.submit_btn, width=2, border_radius=6)
        btn_text = self.font_btn.render("SUBMIT", True, (255, 255, 255))
        screen.blit(
            btn_text,
            (self.submit_btn.centerx - btn_text.get_width() // 2,
             self.submit_btn.centery - btn_text.get_height() // 2),
        )

        feedback_surf = self.font_medium.render(self.feedback_msg, True, self.feedback_color)
        screen.blit(feedback_surf, (self.cx - feedback_surf.get_width() // 2, 235))

        range_surf = self.font_range.render(
            f"Range: {self.min_possible} - {self.max_possible}", True, (180, 185, 195)
        )
        screen.blit(range_surf, (self.cx - range_surf.get_width() // 2, 265))

        if self.game_won:
            restart_surf = self.font_medium.render("Press [R] to Start a New Game", True, (255, 220, 80))
            screen.blit(restart_surf, (self.cx - restart_surf.get_width() // 2, 295))

        # --- History panel (x 630-800) ---
        panel = pygame.Rect(630, 35, 170, 300)
        pygame.draw.rect(screen, (40, 45, 56), panel, border_radius=8)
        pygame.draw.rect(screen, (90, 95, 105), panel, width=2, border_radius=8)

        header = self.font_medium.render("History", True, (245, 245, 245))
        screen.blit(header, (panel.centerx - header.get_width() // 2, panel.y + 14))

        if not self.history:
            empty = self.font_btn.render("No guesses yet", True, (130, 135, 145))
            screen.blit(empty, (panel.centerx - empty.get_width() // 2, panel.y + 70))

        for i, (guess, direction) in enumerate(self.history):
            row_cy = panel.y + 75 + i * 46
            color = (240, 100, 80) if direction == "high" else (80, 160, 240)
            self._draw_arrow(screen, panel.x + 35, row_cy, direction == "high", color)
            num_surf = self.font_medium.render(str(guess), True, color)
            screen.blit(num_surf, (panel.x + 65, row_cy - num_surf.get_height() // 2))
               
        if self.game_over:
            overlay = pygame.Surface((self.play_width, self.height), pygame.SRCALPHA)
            overlay.fill((20, 22, 28, 225))
            screen.blit(overlay, (0, 0))

            over_surf = self.font_title.render("GAME OVER", True, (240, 100, 80))
            screen.blit(over_surf, (self.cx - over_surf.get_width() // 2, 110))

            label_surf = self.font_medium.render("The secret number was", True, (180, 185, 195))
            screen.blit(label_surf, (self.cx - label_surf.get_width() // 2, 170))

            num_surf = self.font_title.render(str(self.secret_number), True, (255, 220, 80))
            screen.blit(num_surf, (self.cx - num_surf.get_width() // 2, 200))

            restart_surf = self.font_medium.render("Press [R] to Start a New Game", True, (245, 245, 245))
            screen.blit(restart_surf, (self.cx - restart_surf.get_width() // 2, 270))