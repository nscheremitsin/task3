import sys
from container import Container
import time

# Checking args validity
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("""
            Incorrect command line!
            Waited:
            \tpython main -f <input_file> <output_file_1> <output_file_2>
            Or:
            \tpython main -n <number> <output_file_1> <output_file_2>
            """)
        exit()

    # start = time.time()

    output_file_one = sys.argv[3]
    output_file_two = sys.argv[4]

    container = Container()

    # Populating container with 1 of 2 methods
    if sys.argv[1] == '-f':
        input_file = sys.argv[2]
        container.input(input_file)
    elif sys.argv[1] == '-n':
        amount = int(sys.argv[2])
        container.randomize(amount)

    # Outputting populated container in file 1
    container.output(
        output_file_one,
        "Container has {0} elements:".format(
            container.length()
        )
    )
    # Outputting result of calculations in file 2 after sorting
    container.sort()
    container.output(
        output_file_two,
        "Container has {0} elements after sorting in the following order (average volume: {1})".format(
            container.length(),
            container.calculate_average_volume()
        )
    )

    # print(time.time() - start)
