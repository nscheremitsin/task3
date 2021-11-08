from ball import Ball
from tetrahedron import Tetrahedron
from parallelepiped import Parallelepiped
from random import randint


class Container:
    def __init__(self):
        self.shapes = []

    def length(self):
        return len(self.shapes)

    # Read parameters from file
    def input(self, file_name):
        with open(file_name, 'r') as file:
            file.readline()
            for line in file:
                args = line.split()
                args = [int(args[i]) if i != 1 else float(args[i]) for i in range(len(args))]
                self.append_shape(args)

    # Randomizing parameters
    def randomize(self, amount):
        for i in range(amount):
            args = [
                randint(1, 3),
                randint(1, 9) + randint(1, 999) / 1000
            ]
            for j in range(3):
                args.append(randint(1, 9))
            self.append_shape(args)

    # Appending new shape in storage
    def append_shape(self, args):
        key = args[0]
        density = args[1]
        arg = args[2]
        if key == 1:
            self.shapes.append(Ball(density, arg))
        elif key == 2:
            self.shapes.append(Tetrahedron(density, arg))
        elif key == 3:
            self.shapes.append(Parallelepiped(density, arg, args[3], args[4]))

    # Outputting parameters in file
    def output(self, file_name, message):
        with open(file_name, 'w') as file:
            file.write(message + "\n")
            for shape in self.shapes:
                file.write(str(shape) + "\n")

    # Calculating average shapes volume
    def calculate_average_volume(self):
        volume = 0
        for shape in self.shapes:
            volume += shape.calculate_volume()
        return volume / len(self.shapes)

    # Sorting storage depending on average volume
    def sort(self):
        average_volume = self.calculate_average_volume()
        self.shapes.sort(key=lambda x: x.calculate_volume() < average_volume)
