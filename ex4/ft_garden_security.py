class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
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

    def set_age(self, value) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative\nAge update rejected")
        else:
            self._age = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", -15.0, -10)
    print("Plant created: ", end="")
    rose.show()
    print()

    new_height = 0.0
    new_age = 0
    rose.set_height(new_height)
    print(f"Height updated: {new_height}cm")
    rose.set_age(new_age)
    print(f"Age updated: {new_age} days\n")

    rose.set_height(-5)
    rose.set_age(-3)

    print("\nCurrent state: ", end="")
    rose.show()