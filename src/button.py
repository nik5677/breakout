class Button:
    """This class represents a button."""
    def __init__(self, image_normal, image_hover, font, position, text_input, text_color):
        self.image_normal = image_normal
        self.image_hover = image_hover
        self.image = image_normal
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.font = font
        self.text_color = text_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.text_color)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def place(self, screen):
        """Place the button and its text on a screen"""
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        """Return True if mouse position is within button, else False"""
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def hover(self, position):
        """Hover the button if mouse position is within it"""
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = self.image_hover
        else:
            self.image = self.image_normal
