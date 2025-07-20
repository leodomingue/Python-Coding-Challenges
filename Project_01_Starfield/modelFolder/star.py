import random
import pygame

class Star:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.initial_x = x
        self.initial_y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.trail_array = []
        self.trail_width = random.randint(2, 5)
        self.star_size =  self.trail_width

    def add_to_trail(self):
        self.trail_array.append((self.x,self.y))

    def update_position(self):
        self.add_to_trail()
        self.x += self.velocity_x
        self.y += self.velocity_y

    def get_40th_last_trail_point_or_first(self):
        if len(self.trail_array) <= 19:
            return self.trail_array[0]
        else:
            return self.trail_array[-19]
        
    def get_last_trail_point(self):
        return self.trail_array[-1]
    
    def retrive_trail_width(self):
        return self.trail_width
    
    def retrive_star_size(self):
        return self.star_size
    
    def retrive_star_position(self):
        return (self.x,self.y)
    
    def regenerate_star_if_not_in_window(self, width, height):
       if (self.get_40th_last_trail_point_or_first()[0] < 0 or self.get_40th_last_trail_point_or_first()[0] > width or self.get_40th_last_trail_point_or_first()[1] < 0 or self.get_40th_last_trail_point_or_first()[1] > height):
            self.x = self.initial_x
            self.y = self.initial_y
            self.trail_array = []

    def draw_star(self, display):
        pygame.draw.circle(display, (255,255,255), self.retrive_star_position(), self.star_size)

    def draw_star_trail(self, display):
        if len(self.trail_array) >= 1:
            pygame.draw.line(display, (255,255,255), self.get_40th_last_trail_point_or_first(), self.get_last_trail_point(), 
                        self.retrive_trail_width())


    def draw(self, display):
        self.draw_star_trail(display)
        self.draw_star(display)

    def update(self, width, height):
        self.update_position()
        self.regenerate_star_if_not_in_window(width, height)


    






