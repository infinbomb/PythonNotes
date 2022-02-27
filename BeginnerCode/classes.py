class MyClass():
    def __init__(self, numStudents, grade):
        self.numStudents = numStudents
        self.grade = grade
    
    def class_description(self):
        print("Your class has " + str(self.numStudents) + " students")
        
class Person(MyClass):
    pass 

class Senior(MyClass):
    def __init__(self, name, college): 
    # this will override Parent class initialization
        self.name = name
        self.age = 12
        self.college = college
        
        
class JuniorClass(MyClass):
    def __init__(self, numStudents, grade):
        super().__init__(numStudents, grade)
        self.senioritis = False # adds another attribute to the constructor
       
class SophmoreClass(MyClass):
    def __init__(self, numStudents, grade, senioritis):
        super().__init__(numStudents, grade)
        self.senioritis = senioritis # adds a given attribute to the constructor
    
    def class_description(self):
        if self.senioritis:
            print("This Class has senioritis")
        else:
            print("This Class is working hard :)")
        super().class_description()
       
p6 = SophmoreClass(100, 10, False)
p6.class_description()
 
p5 = JuniorClass(6, 11)    
p5.class_description()
   
p1 = MyClass(5, 12)
p1.class_description()

p2 = Person(4, 11)
print(p2.grade)

p3 = Senior("Charles", "Cornell University")
print(p3.college)