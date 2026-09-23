class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative\nHeight update rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm")

    def set_age(self, value) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative\nAge update rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days\n")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, age, height)
        self.color = color
    def show(self):
        super().show()
        print(f" Color: {self.color}")
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter
    def show(self):
          super().show()
    def produce_shade(self):
        print(f"{self.name} now produces a shade of {40 * trunk_diameter}cm long and {trunk_diameter}cm wide")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, rate):
        super().grow(rate)
        self.nutritional_value += 10

    def age(self):
        super().age()
        self.nutritional_value += 10

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")
