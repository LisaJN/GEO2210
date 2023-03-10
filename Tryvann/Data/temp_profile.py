# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
snow_temp = pd.read_csv("snow_temp.csv", header=0, names=['depth','temp'])
snow_temp_2 = pd.read_csv("snow_temp_2.csv", header=0, names=['depth','temp'])

# make plots pretty <3  
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'whitesmoke'

# Plot temperature profile
fig = plt.figure()
fig.supxlabel('Temperature [C]')
fig.supylabel('Depth [cm]')
fig.suptitle('Temperature change in snow pack')

plt.subplot(1,2,2)
plt.plot(snow_temp['temp'],snow_temp['depth'],'c', label='Original')
plt.grid()
plt.legend()
plt.subplot(1,2,1)
plt.plot(snow_temp_2['temp'],snow_temp_2['depth'],'--', label='Comparison')
plt.grid()
plt.legend()
plt.show()