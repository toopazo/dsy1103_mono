# from app.mvc_vista import Vista

# def test_vista():
#     assert Vista().main() == "OK"

from app.calculate import function_to_test

def test_vista():
    assert function_to_test(3,4) == 5