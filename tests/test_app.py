from app import index


def test_index():
    assert index() == "Hello, this is dev enviroment, and Github action CICD !"

