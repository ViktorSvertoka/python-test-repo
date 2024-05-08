class Duck:
    def quack(self):
        print("Quack, quack!")


class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")


def make_it_quack(duck):
    duck.quack()


duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)
