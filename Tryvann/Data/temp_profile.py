# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
snow_temp = pd.read_csv("snow_temp.csv", header=0, names=['depth','temp'])
snow_temp_2 = pd.read_csv("snow_temp_2.csv", header=0, names=['depth','temp'])

# Plot temperature profile
plt.plot(snow_temp['temp'],snow_temp['depth'],'c')
plt.plot(snow_temp_2['temp'],snow_temp_2['depth'],'--')
plt.xlabel("Temperature")
plt.ylabel("Depth")
plt.grid()
plt.legend(['Original','Comparison'])
plt.title("Temperature as a fuction of depth")
plt.show()
