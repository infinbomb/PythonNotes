import randommodule as m
from randommodule import myList
import platform

m.add_one(1)
# use this format when calling functions in a module

num1 = 10
num2 = m.x(num1)
print(num2)

for num in myList:
    print(num)
    
all_variables = dir(platform)
print(all_variables)