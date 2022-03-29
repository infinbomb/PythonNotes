import datetime
import math

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

# You can use the datetime constructor
today = datetime.datetime(2022, 3, 9)
print(today)
print(today.strftime("%A"))
print(today.strftime("%c"))
print(today.strftime("%x"))


findmin = min(1, 2, 3)
findmax = max(1, 2, 3)
# You can use min and max to find the minadn max
# in an iterable
print(findmin)
print(findmax)


findabs = abs(-7.25)
print(findabs)

power = pow(2, 3)
print(power)

squareroot = int(math.sqrt(64))
print(squareroot)

useceiling = math.ceil(1.2)
usefloor = math.floor(1.7)
print("Rounding up: " + str(useceiling))
print("Rounding down: " + str(usefloor))

pie = math.pi
print(pie)