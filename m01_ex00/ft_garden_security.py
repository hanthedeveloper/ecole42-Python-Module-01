class Plant:
    def __init__(self, _name: str, _height: float, _age: int):
        self._name = _name
        self._height = _height
        self._age = _age
    def set__height(self, value: int) -> str:
        if value < 0:
            print(f"{self._name}: Error, _height can't be negative\n_height update rejected")
        else:
            self._height = value
            print(f"_height updated: {value}cm")
    def set_age(self, value) -> str:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative\nAge update rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days")
    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_age(15)
    print(f"Current state: ", end="")
    rose.show()
    rose.page = 14
    print(f"Current state: ", end="")
    rose.show()