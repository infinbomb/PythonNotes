num1 = int(input("Enter first digit: "))
sign = input("Enter a sign: ")
num2 = int(input("Enter second digit: "))

def eq(num1, sign, num2):
    if sign == "/":
        print(num1/num2)
    elif sign == "+":
        print(num1+num2)
    elif sign == "-":
        print(num1-num2)
    else:
        print(num1*num2)

eq(num1, sign, num2)

"""
This is a
multiline comment
"""