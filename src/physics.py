# Use for Physics Functions
import random
from CONSTANTS import *

class Ball:
    def __init__(self, x, y):
        self.x = random.randint(0, x)
        self.y = random.randint(0, y)

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.radius = random.randint(10,20)


class Square:
    def __init__(self, x, y):
        self.x = random.randint(0, x)
        self.y = random.randint(0, y)

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.radius = random.randint(10,20)