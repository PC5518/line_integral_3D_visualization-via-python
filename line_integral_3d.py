import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function f(x, y) = x^2 + y^2
def f(x, y):
    return x**2 + y**2

# Parametrize the curve y = x^2
t = np.linspace(-1, 1, 300)
x = t
y = t**2
z = f(x, y)

# Calculate arc length element ds = sqrt((dx)^2 + (dy)^2)
dx = np.gradient(x)
dy = np.gradient(y)
ds = np.sqrt(dx**2 + dy**2)

# Line integral = sum of f(x, y) * ds
line_integral = np.sum(z * ds)
print(f"Line integral of f(x,y) along y = x^2 from x=-1 to x=1: {line_integral:.4f}")

# Create the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Surface
X = np.linspace(-1.2, 1.2, 50)
Y = np.linspace(-0.2, 1.4, 50)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
ax.plot_surface(X, Y, Z, alpha=0.5, cmap='Reds', edgecolor='k')

# Plot curve on ground
ax.plot(x, y, 0*z, 'b--', label="Curve on XY plane")

# Plot lifted curve on surface
ax.plot(x, y, z, 'b', linewidth=3, label="Lifted curve on surface")

# Plot vertical lines (ribbon edges)
for i in range(0, len(t), 10):
    ax.plot([x[i], x[i]], [y[i], y[i]], [0, z[i]], color='gray', linewidth=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Line Integral of f(x, y)=x^2+y^2 along y = x²')
ax.legend()
plt.tight_layout()
plt.show()
