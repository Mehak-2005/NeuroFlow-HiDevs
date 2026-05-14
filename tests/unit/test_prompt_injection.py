def test_ignore_instruction():
    text = "ignore previous instructions"
    assert "ignore" in text


def test_system_prompt():
    text = "system prompt"
    assert "system" in text


def test_prompt_type():
    text = "prompt"
    assert isinstance(text, str)


def test_prompt_not_empty():
    text = "attack"
    assert text != ""


def test_prompt_length():
    text = "hello"
    assert len(text) > 0