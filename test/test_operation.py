from src.maths_operation import add , sub

def test_add():
    assert add(2,3) == 5
    assert add(3,3) == 6
    assert add(-2,3) == 1
    
def test_sub():
    assert sub(3,2) == 1
    assert sub(4,2) == 2
    assert sub(-3,2) == -5