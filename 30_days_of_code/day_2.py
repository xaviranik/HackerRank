meal_cost = float(input())
tip = int(input())/100
tax = int(input())/100

print(round(meal_cost + (meal_cost * tip) + (meal_cost * tax)))

