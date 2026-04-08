from actions.executor import evaluate_action_safety


def test_action_safety_blocks_dangerous():
    assert evaluate_action_safety("rm -rf /") is False


def test_action_safety_allows_normal():
    assert evaluate_action_safety("open calculator") is True
