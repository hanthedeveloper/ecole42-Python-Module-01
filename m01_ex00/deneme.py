#!/usr/bin/env python3
""" dosya acıklaması boyle yazılıyor??? """
def ft_garden_intro() -> None:
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")

print("__name__   :", __name__)
print("__file__   :", __file__)
print("__doc__    :", __doc__)
print("__package__:", repr(__package__))

class Plant:
    name: str
    height: float
    page: int


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    flower = Plant()
    print(f"{flower}")
