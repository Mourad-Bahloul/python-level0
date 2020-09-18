
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

# delete attribute from an object
del p1.age

# print(p1.age) => error: AttributeError: 'Person' object has no attribute 'age'
del p1
# print(p1) => NameError: name 'p1' is not defined