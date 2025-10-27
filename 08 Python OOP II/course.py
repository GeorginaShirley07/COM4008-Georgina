class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        
    def print_info(self):
        print(self.name, self.code)