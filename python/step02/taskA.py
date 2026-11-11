# Name: Connor Harrison
# Date: 11/11/26
# Program: Step 2 - Variables and Input
# Description: Works out the pizza party and does the calculation

SLICES_PER_PIZZA = 8
PIZZA_PRICE = 12.99
SLICE_PRICE = 2.25

# Input: the host's name, the number of people, and slices per person
host_name = input("Enter Host's Name: ")
number_people = int(input("Number of People: "))
slices_person = float(input("Slices Per Person: "))

# Processing: total slices of pizza and the cost
total_slices = number_people * slices_person
whole_pizzas = total_slices // SLICES_PER_PIZZA
extra_slices = total_slices % SLICES_PER_PIZZA 
total_cost = whole_pizzas * PIZZA_PRICE + extra_slices * SLICE_PRICE
cost_per_person = total_cost / number_people

# Output: a small report of the pizza party
print("Host Name:", host_name)
print("Number of People:", number_people)
print("Slices per Person", slices_person)
print("=== Pizza Plan for", host_name, "'s Party ===")
print("Slices needed:", total_slices)
print("Whole pizzas:", whole_pizzas)
print("Extra slices:", extra_slices)
print("Total cost: $", total_cost)
print("Cost per person", cost_per_person)
