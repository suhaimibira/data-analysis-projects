# 1. Declare and assign the variables here:
shuttle_name = 'Determination'
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 38400
MILES_PER_KM = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(MILES_PER_KM))

# Code your solution to exercises 3 and 4 here:

miles_to_mars = (distance_to_mars_km)*(MILES_PER_KM)
hours_to_mars = (miles_to_mars)/(shuttle_speed_mph)
days_to_mars = (hours_to_mars)/(24)

print(f"Distance to Mars in miles: {miles_to_mars}")
print(f"Time to Mars in hours: {hours_to_mars}")
print(f"Time to Mars in days: {days_to_mars}")

print('Determination will take 333 days to reach Mars.')

# Code your solution to exercise 5 here

miles_to_moon = distance_to_moon_km * MILES_PER_KM
hours_to_moon = miles_to_moon /shuttle_speed_mph
days_to_moon = hours_to_moon/ 24

print(f"Distance to Moon in miles: {miles_to_moon}")
print(f"Time to Moon in hours: {hours_to_moon}")
print(f"Time to Moon in days: {days_to_moon}")

print('Determination will take 0.06 days to reach the Moon.')
