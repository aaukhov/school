import z1

def test_passtest_1234():
    assert z1.passtest('1234') == False

def test_passtest_password():
    assert z1.passtest('Password') == False

def test_passtest_Dom():
    assert z1.passtest('Dom') == False

def test_passtest_poiuytrewq():
    assert z1.passtest('poiuytrewq') == False

def test_passtest_STuyNg29y():
    assert z1.passtest('STuyNg29y') == True