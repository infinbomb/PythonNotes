class MyClass():
    def __init__(self, numStudents, grade):
        self.numStudents = numStudents
        self.grade = grade
    
    def class_description(self):
        print("Your class has " + str(self.numStudents) + " students")
        
class Person(MyClass):
    pass 

class Senior(MyClass):
    def __init__(self, name, age, college): 
    # this will override Parent class initialization
        self.name = name
        self.age = age
        self.college = college
        
p1 = MyClass(5, 12)
p1.class_description()

p2 = Person(4, 11)
print(p2.grade)

p3 = Senior("Charles", 12, "Cornell University")
print(p3.college)