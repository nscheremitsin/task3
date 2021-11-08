from math import sqrt


class Tetrahedron:
    # Initializing tetrahedron
    def __init__(self, density, edge):
        self.density = density
        self.edge = edge

    # Tetrahedron string representation
    def __str__(self):
        return "Regular tetrahedron.        a = {0}.                Volume = {1}.  Density = {2}".format(
            self.edge, self.calculate_volume(), self.density
        )

    # Calculating tetrahedron volume
    def calculate_volume(self):
        return pow(self.edge, 3) * sqrt(2) / 12
