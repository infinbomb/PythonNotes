def func(x):
    return x+1
# or
func2 = lambda x: x+1
# name = lambda parameter: value being returned
# must fit on one line

print(func(1))
print(func2(1))
print("I")

# 1 parameter
def func3(x):
    func4 = lambda x: x+1
    # lambda function = lambda parameter: value being returned
    return func4(x) + 5
print(func3(1))

# You can have multiple parameters
func5 = lambda x, y: x + y
print(func5(1, 2))

# optional parameter
func6 = lambda x, y = 1: x + y
print(func6(1))

