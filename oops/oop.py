# Object Class

# Object - collection of data and its  functionality
# class - Blueprint for objects

# example: Object.    : House
# Class: map.

# Instance
# local
# class person:
#     def __init__(self,name):
#         self.name = name
#         name = "john"
#         print(name)

#     def display(self):
#         print("Hello ",self.name)

# person1 = person("atul")
# person1.display()

# person("atul").display()

# Class and Instance  variables

# class student:
#     clg = 'xyz'     #class variable

#     def __init__(myself,rollno,name):
#         myself.rollno = rollno
#         myself.name = name

#     def display(myself):
#         print("student name: ",myself.name)
#         print("student rollnumber: ",myself.rollno)
#         print("college: ",student.clg)

# student1= student("xyz001", "atul")
# student1.display()

# student2= student("xyz056", "john")
# student2.display()

# print(student2.clg)
    

class person:
    def display(self):
        print("hello")

p = person()
p.display()