# initialize the lists to store the miles and gallons for each trip
mileage_list = []
gallons_list = []
tank_capacity_list = []
car_make_model_list = []

while True:
    unit = input(
        "Enter your preferred unit of measurement (mpg, km/L, or L/100km): ")
    if unit in ("mpg", "km/L", "L/100km"):
        break
    else:
        print("Invalid unit of measurement. Please try again.")

while True:
    try:
        miles_driven = float(input("Enter the number of miles driven: "))

        if miles_driven == -1:
            break

        gallons_used = float(
            input("Enter the number of gallons of gas used: "))
        tank_capacity = float(input("Enter the tank capacity of your car: "))
        car_make_model = input("Enter the make and model of your car: ")

        # add the data to the lists
        mileage_list.append(miles_driven)
        gallons_list.append(gallons_used)
        tank_capacity_list.append(tank_capacity)
        car_make_model_list.append(car_make_model)

        break

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# calculate the fuel efficiency in miles per gallon
mpg = miles_driven / gallons_used
mpg_list = [mileage_list[i] / gallons_list[i]
            for i in range(len(mileage_list))]

average_mpg = sum(mileage_list) / sum(gallons_list)

# convert to the preferred unit of measurement
if unit == "km/L":
    fuel_efficiency = mpg * 0.425144
    unit_string = "km/L"
elif unit == "L/100km":
    fuel_efficiency = 235.214583 / mpg
    unit_string = "L/100km"
elif unit == "mpg":
    fuel_efficiency = mpg
    unit_string = "mpg"


# display the result
print("Your car's fuel efficiency is", round(fuel_efficiency, 2), unit_string)

# display the results
for i in range(len(mileage_list)):
    print("Trip", i+1, "fuel efficiency:", round(mpg_list[i], 2), "mpg")

print("Average fuel efficiency:", round(average_mpg, 2), "mpg")


# calculate the fuel efficiency for each trip in liters per 100 km
l_per_100km_list = [100 * gallons_list[i] /
                    (mileage_list[i] * 1.60934) for i in range(len(mileage_list))]

# calculate the average fuel efficiency across all trips
total_miles = sum(mileage_list)
total_gallons = sum(gallons_list)
average_fuel_efficiency = 100 * total_gallons / (total_miles * 1.60934)

# display the results for each trip
for i in range(len(mileage_list)):
    print("Trip", i+1)
    print("Car make and model:", car_make_model_list[i])
    print("Tank capacity:", tank_capacity_list[i], "gallons")
    print("Miles driven:", mileage_list[i])
    print("Gallons used:", gallons_list[i])
    print("Fuel efficiency:", round(
        l_per_100km_list[i], 2), "liters per 100 km")

# display the average fuel efficiency across all trips
print("\nAverage fuel efficiency:", round(
    average_fuel_efficiency, 2), "liters per 100 km")
