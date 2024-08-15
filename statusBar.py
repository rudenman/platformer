class StatusBar:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

        self.background = None
        self.background_rect = None

        self.current_level = None
        self.current_level_rect = None

        self.current_number_of_lives = None
        self.current_number_of_lives_rect = None

    def update_values(self, current_level, lives):
        self.current_level = self.font.render(f" Уровень: {current_level}", False, [203, 203, 203])
        self.current_level_rect = self.current_level.get_rect(topleft=(0, 0))

        self.current_number_of_lives = self.font.render(f"Осталось жизней: {lives}", False, [203, 203, 203])
        self.current_number_of_lives_rect = self.current_number_of_lives.get_rect(
            topleft=(self.current_level_rect.right + 50, 0))

    def draw(self):
        self.screen.blit(self.current_level, self.current_level_rect)
        self.screen.blit(self.current_number_of_lives, self.current_number_of_lives_rect)

    def update(self, current_level, lives):
        self.update_values(current_level, lives)
        self.draw()
