from pascals_triangle.solution import pascals_triangle


def test_basic():
    basic = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1]
    ]
    assert pascals_triangle(len(basic)-1) == basic


def test_check_sum():
    for i, li in enumerate(pascals_triangle(100)):
        assert sum(li) == 2 ** i
