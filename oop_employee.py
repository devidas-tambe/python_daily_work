class employee:
    def __init__(self, role, dept, salary):
        self.name = role
        self.age = dept
        self.salary = salary



    def display(self):
        print("Role:", self.name)
        print("Department:", self.age)
        print("Salary:", self.salary)

emp=employee("manager", "sales", 50000)

emp.display()