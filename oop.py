student_1=["Madhav",10]
student_2=["Ramesh",20]
print(f"{student_1[0]} is {student_1[1]} yeare are old")

class student:
    # name="rohit"
    # age=10
    def __init__(self,name,age):
        self.name=name
        self.age=age
std=student("madhav",10)
print(std.name,std.age)

std1=student