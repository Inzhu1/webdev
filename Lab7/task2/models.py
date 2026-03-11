class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self._health_status = "Healthy"
        self.__id = hash(self.name + species)
    
    def eat(self, food):
        return f"{self.name} the {self.species} is eating {food}."
    
    def sleep(self):
        return f"{self.name} is sleeping. Zzz..."
    
    def speak(self):
        return f"{self.name} makes a generic animal sound."
    
    def get_health_status(self):
        return f"{self.name}'s health status: {self._health_status}"
    
    def set_health_status(self, status):
        valid_statuses = ["Healthy", "Sick", "Under Observation", "Recovering"]
        if status in valid_statuses:
            self._health_status = status
        else:
            print(f"Invalid health status. Choose from: {valid_statuses}")
    
    def __str__(self):
        return f"{self.name} ({self.species}), Age: {self.age} years"


class Dog(Animal):
    def __init__(self, name, age, breed, is_trained=False):
        super().__init__(name, age, species="Dog")
        self.breed = breed
        self.is_trained = is_trained
    
    def speak(self):
        return f"{self.name} barks: Woof! Woof!"
    
    def fetch(self, item):
        if self.is_trained:
            return f"{self.name} fetches the {item}!"
        else:
            return f"{self.name} looks at the {item} but doesn't know what to do."
    
    def __str__(self):
        trained_status = "trained" if self.is_trained else "not trained"
        return f"{super().__str__()}, Breed: {self.breed} ({trained_status})"


class Cat(Animal):
    def __init__(self, name, age, color, is_indoor=True):
        super().__init__(name, age, species="Cat")
        self.color = color
        self.is_indoor = is_indoor
    
    def speak(self):
        return f"{self.name} meows: Meow! Meow!"
    
    def climb(self, surface):
        return f"{self.name} gracefully climbs the {surface}."
    
    def purr(self):
        return f"{self.name} is purring contentedly."
    
    def __str__(self):
        indoor_status = "indoor" if self.is_indoor else "outdoor"
        return f"{super().__str__()}, Color: {self.color} ({indoor_status} cat)"


class Bird(Animal):
    def __init__(self, name, age, wingspan, can_fly=True):
        super().__init__(name, age, species="Bird")
        self.wingspan = wingspan
        self.can_fly = can_fly
    
    def speak(self):
        return f"{self.name} chirps: Tweet! Tweet!"
    
    def fly(self):
        if self.can_fly:
            return f"{self.name} spreads its {self.wingspan}cm wings and takes flight!"
        else:
            return f"{self.name} flaps its wings but cannot fly."
    
    def __str__(self):
        flight_status = "can fly" if self.can_fly else "cannot fly"
        return f"{super().__str__()}, Wingspan: {self.wingspan}cm ({flight_status})"