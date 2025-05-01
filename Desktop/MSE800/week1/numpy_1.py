import numpy as np

temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

average_temp = np.mean(temperatures)
print("Average temperature:", average_temp)

highest_temp = np.max(temperatures)
lowest_temp = np.min(temperatures)
print("Highest temperature:", highest_temp)
print("Lowest temperature:", lowest_temp)

temperatures_f = temperatures * 9/5 + 32
print("Temperatures in Fahrenheit:", temperatures_f)

above_20_indices = np.where(temperatures > 20)[0]
print("Days with temperature > 20°C (indices):", above_20_indices)
