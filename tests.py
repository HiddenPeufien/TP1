from secondMin import secondMin #importing the function to be tested


def test_descending(): # Basic test
    l = [5, 4, 3, 2, 1]
    r = secondMin(l)
    # assert will raise an AssertError if the test is False
    assert r==2 , "descending test"


def test_ascending():
    l = [1, 2, 3, 4, 5]
    r = secondMin(l)
    # assert will raise an AssertError if the test is False
    assert r==2 , "ascending test"

def test_second_min_is_first_element():
    l = [2, 1, 3, 4, 5]
    r = secondMin(l)
    # assert will raise an AssertError if the test is False
    assert r==2 , "second min is first test"    

def test_all_elements_same():
    l = [2, 2, 2, 2, 2]
    r = secondMin(l)
    # assert will raise an AssertError if the test is False
    assert r==None , "second min is last test"


def test_second_min_is_last_element():
    l = [1, 3, 4, 5, 2]
    r = secondMin(l)
    # assert will raise an AssertError if the test is False
    assert r==2 , "second min is last test"

    
def test_size_is_one():
    l = [1]
    r = secondMin(l)
    # assert will raise an AssertError if the test is False
    assert r==None , "list is size 1 test"  

def test_mixed_types():
    try:
        l = [1, "e", "a", 5, 2]
        r = secondMin(l)
        assert False
    except(TypeError):
        assert True , "second min is last test"

def test_is_empty():
    l = []
    r = secondMin(l)
    # assert will raise an AssertError if the test is False
    assert r==None , "list is empty"

def test_contains_float():
    l = [1.2,3.3,4.4,5.4]
    r = secondMin(l)
    # assert will raise an AssertError if the test is False
    assert r==3.3 , "list contains floats test"

def test_contains_negative_numbers():
    l = [-1,2,3,-3]
    r = secondMin(l)
    # assert will raise an AssertError if the test is False
    assert r==-1 , "list contains negative numbers"
    
