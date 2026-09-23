class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

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
        self.set_height(round(self.get_height() + rate, 2))

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def show(self) -> None:
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False  # état interne : a-t-elle déjà fleuri ?

    def show(self) -> None:
        super().show()  # IMPORTANT : super() suivi de () sinon ça ne marche pas
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    # ATTENTION : show() et produce_shade() doivent être au même niveau
    # d'indentation que __init__, pas imbriqués DEDANS __init__ !
    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height()}cm long and {self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0  # un seul nom, ni deux (attribut + méthode)

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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()
