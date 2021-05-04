"""
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
class Animals:
    Parent class, should have eat, sleep
   class Animal1(Animal):
    Some of the animal with 1-2 extra methods related to this animal
"""


class Animals:
    def eat(self):
        print(f'{self.__class__.__name__} eating')

    def sleep(self):
        print(f'{self.__class__.__name__} sleeping')


class Wolf(Animals):
    def hunt(self):
        print(f'{self.__class__.__name__} catch prey')


class Dog(Animals):
    def bark(self):
        print(f'{self.__class__.__name__} barking')


class Bee(Animals):
    def Bee(self):
        print(f'{self.__class__.__name__} flying')


class Lynx(Animals):
    def running(self):
        print(f'{self.__class__.__name__} pursues the victim')


class Snake(Animals):
    def crawl(self):
        print(f'{self.__class__.__name__} crawling')


wolf = Wolf()
dog = Dog()
bee = Bee()
lynx = Lynx()
snake = Snake()

print('Task 1.1')
wolf.sleep()
lynx.running()
dog.eat()

print(f'wolf is an instance of the Animals class: {isinstance(wolf, Animals)}')
print(f'dog is an instance of the Animals class: {isinstance(dog, Animals)}')
print(f'bee is an instance of the Animals class: {isinstance(bee, Animals)}')
print(f'lynx is an instance of the Animals class: {isinstance(lynx, Animals)}')
print(f'snake is an instance of the Animals class: {isinstance(snake, Animals)}')

"""
 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 create an instance of Centaur class and call the common method of these classes and unique.

 class Human:
    Human class, should have eat, sleep, study, work

 class Centaur(.. , ..):
    Centaur class should be inherited from Human and Animal and has unique method related to it.
"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} eating')

    def sleep(self):
        print(f'{self.name} sleeping')

    def study(self):
        print(f'{self.name} studying')

    def work(self):
        print(f'{self.name} working')


class Centaur(Animals, Human):
    def hunting(self):
        print(f'{self.name} hunting to get supplies')

    def archery(self):
        print(f'{self.name} archery')

    def guard(self):
        print(f'{self.name} guard his lands')


centaur = Centaur('Heron', 49)
print('Task 1.2')
centaur.eat()
centaur.sleep()
centaur.study()
centaur.hunting()
centaur.archery()
centaur.guard()
