# Fundamental features of oop
# Inheritance
# Encapsulation
# Polymorphism

# Inheritance

# base class
# feature 1
# feature 2

# derived class
# feature 1
# feature 2
# feature 3

class animal:
    # def eating(self):
    #     print("eating")

    def __init__(self,name):
        self.name = name


class dog(animal):
    def display(self):
        print(self.name)
    
    # def bark(self):
    #     print("bark")


# tommy = dog()
# tommy.eating()
# tommy.bark()

d = dog("babydog")
d.display()