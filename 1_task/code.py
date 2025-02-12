class Animal:

    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health

    def feed(self):
        self.health += 1
        return self.health

    def __repr__(self):
        return f"Animal(name={self.name}, age={self.age}, health={self.health})"

class Dog(Animal):

    def __init__(self, name, age, health, breed, activity_level):
        super().__init__(name, age, health)
        self.breed = breed
        self.activity_level = activity_level
    
    def play(self):
        if self.health > self.activity_level:
            self.health = self.health - self.activity_level
            return self.health
        else:
            return "Здоровья недостаточно"



p = Animal('r', 10, 100)
print(p.feed()) 
print(p)        
dog = Dog('r', 10, 100, 'w', 12)
print(dog)
print(dog.play())
print(dog.play())
print(dog.play())