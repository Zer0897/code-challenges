def pascals_triangle(number, *, base=1):
    """
    One solution for generating [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) recursively.

    param
        number: int -- Number of rows to build.
        base: int (optional) -- Starting value to build from. Defaults to 1.

    return
        list -- Pascal's triangle.

    example::

    ```
    for row in pascals_triangle(10):
        row = ' '.join(map(str, row))
        print(row.center(100))

    >>>                                          1
                                                1 1
                                               1 2 1
                                              1 3 3 1
                                             1 4 6 4 1
                                           1 5 10 10 5 1
                                          1 6 15 20 15 6 1
                                        1 7 21 35 35 21 7 1
                                       1 8 28 56 70 56 28 8 1
                                    1 9 36 84 126 126 84 36 9 1
                                1 10 45 120 210 252 210 120 45 10 1
    ```
    """
    # For convenience, letting the user enter an integer for
    # base without having to wrap it in []
    if isinstance(base, int):
        base = [base]

    if number == 0:
        return [base]

    new = [l + r for l, r in zip(base, base[1:] + [0])]
    return [base] + pascals_triangle(number - 1, base=[base[0]] + new)
