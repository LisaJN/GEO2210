# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
mwe = pd.read_csv('mwe.csv', header=0, names=['depth','Water equivalents'])
mwe_2 = pd.read_csv('mwe_2.csv', header=0, names=['depth','Water equivalents'])

# Plot of snow density
plt.plot(mwe['Water equivalents'],mwe['depth'],'c')
plt.plot(mwe_2['Water equivalents'],mwe_2['depth'],'--')
plt.xlabel('Water equivalents [m]')
plt.ylabel('Depth [cm]')
plt.grid()
plt.legend(['Original','Comparison'])
plt.title('Water equivalents in snow pack')
plt.show()