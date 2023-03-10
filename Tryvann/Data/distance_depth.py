# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Get data
distance_depth = pd.read_csv("distance_depth.csv", header=0, names=['depth','distance'])
distance_depth_2 = pd.read_csv("distance_depth_2.csv", header=0, names=['depth','distance'])

# make plots pretty <3  
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'whitesmoke'

# Plot of my snow distance 
plt.plot(distance_depth["depth"],distance_depth["distance"],'c')
plt.plot(distance_depth_2["depth"],distance_depth_2["distance"],'--')
plt.ylabel("Depth [cm]")
plt.xlabel("Distance [m]")
plt.grid()
plt.legend(['Original','Comparison'])
plt.title("Depth of snow transect")
plt.show()