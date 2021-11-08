class Parallelepiped:
    # Initializing parallelepiped
    def __init__(self, density, a, b, c):
        self.density = density
        self.edge_a = a
        self.edge_b = b
        self.edge_c = c

    # Parallelepiped string representation
    def __str__(self):
        return "Rectangular parallelepiped. a = {0}, b = {1}, c = {2}.  Volume = {3}.  Density = {4}".format(
            self.edge_a, self.edge_b, self.edge_c, self.calculate_volume(), self.density
        )

    # Calculating parallelepiped volume
    def calculate_volume(self):
        return self.edge_c * self.edge_b * self.edge_a
