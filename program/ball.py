from math import pi


class Ball:
    # Initializing ball
    def __init__(self, density, radius):
        self.density = density
        self.radius = radius

    # Ball string representation
    def __str__(self):
        return "Ball.                       r = {0}.                Volume = {1}.  Density = {2}".format(
            self.radius, self.calculate_volume(), self.density
        )

    # Calculating ball volume
    def calculate_volume(self):
        return pi * 4 / 3 * pow(self.radius, 3)
