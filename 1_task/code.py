class Animal:

    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health

    def feed(self, health_up):
        self.health += health_up

    def __repr__(self):
        attributes = vars(self)
        return f"{self.__class__.__name__}({', '.join(f'{key}={value}' for key, value in attributes.items())})"

class Dog(Animal):

    def __init__(self, name, age, health, breed, activity_level):
        super().__init__(name, age, health)
        self.breed = breed
        self.activity_level = activity_level
    
    def play(self):
        if self.health > self.activity_level:
            self.health = self.health - self.activity_level

class Cat(Animal):

    def __init__(self, name, age, health, color, favorite_toy):
        super().__init__(name, age, health)
        self.color = color
        self.favorite_toy = favorite_toy

    def sleep(self):
        self.health = 100

class Fish(Animal):

    def __init__(self, name, age, health, species, size):
        super().__init__(name, age, health)
        self.species = species
        self.size = size

    def swim(self):
        if self.health < 97:
            self.health += 3
        elif self.health > 97 and self.health < 100:
            self.health = 100
class ZooShop:

    def __init__(self):
        self.animal_all = []
    
    def add_animal(self, animal):
        self.animal_all.append(animal)
    
    def remove_animal(self, animal):
        if animal in self.animal_all:
            self.animal_all.remove(animal)

    def __repr__(self):
        return '\n'.join(str(animal) for animal in self.animal_all)
    
    def __len__(self):
        return len(self.animal_all)


dog = Dog("Rex", 3, 100, "German Shepherd", 10)
cat = Cat("Barsik", 2, 90, "black", "mouse")
fish = Fish("Goldie", 1, 80, "goldfish", "small")
loh = Animal('r', 1, 1)
zoo_shop = ZooShop()
zoo_shop.add_animal(dog)
zoo_shop.add_animal(loh)
zoo_shop.add_animal(cat)
zoo_shop.add_animal(fish)
print(zoo_shop)
# Должен вывести информацию обо всех животных
zoo_shop.remove_animal(cat)
print(len(zoo_shop))
# Должен вернуть 2, так как осталось два животных