class Car:

    def__init__(self, color,speed,is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"new car: {self.name} (color {self.color}) police car - {self.is_police}")

    def go(self):
        print(f"{self.name}: car is go")

    def stop(self):
        print(f"{self.name}: car is stop")

    def turn(self, direction):
        print(f"{self.name}: car is turn {'left' if direction == 0 else 'right'}")

    def show_speed(self):
        print(f"{self.name}: car speed - {self.speed}")

class WorkCar(Car):

    def show_speed(self):
        return f"{self.name}: car speed - {self.speed} - match speed"\
            if self.speed > 40 else f"{self.name}: car speed -{self.speed}"

