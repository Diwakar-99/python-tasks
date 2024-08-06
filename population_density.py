# List of cities with their populations and areas
cities = [
    ("CityA", 500000, 100),   # (City Name, Population, Area)
    ("CityB", 800000, 150),
    ("CityC", 300000, 50),
    ("CityD", 1200000, 200),
    ("CityE", 400000, 80)
]

# Dictionary to store population density for each city
population_density = {}

# Calculate population density for each city
for city in cities:
    city_name, population, area = city
    density = population / area  # Calculate density
    population_density[city_name] = density  # Store in the dictionary

# Find the city with the highest population density
highest_city = max(population_density, key=population_density.get)
highest_density = population_density[highest_city]

# Print population densities for each city
print("Population Density of Cities:")
for city_name, density in population_density.items():
    print(f"{city_name}: {density:.2f} people per unit area")

# Print the city with the highest population density
print(f"\nCity with the highest population density: {highest_city} with a density of {highest_density:.2f} people per unit area")
 
