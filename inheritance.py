class car:
    @staticmethod
    def start():
        print("car is starting")

    def stop():
        print("car is stopping")

class electric_car(car):
    def __init__(self, name ):
        self.name=name

ev=electric_car("tesla")
ev.start()
print(ev.name)
