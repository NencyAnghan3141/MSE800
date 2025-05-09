import pandas as pd
import matplotlib.pyplot as plt

# Load data
auckland = pd.read_csv("Auckland_temperature.csv")
christchurch = pd.read_csv("Christchurch_temperature.csv")

# Ensure correct datetime and sorting
auckland['Month'] = pd.to_datetime(auckland['Month'])
christchurch['Month'] = pd.to_datetime(christchurch['Month'])

# Set month as index for plotting
auckland.set_index('Month', inplace=True)
christchurch.set_index('Month', inplace=True)

# Optional: If there's a 'Temperature' column
plt.figure(figsize=(10, 6))
plt.plot(auckland.index, auckland['Temperature'], label='Auckland')
plt.plot(christchurch.index, christchurch['Temperature'], label='Christchurch')

plt.title("Monthly Average Temperatures - Auckland vs Christchurch")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
