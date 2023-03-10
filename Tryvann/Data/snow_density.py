# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
snow_density = pd.read_csv('snow_density.csv', header=0, names=['depth','density'])
snow_density_2 = pd.read_csv('snow_density_2.csv', header=0, names=['depth','density'])

# make plots pretty <3  
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'whitesmoke'

# Plot of snow density
fig = plt.figure()
fig.supxlabel('Density [kg/m^3]')
fig.supylabel('Depth [cm]')
fig.suptitle('Density in snow pack')

plt.subplot(1,2,2)
plt.plot(snow_density['density'],snow_density['depth'],'c', label='Original')
plt.grid()
plt.legend()
plt.subplot(1,2,1)
plt.plot(snow_density_2['density'],snow_density_2['depth'],'--', label='Comparison')
plt.grid()
plt.legend()
plt.show()
