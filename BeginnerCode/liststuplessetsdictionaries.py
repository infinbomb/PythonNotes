#this is a list
myList = ["Charles", "Darren", "Karen", "Karen"]
# Lists allow duplicate items
print(len(myList))

#Lists also allow for different data types
randomList = ["Charles", 18, True]
print(type(randomList))

for item in randomList:
    print(type(item))
    
thislist = list(("apple", "banana", "cherry"))
print(thislist)

#LIST COMPREHENSION
changeList = [x for x in thislist if "a" in x]
print(changeList)

upperList = [x.upper() for x in thislist]
print(upperList)

newList = []