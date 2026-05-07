class student:
    def __init__(self, name, mark):
        self.name=name
        self.mark=mark

    def avg_get(self):
        sum=0
        for i in self.mark:
            sum = sum+i
            return sum/len(self.mark)
s1=student("Devidas ", [55,87,98])
print("name:",s1.name)
print("average mark:",s1.avg_get())