class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Машина едет по дороге."

class Boat(Vehicle):
    def move(self):
        return "Лодка плывёт по воде."

class Plane(Vehicle):
    def move(self):
        return "Самолёт летит в небе."


transport = [Car(), Boat(), Plane()]

for t in transport:
    print(t.move())