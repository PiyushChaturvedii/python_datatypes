# Multiple Inheritance
# Multilevel Inheritance

# BASE CLASS
# feature 1

# DERIVED CLASS 1
# Features of base class
# + feature2

# derived class 2
# feature of base class
# + derive class 1
# + feature 3

# Grand father
# father
# child


#base class
class person:
    def display(self):
        print("hello, this is class person")
# derived class 1
class employee(person):
    def printing(self):
        print("hello, this is derived class employee")
# derived class 2
class programmer(employee):
    def show(self):
        print("hello , this is another derived class programmer.")

p1= programmer()
p1.show()
p1.printing()
p1.display()


# Multiple Inheritance
# base class 1            base class 2

    # derived class

    # Father              Mother
    #         child

# land        water
#     Frog


class land_animal:
    def printing(self):
        print("This animal lives on land")

class water_animal:
    def display(self):
        print("this animal lives in water")

class frog(land_animal, water_animal):
    pass

f1=frog()
f1.printing()
f1.display()