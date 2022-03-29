# Errors and Exceptions

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    pass
        
def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small")
    
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)
    