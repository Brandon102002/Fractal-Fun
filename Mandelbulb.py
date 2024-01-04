import numpy as np
from mayavi import mlab

size = 2
density = 32

# Create the figure with a black background
#mlab.figure(bgcolor=(0, 0, 0))

# Plot each voxel as a point
#mlab.points3d(x, y, z, mode='cube', color=(1, 1, 1), scale_factor=1)

# Display the figure
#mlab.show()

x = np.linspace(-0.5*size, 0.5*size, num=density)
y = np.linspace(-0.5*size, 0.5*size, num=density)
z = np.linspace(-0.5*size, 0.5*size, num=density)

print(f"x = {x} \n y = {y} \n z = {z}")

r = np.zeros((density, density, density))
theta = np.zeros((density, density, density))
phi = np.zeros((density, density, density))

for i in range(density):
    for k in range(density):
        for j in range(density):
            print(f"i = {i}, j = {j}, k = {k}")
            print(f"[{x[i]}, {y[j]}, {z[k]}]")

            r[i, j, k] = np.sqrt(x[i]**2 + y[j]**2 + z[k]**2)
            theta[i, j, k] = np.arctan2(sqrt(x[i]**2 + y[j]**2), z[k])
            phi[i, j, k] = np.arctan2(y[j], z[k])
            