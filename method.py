class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def show(self):
        return self.name

s1=student("devidas", 25)
s1.display()

s2=student("sachin", 30)
print("name:", s2.show())