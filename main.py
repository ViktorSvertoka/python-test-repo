class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def make_it_speak(speaker) -> None:
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop


from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str:
        pass


class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
