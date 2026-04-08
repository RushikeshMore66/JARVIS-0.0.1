from brain.llm import route_llm


def test_route_llm_default_local():
    assert route_llm("say hello") == "local"


def test_route_llm_cloud_for_web():
    assert route_llm("search the web for latest AI news") == "cloud"
