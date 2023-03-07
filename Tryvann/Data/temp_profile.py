# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
snow_temp = pd.read_csv("snow_temp.csv", header=0, names=['depth','temp'])

# Plot of snow temperature
plt.plot(snow_temp["temp"],snow_temp["depth"])
plt.xlabel("Temperature")
plt.ylabel("Depth")
plt.grid()
plt.title("Temperature as a fuction of depth")
plt.show()
