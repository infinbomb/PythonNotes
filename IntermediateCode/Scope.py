def myFunction():
    x = 300
    print(x)
    
# print(x) 
# X cannot be accessed outside the function
myFunction()

#However it can be accessed in the function
def nestedFunction():
    x = ["a", "b", "c", "d", "e", "f"]
    for num in x:
        print(num)
    for a in range(0, len(x)):
        print(x[a])  
    
    def func():
        # No need to pass in x list
        for a in range(0, len(x), 2):
            print(x[a])
            
    func()
  
nestedFunction()

# Functions and outside code with same variables will be treated seperately
def someFunc():
    x = 2
    print(x)

someFunc()
x = 3
print(x)

x = lambda a, b, c: a * b // c
print(x(1, 6, 3))
# Here, "x" is a lambda function, so it can have the same name

# If you want to use a variable outside scope, use keyword "global"
def anotherFunc():
    global a
    a = 1
    # You must put global before devlaring the variable
    
anotherFunc()
print(a + 10)