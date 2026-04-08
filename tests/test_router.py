from brain.router import classify_intent, route


def test_classify_intent_vision():
    assert classify_intent("analyze screen") == "vision"


def test_classify_intent_action():
    assert classify_intent("open calculator") == "action"


def test_route_interrupt_falls_back_chat():
    assert route("cancel current task") == "chat"
