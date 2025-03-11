# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I'm {self.name}, the superhero of {self.city}!"

    def use_power(self):
        return f"{self.name} uses their power: {self.power}!"

class Sidekick(Superhero):
    def __init__(self, name, power, city, hero_name):
        super().__init__(name, power, city) 
        self.hero_name = hero_name

    def assist(self):
        return f"{self.name} is assisting {self.hero_name} in battle!"

# Example usage
hero = Superhero("Captain joshua", "super strength", "Metropolis")
sidekick = Sidekick("lee joshua", "agility", "Metropolis", hero.name)

def introduce_hero(superhero):
    print(superhero.introduce())
    print(superhero.use_power())
    if isinstance(superhero, Sidekick):
        print(superhero.assist())

introduce_hero(hero)
introduce_hero(sidekick)