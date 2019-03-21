from .solution import pascals_triangle


def example():
    for row in pascals_triangle(10):
        row = ' '.join(map(str, row))
        print(row.center(100))


if __name__ == '__main__':
    example()
