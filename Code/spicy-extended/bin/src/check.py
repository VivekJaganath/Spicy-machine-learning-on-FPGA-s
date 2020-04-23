import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#defining figure and size
fig, ax = plt.subplots(figsize=(10, 10))

#declating lists for values in the dataset starting position (x,y,z) and relative movement (u,v,w)
#since z and w are null ignoring them
X, Y, U, V, N = [],[],[],[],[]

#Open the file and readlines
with open("C:\\Users\\Vivek\Desktop\\2020-vivek-jaganath\\Code\\spicy-extended\\bin\\src\\field2.irreg.txt", "r") as f:
    rows = f.readlines()[6:] #ignoring the firts 6 values to get consistent plotting and to avoind indexing while itterating over elements
for line in rows:
    J = line.split(" ")
    X.append(float(J[0])) #filling the list with values from dataset
    Y.append(float(J[1]))
    U.append(float(J[3]))
    V.append(float(J[4]))
x1 = np.asarray(X) #converting the list to numpy array to easily work on even larger datasets
y1 = np.asarray(Y)
u1 = np.asarray(U)
v1 = np.asarray(V)

for i in range(len(u1)):
    N.append(np.sqrt(u1[i]**2)+(v1[i]**2)) #calculating the length of vectors as discussed in the lectures
n1 = np.asarray(N)

#Plotting the values
#refrence 1: https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.15-Quiver-and-Stream-Plots/
#reference 2: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.colorbar.html
#reference 3: https://jakevdp.github.io/PythonDataScienceHandbook/04.07-customizing-colorbars.html
plt.quiver(x1, y1, u1, v1, n1, scale=6)
ax.set_title('Direction of Water in Tunnel')
ax.set_aspect('equal')
plt.axis([0, 1, 0, 1])
cax = fig.add_axes([0.78,0.078,0.01,0.85])
cbx = mpl.colorbar.ColorbarBase(cax, orientation = 'vertical')
cbx.set_ticks([0,0.5,1])
cbx.set_ticklabels(['Low', 'Medium', 'High'])
cbx.set_label('Velocity of water in tunnel')
plt.tight_layout()
plt.show()