from calculations import salary_calculations

salary = 1000
bonus = 15
salary_with_bonus = salary_calculations.add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015


from calculations.salary_calculations import add_bonus

salary = 1000
bonus = 15
salary_with_bonus = add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015
