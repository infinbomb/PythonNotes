import random 

a = random.randint(1, 10) # inclusive
print(a)

a = random.randrange(1, 10) # exclusive
print(a)

a = random.normalvariate(0, 1)
print(a)
# useful in statistics

mylist = list("ABCDEFG")
print(mylist)
a = random.choice(mylist) # picks a random element
print(a)