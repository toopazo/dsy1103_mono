from app.mvc_vista import Vista

# def test_vista():
#     assert Vista().main() == "OK"

# from app.calculate import function_to_test

def test_vista_1():
    assert Vista().main() == "OK"

def test_vista_2():
    assert Vista().main() == "Not OK"