class Staff:
    def __init__(self, name, id, position):
        self.name = name
        self.id = id
        self.position = position

    def print_info(self):
        print(self.name,self.id, self.position)