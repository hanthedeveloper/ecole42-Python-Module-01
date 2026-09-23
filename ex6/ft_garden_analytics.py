class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self._stats = self.Stats()

    @staticmethod
    def check(age: int, year: int) -> int:
        return age > year
    @classmethod
    def create(cls) -> "Plant":
        return cls("Unknown plant", {get_height}cm, {get_age} days old)

    class Stats:
        def __init__(self):
            self._age_count = 0
            self._grow_count = 0
            self._show_count = 0
        def add_grow(self):
            self._grow_count += 1
        def add_age(self):
            self._age_count += 1
        def add_show(self):
            self._show_count += 1


    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self, rate: float = 1.0) -> None:
        self.self.add_grow()
        self.set_height(round(self.get_height() + rate, 2))

    def age(self) -> None:
        self._stats.add_age()
        self.set_age(self.get_age() + 1)

    def show(self) -> None:
        self._stats.add_show()
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True

class Seed(Flower):
     def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.Stats._count_shade = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats._count_shade += 1
        print(f"Tree {self.name} now produces a shade of {self.get_height()}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, rate: float = 1.0) -> None:
        super().grow(rate)
        self.nutritional_value += 10

    def age(self) -> None:
        super().age()
        self.nutritional_value += 10

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

def myFunc(self):
    self.show