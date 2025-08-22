from app.mvc_vista import Vista

def test_vista():
    assert Vista().main() == "OK"