from .generator import generate_stars_random
import random


class StarField:
    def __init__(self, width, height, star_count):
        self.width = width
        self.height = height
        self.stars = [generate_stars_random(width, height, random.randint(20, 200)) for _ in range(star_count)]

    def update_and_draw(self, display):
        for star in self.stars:
            star.update(self.width, self.height)
            star.draw(display)