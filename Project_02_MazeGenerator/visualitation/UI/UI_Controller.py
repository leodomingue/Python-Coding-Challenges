import pygame
from .buttons import Button

class UIController:

    def __init__(self, top_y, width, height, on_generate_maze_function, on_make_dfs_function, on_change_color_function):
        self.rect = pygame.Rect(0, top_y, width, height)
        self.font = pygame.font.Font(None, 24)
        self.button_space_frame = int(width  * 0.33)
        self.button_width = int(width  * 0.25)
        self.button_height = int(height * 0.50)
        
        self.generate_maze_button = Button(position_x_left=0 + 50, position_y_top=top_y + 20, width=self.button_width, height=self.button_height, text="Generate maze", callback=on_generate_maze_function, font=self.font)
        self.generate_path_button = Button(position_x_left=self.button_space_frame *1 + 50 , position_y_top=top_y + 20, width=self.button_width, height=self.button_height, text="Generate path", callback=on_make_dfs_function, font=self.font)
        self.generate_changecolor_button = Button(position_x_left=self.button_space_frame *2 + 50, position_y_top=top_y + 20, width=self.button_width, height=self.button_height, text="Change color", callback=on_change_color_function, font=self.font)

        self.buttons = [self.generate_maze_button, self.generate_path_button, self.generate_changecolor_button]

    def draw(self, display):
        pygame.draw.rect(display, (50, 50, 50), self.rect)  
        for button in self.buttons:
            button.draw(display)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)