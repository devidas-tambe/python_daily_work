class car:
    def __init__(self):
        self.clutch=False
        self.brk=False
        self.steering=False

    def drive(self):
        self.clutch=True
        self.brk=True
        self.steering=True
        print("car is running")
c1=car()
c1.drive()