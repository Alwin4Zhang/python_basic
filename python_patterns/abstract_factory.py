# -*- coding: utf-8 -*-
'''
  @CreateTime	:  2022/04/19 21:53:35
  @Author	:  Alwin Zhang
  @Mail	:  zjfeng@homaytech.com
'''

import random
from typing import Type


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Dog(Pet):
    def speak(self) -> None:
        print("woof")

    def __str__(self) -> None:
        return f"Dog<{self.name}>"


class Cat(Pet):
    def speak(self) -> None:
        print("meow")

    def __str__(self) -> str:
        return f"Cat<{self.name}>"


class PetShop:
    """A pet shop"""

    def __init__(self, animal_factory: Type[Pet]) -> None:
        """pet_factory is our abstract factory.  We can set it at will."""
        self.pet_factory = animal_factory

    def buy_pet(self, name: str) -> Pet:
        """Creates and shows a pet using the abstract factory"""
        pet = self.pet_factory(name)
        print(f"Here is your lovely {pet}")
        return pet

# additional factories


def random_animal(name: str) -> Pet:
    # create a random animal
    """Let's be dynamic"""
    return random.choice([Dog, Cat])(name)


def main() -> None:
    # A shop the sells only cats
    cat_shop = PetShop(Cat)
    pet = cat_shop.buy_pet("Lucy")
    pet.speak()

    # A shop that sells random animals
    shop = PetShop(random_animal)
    for name in ["Max", "Jack", "Buddy"]:
        pet = shop.buy_pet(name)
        pet.speak()
        print("=" * 20)


if __name__ == '__main__':
    # random.seed(1234)
    # import doctest
    # doctest.testmod()
    main()
