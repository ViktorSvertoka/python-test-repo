greeting = "Hello from Python"
greeting_letters = list(greeting)

print(greeting_letters)


my_dict = {"a": 10, "b": True}
my_dict_keys = list(my_dict)

print(my_dict_keys)


ratings = [2.5, 5.0, 4.3, 3.7]

print(min(ratings))
print(max(ratings))
print(sum(ratings))

print(sum(ratings) / len(ratings))


my_ratings = [2.5, 5.0]

other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings

print(all_ratings)

first_two_all_ratings = all_ratings[:2]

print(first_two_all_ratings)
