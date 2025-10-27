class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# call the constructor with name and id
student1 = Student("Gina", 22510977)
print(student1.name)
print(student1.id)