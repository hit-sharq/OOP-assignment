# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass for Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Subclass for Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"

# Function to demonstrate the move action
def demonstrate_movement(vehicle):
    print(vehicle.move())

# Example usage
if __name__ == "__main__":
    my_car = Car()
    my_plane = Plane()
    my_bicycle = Bicycle()

    demonstrate_movement(my_car)       # Output: Driving 🚗
    demonstrate_movement(my_plane)     # Output: Flying ✈️
    demonstrate_movement(my_bicycle)   # Output: Pedaling 🚲