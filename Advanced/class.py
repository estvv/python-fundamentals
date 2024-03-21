class Person:
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
    def __str__(self):
        return f"{self.name}, {self.age}, {self.size}"
    def check_size(self):
        print(self.name, "fait", self.size,"centimètres.")


p1 = Person("John", 36, 180)
print(p1.name)
print(p1.age)
print(p1)
p1.check_size()