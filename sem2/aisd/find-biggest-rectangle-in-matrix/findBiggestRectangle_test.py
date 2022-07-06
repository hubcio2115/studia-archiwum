from findBiggestRectangle import findBiggestRectangle


def test_findBiggestRectangle() -> None:
    assert findBiggestRectangle([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0

    assert findBiggestRectangle([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                                1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 25

    assert findBiggestRectangle([]) == 0

    assert findBiggestRectangle(
        [[1, 0, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1]]) == 12

    assert findBiggestRectangle(
        [[1, 0, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1]]) == 6
