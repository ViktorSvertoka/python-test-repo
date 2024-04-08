my_cars = ["BMW", "Mercedes"]

# copied_cars = my_cars[:]
copied_cars = my_cars.copy()

copied_cars.append("Audi")

print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']

print(my_cars)  # ['BMW', 'Mercedes']

print(id(my_cars) == id(copied_cars))  # False
