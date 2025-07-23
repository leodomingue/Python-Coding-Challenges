import pygame

class Button:
    def __init__(self, position_x_left, position_y_top, width, height, text, callback, font):
        self.rect = pygame.Rect(position_x_left, position_y_top, width, height)
        self.text = text
        self.callback = callback
        self.font = font
        self.width = width
        self.hovered = False
        self.color_not_hovered = (150, 150, 150)
        self.color_hovered = (200, 200, 200)

    def draw(self, display):
        color = (200, 200, 200) if self.hovered else (150, 150, 150)
        pygame.draw.rect(display, color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        display.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                self.callback()

    def return_width(self):
        return self.width