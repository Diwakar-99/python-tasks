# Problem: Calculate and print the average temperature for a week based on user input.

total_temp = 0
for i in range(1, 8):
    individual_temp = int(input(f"Enter day {i} temperature: "))
    total_temp += individual_temp

average_temp = total_temp / 7

print("Average temperature for the week: ", average_temp)
