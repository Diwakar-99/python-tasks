# List of temperatures in Celsius
celsius_temps = [20, 22, 25, 18, 30, 27, 23]

fahrenheit_temps = []

for temp in celsius_temps:
    fahrenheit_temps.append((temp * 9/5) + 32)

# Calculate the average temperature in Fahrenheit
average_fahrenheit = sum(fahrenheit_temps) / len(fahrenheit_temps)

# Print the results
print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("Average temperature in Fahrenheit:", average_fahrenheit)
 
