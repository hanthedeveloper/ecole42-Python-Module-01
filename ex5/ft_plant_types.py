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
        super.show()
        print(f" Color: {self.color}")
    def bloom(self):


class Tree(Plant):



class Vegetable:
