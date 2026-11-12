# Name: Connor Harrison
# Date: 11/11/26
# Program: Step 2 - Variables and Input
# Description: a program that figures out gas, cost per person, and driving time for a road trip

# Input: the destination, trip distance in miles, the car's miles per gallon, the gas price, and the number of people splitting the cost
destination = input("Destination: ")
miles = float(input("Trip distance (miles): "))
miles_per_gallon = float(input("Car's miles per gallon: "))
gas_price = float(input("Gas price per gallon: "))
people = int(input("Number of people splitting the cost: "))

# Constant
AVERAGE_SPEED = 55

# Processing: the time and cost
gallons = miles / miles_per_gallon
gas_cost = gallons * gas_price
cost_per_person = gas_cost / people
driving_time_mins = int(miles / AVERAGE_SPEED * 60)
hours = driving_time_mins // 60
leftover_minutes = driving_time_mins % 60
round_trip_gas = gas_cost * 2

# Output: the report of what the trip is gonna cost and how long it is gonna be
print()
print("Destination:", destination)
print("Trip distance (miles):", miles)
print("Car's miles per gallon:", miles_per_gallon)
print("Gas price per gallon:", gas_price)
print("Number of people splitting the cost:", people)
print()
print("--- Trip to", destination, "---")
print("Gallons of gas:  ", gallons)
print("Gas cost:        ", gas_cost)
print("Cost per person: ", cost_per_person)
print("Driving time:    ", hours, "hr", leftover_minutes, "min (at 55 mph)")
print("Round trip gas:  $", round_trip_gas)
