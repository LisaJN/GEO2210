# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
snow_density = pd.read_csv('snow_density.csv', header=0, names=['depth','density'])
snow_density_2 = pd.read_csv('snow_density_2.csv', header=0, names=['depth','density'])


# Plot of snow density
plt.plot(snow_density['density'],snow_density['depth'],'c')
plt.plot(snow_density_2['density'],snow_density_2['depth'],'--')
plt.xlabel('Density [kg/m^3]')
plt.ylabel('Depth [cm]')
plt.grid()
plt.legend(['Original','Comparison'])
plt.title('Density in snow pack')
plt.show()