# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
mwe = pd.read_csv('mwe.csv', header=0, names=['depth','Water equivalents'])
mwe_2 = pd.read_csv('mwe_2.csv', header=0, names=['depth','Water equivalents'])

# make plots pretty <3  
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'whitesmoke'

# Plot of snow density
fig = plt.figure()
fig.supxlabel('Water equivalents [m]')
fig.supylabel('Depth [cm]')
fig.suptitle('Water equivalents in snow pack')

plt.subplot(1,2,2)
plt.plot(mwe['Water equivalents'],mwe['depth'],'c', label='Original')
plt.grid()
plt.legend()
plt.subplot(1,2,1)
plt.plot(mwe_2['Water equivalents'],mwe_2['depth'],'--', label='Comparison')
plt.grid()
plt.legend()
plt.show()