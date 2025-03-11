# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"
    def honk(self):
        return "HONK HONK!"
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"
def demonstrate_movement(vehicle):
    print(vehicle.move())
if __name__ == "__main__":
    my_car = Car()
    my_plane = Plane()
    my_bicycle = Bicycle()

    demonstrate_movement(my_car)       # Output: Driving 🚗
    demonstrate_movement(my_plane)     # Output: Flying ✈️
    demonstrate_movement(my_bicycle)   # Output: Pedaling 🚲