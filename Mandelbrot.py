import matplotlib.pyplot as plt
import numpy as np
np.warnings.filterwarnings("ignore")

# Mandelbrot set: z_0 = 0; z_(n+1) = z_n^2 + c

# recursive
def z(n, c):
    return 0 if n==0 else z(n-1, c)**2 + c

# iterative
def sequence(c):
    z = 0
    while True:
        yield z
        z = z**2 + c

# Creates a square 2D matrix of complex values to test
def complex_matrix_gen(x_min, x_max, y_min, y_max, pixels):
    reals = np.linspace(x_min, x_max, int((x_max - x_min) * pixels))
    imaginary = np.linspace(y_min, y_max, int((y_max - y_min) * pixels)) * 1j
    return reals[np.newaxis, :] + imaginary[:, np.newaxis]

def stable(c, num_iterations) -> bool:
    z = 0
    for _ in range(num_iterations):
        z = z**2 + c
    return abs(z) <= 2

num_pixels = 2**10
#num_pixels = 2**12

c = complex_matrix_gen(-2, 0.5, -1.5, 1.5, num_pixels)
plt.imshow(stable(c, num_iterations=20), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()