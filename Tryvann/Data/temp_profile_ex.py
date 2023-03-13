# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
snow_temp = pd.read_csv("snow_temp.csv", header=0, names=['depth','temp'])
snow_temp_3 = pd.read_csv("snow_temp_3.csv", header=0, names=['depth','temp'])

# make plots pretty <3  
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'whitesmoke'

# Plot temperature profile
plt.plot(snow_temp['temp'],snow_temp['depth'],'c', label='Original')
plt.plot(snow_temp_3['temp'],snow_temp_3['depth'],'--', label='Example')
plt.xlabel('Temperature [C]')
plt.ylabel('Depth [cm]')
plt.title('Example of temperature profile after a cold night')
plt.grid()
plt.legend()
plt.show()