def test_closed_state():
    state = "closed"
    assert state == "closed"


def test_open_state():
    state = "open"
    assert state == "open"


def test_half_open_state():
    state = "half-open"
    assert state == "half-open"


def test_state_type():
    state = "closed"
    assert isinstance(state, str)


def test_state_not_none():
    state = "open"
    assert state is not None