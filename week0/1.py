import numpy as np

# Temperatures in Celsius for the week
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# 1. Calculate the average temperature for the week
average_temp = np.mean(temperatures)

# 2. Find the highest and lowest temperature recorded
highest_temp = np.max(temperatures)
lowest_temp = np.min(temperatures)

# 3. Convert all temperatures to Fahrenheit
temperatures_fahrenheit = (temperatures * 9/5) + 32

# 4. Identify the days (indices) where the temperature was above 20°C
days_above_20 = np.where(temperatures > 20)[0]

# Print the results
print(f"Average temperature for the week: {average_temp:.2f}°C")
print(f"Highest temperature recorded: {highest_temp}°C")
print(f"Lowest temperature recorded: {lowest_temp}°C")
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
print(f"Days where the temperature was above 20°C: {days_above_20}")
