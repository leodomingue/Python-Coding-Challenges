import random
import math
from .star import Star


def generate_stars_random(width,height, radius):

    #Circunference Center
    center_x = width // 2
    center_y = height // 2

    #Random Angle
    angle = random.uniform(0, 2 * math.pi)

    #Position In The Circunference
    x = center_x + math.cos(angle) * radius
    y = center_y + math.sin(angle) * radius



    velocity = random.uniform(3,7)
    velocity_x = math.cos(angle) *velocity
    velocity_y = math.sin(angle) *velocity

    return Star(x,y,velocity_x,velocity_y)