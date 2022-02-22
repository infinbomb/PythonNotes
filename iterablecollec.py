print("test")

x = {
    "name":"John",
    "age":21, 
    "age":20 # overrides the previous pair(no duplicates)
}

print(type(x))
# this is a key value pair dictionary
print(x)
print(len(x))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"] # a dict pair can be any type
}

list1 = ["abc", 1, True, "Jig", False]
for i in list1:
    print(i)
    print(type(i))

# tuples, lists, sets, dicationaries are all iterable
# and can be extended to a list
thislist = ["China", "sucks"]
thistuple = ("a", "azz")
thislist.extend(thistuple)
print(thislist)
print(thistuple)

# using the given list, make a new list with only "a"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
print(fruits[-1]) # prints last item
print(fruits[2:5]) # inclusive exclusive range 2 to 5
# newlist.append([x for x in fruits if "a" in x])
# or
newlist = [x for x in fruits if "a" in x]
# expression for item in iterable if condition == true
print(newlist)
# the if can be omitted
ezlist = [x for x in fruits]
upperlist = [x.upper() for x in fruits]
replacelist = [x if x != "banana" else "orange" for x in fruits]

newList = ["Chicken", "Beef", "Pork"]
changelist = [x if x != "Chicken" else "Frog" for x in newList]
print(newList)
print(changelist)