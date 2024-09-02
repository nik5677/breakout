import pygame


class Resources:
    """This class is used to load, store and change game resources (images, sounds, fonts...)"""
    def __init__(self, theme='default'):
        """Initialize resources"""
        self.brick_color_list = ['pink', 'purple', 'blue', 'cyan', 'green', 'yellow', 'orange', 'red']
        self.brick_list = {}

        try:
            self.background = pygame.image.load(f"resources/themes/{theme}/background.png")
        except FileNotFoundError:
            self.background = pygame.image.load(f"resources/themes/default/background.png")

        try:
            self.logo = pygame.image.load(f"resources/themes/{theme}/logo.png").convert_alpha()
        except FileNotFoundError:
            self.logo = pygame.image.load(f"resources/themes/default/logo.png").convert_alpha()

        try:
            self.paddle = pygame.image.load(f"resources/themes/{theme}/paddle.png").convert_alpha()
        except FileNotFoundError:
            self.paddle = pygame.image.load(f"resources/themes/default/paddle.png").convert_alpha()

        try:
            self.ball = pygame.image.load(f"resources/themes/{theme}/ball.png").convert_alpha()
        except FileNotFoundError:
            self.ball = pygame.image.load(f"resources/themes/default/ball.png").convert_alpha()

        try:
            self.normal_button = pygame.image.load(f"resources/themes/{theme}/normal_button.png").convert_alpha()
        except FileNotFoundError:
            self.normal_button = pygame.image.load(f"resources/themes/default/normal_button.png").convert_alpha()

        try:
            self.hover_button = pygame.image.load(f"resources/themes/{theme}/hover_button.png").convert_alpha()
        except FileNotFoundError:
            self.hover_button = pygame.image.load(f"resources/themes/default/hover_button.png").convert_alpha()

        for color in self.brick_color_list:
            try:
                self.brick_list[color] = pygame.image.load(f"resources/themes/{theme}/bricks/brick_{color}.png").convert_alpha()
            except FileNotFoundError:
                self.brick_list[color] = pygame.image.load(f"resources/themes/default/bricks/brick_{color}.png").convert_alpha()

        try:
            self.win_sound = pygame.mixer.Sound(f"resources/themes/{theme}/sounds/win.ogg")
        except FileNotFoundError:
            self.win_sound = pygame.mixer.Sound(f"resources/themes/default/sounds/win.ogg")

        try:
            self.lose_sound = pygame.mixer.Sound(f"resources/themes/{theme}/sounds/lose.ogg")
        except FileNotFoundError:
            self.lose_sound = pygame.mixer.Sound(f"resources/themes/default/sounds/lose.ogg")

        try:
            self.bounce_sound = pygame.mixer.Sound(f"resources/themes/{theme}/sounds/bounce.ogg")
        except FileNotFoundError:
            self.bounce_sound = pygame.mixer.Sound(f"resources/themes/default/sounds/bounce.ogg")

        try:
            self.button_font = pygame.font.Font(f"resources/themes/{theme}/font.ttf", 34)
            self.score_font = pygame.font.Font(f"resources/themes/{theme}/font.ttf", 24)
            self.header_font = pygame.font.Font(f"resources/themes/{theme}/font.ttf", 45)
        except FileNotFoundError:
            self.button_font = pygame.font.Font(f"resources/themes/default/font.ttf", 34)
            self.score_font = pygame.font.Font(f"resources/themes/default/font.ttf", 24)
            self.header_font = pygame.font.Font(f"resources/themes/default/font.ttf", 45)

        try:
            with open(f"resources/themes/{theme}/text_color.txt") as f_in:
                for line in f_in:
                    if len(line.split()) == 0:
                        continue
                    self.text_color = line
        except FileNotFoundError:
            with open(f"resources/themes/default/text_color.txt") as f_in:
                for line in f_in:
                    if len(line.split()) == 0:
                        continue
                    self.text_color = line

    def change_theme(self, new_theme):
        """Change resources' theme"""
        try:
            self.background = pygame.image.load(f"resources/themes/{new_theme}/background.png")
        except FileNotFoundError:
            self.background = pygame.image.load(f"resources/themes/default/background.png")

        try:
            self.logo = pygame.image.load(f"resources/themes/{new_theme}/logo.png").convert_alpha()
        except FileNotFoundError:
            self.logo = pygame.image.load(f"resources/themes/default/logo.png").convert_alpha()

        try:
            self.paddle = pygame.image.load(f"resources/themes/{new_theme}/paddle.png").convert_alpha()
        except FileNotFoundError:
            self.paddle = pygame.image.load(f"resources/themes/default/paddle.png").convert_alpha()

        try:
            self.ball = pygame.image.load(f"resources/themes/{new_theme}/ball.png").convert_alpha()
        except FileNotFoundError:
            self.ball = pygame.image.load(f"resources/themes/default/ball.png").convert_alpha()

        try:
            self.normal_button = pygame.image.load(f"resources/themes/{new_theme}/normal_button.png").convert_alpha()
        except FileNotFoundError:
            self.normal_button = pygame.image.load(f"resources/themes/default/normal_button.png").convert_alpha()

        try:
            self.hover_button = pygame.image.load(f"resources/themes/{new_theme}/hover_button.png").convert_alpha()
        except FileNotFoundError:
            self.hover_button = pygame.image.load(f"resources/themes/default/hover_button.png").convert_alpha()

        for color in self.brick_color_list:
            try:
                self.brick_list[color] = pygame.image.load(
                    f"resources/themes/{new_theme}/bricks/brick_{color}.png").convert_alpha()
            except FileNotFoundError:
                self.brick_list[color] = pygame.image.load(
                    f"resources/themes/default/bricks/brick_{color}.png").convert_alpha()

        try:
            self.win_sound = pygame.mixer.Sound(f"resources/themes/{new_theme}/sounds/win.ogg")
        except FileNotFoundError:
            self.win_sound = pygame.mixer.Sound(f"resources/themes/default/sounds/win.ogg")

        try:
            self.lose_sound = pygame.mixer.Sound(f"resources/themes/{new_theme}/sounds/lose.ogg")
        except FileNotFoundError:
            self.lose_sound = pygame.mixer.Sound(f"resources/themes/default/sounds/lose.ogg")

        try:
            self.bounce_sound = pygame.mixer.Sound(f"resources/themes/{new_theme}/sounds/bounce.ogg")
        except FileNotFoundError:
            self.bounce_sound = pygame.mixer.Sound(f"resources/themes/default/sounds/bounce.ogg")

        try:
            self.button_font = pygame.font.Font(f"resources/themes/{new_theme}/font.ttf", 34)
            self.score_font = pygame.font.Font(f"resources/themes/{new_theme}/font.ttf", 24)
            self.header_font = pygame.font.Font(f"resources/themes/{new_theme}/font.ttf", 45)
        except FileNotFoundError:
            self.button_font = pygame.font.Font(f"resources/themes/default/font.ttf", 34)
            self.score_font = pygame.font.Font(f"resources/themes/default/font.ttf", 24)
            self.header_font = pygame.font.Font(f"resources/themes/default/font.ttf", 45)

        try:
            with open(f"resources/themes/{new_theme}/text_color.txt") as f_in:
                for line in f_in:
                    if len(line.split()) == 0:
                        continue
                    self.text_color = line
        except FileNotFoundError:
            with open(f"resources/themes/default/text_color.txt") as f_in:
                for line in f_in:
                    if len(line.split()) == 0:
                        continue
                    self.text_color = line
