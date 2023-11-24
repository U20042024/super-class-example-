#super_class
class person() :
    def __init__(self,nm,ag) :
        self.name = nm 
        self.age = ag

#subclass1
class student(person) :
    def __init__(self, nm, ag,mrk):
        person.__init__(self,nm,ag)
        self.mark = mrk

#subclass2
class teacher(person) :
    def __init__(self, nm, ag,sal):
        person.__init__(self,nm,ag)
        self.salary = sal

#making_first_object
std1 = student("Reda",19,17.06)
print("the student's name is :", std1.name)
print("the student's age is :",std1.age)
print("the student's mark is :",std1.mark)

#making_second_object
tea1 = teacher("ahmad",31,10000)
print("the teacher's name is :",tea1.name)
print("the teacher's age is :", tea1.age)
print("the teacher's salary is :", tea1.salary)
