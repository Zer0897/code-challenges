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

