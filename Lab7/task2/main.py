from models import Animal, Dog, Cat, Bird

def main():
    generic_animal = Animal("Generic", 5, "Unknown")
    
    dog1 = Dog("Max", 3, "Golden Retriever", is_trained=True)
    dog2 = Dog("Bella", 2, "Poodle", is_trained=False)
    
    cat1 = Cat("Whiskers", 4, "Orange", is_indoor=True)
    cat2 = Cat("Luna", 1, "Black", is_indoor=False)
    
    bird1 = Bird("Tweety", 2, 25.5, can_fly=True)
    bird2 = Bird("Penguin", 7, 40.0, can_fly=False)
    
    zoo_animals = [generic_animal, dog1, dog2, cat1, cat2, bird1, bird2]
    
    print("=== ZOO ANIMALS ===")
    for animal in zoo_animals:
        print(animal)
    
    print("\n=== ANIMAL SOUNDS ===")
    for animal in zoo_animals:
        print(animal.speak())
    
    print("\n=== UNIQUE ACTIONS ===")
    print(dog1.fetch("ball"))
    print(cat1.climb("tree"))
    print(bird1.fly())
    
    print("\n=== HEALTH STATUS ===")
    dog1.set_health_status("Sick")
    print(dog1.get_health_status())

if __name__ == "__main__":
    main()