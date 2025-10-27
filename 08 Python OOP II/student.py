class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(self.name,self.id)