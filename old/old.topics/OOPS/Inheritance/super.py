class Parent:
    def __init__(self,name):
        print("Parent __init__",name)

class Parent2:
    def __init__(self,name):
        print("Parent2 __init__",name)

class Child(Parent,Parent2):
    def __init__(self):
        print("Child __init__")
        Parent2.__init__(self,'max')
        Parent.__init__(self,'min')

child = Child()
print(Child.__mro__)