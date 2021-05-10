"""
There is a Person whose characteristics are:
1. Name
2. Age
3. Availability of money
4. Having your own home
Human can:
1. Provide information about yourself
2. Make money
3. Buy a house
There is also a House, the properties of which include:
1. Area
2. Cost
For Home you can:
1. Apply a purchase discount
e.g.: There is also a Small Typical House with a required area of 40m2.
*Realtor:
1. Name
2. Houses
3. Discount that he/she can give you.
*There is only one realtor who handles small houses you wanna buy. (Singleton)
Realtor is only one in your city and can:
1. Provide information about all the Houses
2. Give a discount
3. Steal your money with 10% chance
"""

from abc import ABC, abstractmethod
import random


class Person(ABC):
    def __init__(self, name: str, age: int, money: (int, float), house: list = []):
        self.name = name
        self.age = age
        self.own_money = money
        self.own_home = house

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError


class Human(Person, ABC):
    def __init__(self, name: str, age: int, money: (int, float), house: list = []):
        super().__init__(name, age, money, house)
        self.salary = random.randint(5000, 15000)

    def info(self):
        print(f'Hi! My name is {self.name}, and I am {self.age} years old.')

    def make_money(self):
        self.own_money += self.salary

    def buy_house(self, house):
        if house.area >= 150:
            print('House is way too big. Maybe you have other one for me?')
        elif house.cost >= self.own_money:
            print(f'{self.name} does not have enough money to purchase this house.')
        else:
            self.own_money -= house.cost
            print(f'Congratulations to {self.name} ! Welcome to your new house!')

        return self.own_home.append(house)


class Building(ABC):
    def __init__(self, area: (float, int), cost: int):
        self.area = area
        self.cost = cost

    @abstractmethod
    def apply_discount(self):
        raise NotImplementedError


class House(Building):
    def __init__(self, area, cost):
        super().__init__(area, cost)

    def apply_discount(self, discount):
        self.cost -= (self.cost * discount)
        return self.cost


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name: str, discount: (float, int), houses: list = []):
        self.name = name
        self.discount = discount
        self.houses = houses

    def info_houses(self):
        if self.houses:
            print(f'Hello! My name is {self.name} and I am your realtor.')
            for house in self.houses:
                print(f' These house on sale: {house}')
        else:
            print('We have not available houses')
        return self.houses

    def give_discount(self):
        return self.discount

    def steal_money(self):
        return random.randrange(0, 100)


if __name__ == '__main__':
    house1 = House(40, 15000)
    house2 = House(165, 60000)
    house3 = House(150, 20000)
    house4 = House(100, 33680)


    realtor = Realtor('Pavlo', 0.20, [house1, house2, house3, house4])
    realtor.info_houses()
    realtor.give_discount()
    realtor.steal_money()

    person = Human('Tanya', 23, 20000)
    person.info()
    person.make_money()
    person.buy_house(house2)
    person.buy_house(house3)
    person.buy_house(house1)