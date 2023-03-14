# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
stratigraphy = pd.read_csv("stratigraphy.csv", header=0, names=['depth','roughness'])
stratigraphy_2 = pd.read_csv("stratigraphy_2.csv", header=0, names=['depth','roughness'])

# make plots pretty <3  
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'whitesmoke'

# Plot temperature profile
fig = plt.figure()
fig.supxlabel('Roughness')
fig.supylabel('Depth [cm]')
fig.suptitle('Stratigraphy')

plt.subplot(1,2,2)
plt.plot(stratigraphy['roughness'],stratigraphy['depth'],'c', label='Original')
plt.grid()
plt.legend()
plt.subplot(1,2,1)
plt.plot(stratigraphy_2['roughness'],stratigraphy_2['depth'],'--', label='Comparison')
plt.grid()
plt.legend()
plt.show()