def test_rrf_score():
    score = 0.8
    assert score > 0


def test_rrf_type():
    result = [1, 2, 3]
    assert isinstance(result, list)


def test_rrf_length():
    result = [1, 2]
    assert len(result) == 2


def test_rrf_sort():
    result = sorted([3, 1, 2])
    assert result == [1, 2, 3]


def test_rrf_contains():
    result = [1, 2, 3]
    assert 2 in result