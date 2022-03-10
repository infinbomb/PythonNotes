import json

# a syntax for storing and exchanging data
# a text, written with JavaScript object notation
myJSON = '{ "name":"Charles", "age":30, "city":"New York"}'
y = json.loads(myJSON)
# parse x
print(y["age"])

myDic = {
    "name":"Charles",
    "age": 18,
    "city": "New Jersey"
}
y = json.dumps(myDic)
print(y)
# This is a JSON string basically

# Use json dumps function to turn these python objects into 
# strings
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "orange"]))
print(json.dumps(("apple", "bananas")))

