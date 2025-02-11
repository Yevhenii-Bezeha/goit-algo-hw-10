import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2

num_points = 100000

x_random = np.random.uniform(a, b, num_points)
y_random = np.random.uniform(0, max(f(x_random)), num_points)

points_under_curve = np.sum(y_random <= f(x_random))

area_monte_carlo = (points_under_curve / num_points) * (b - a) * max(f(x_random))

print(f"Integral using the Monte Carlo method: {area_monte_carlo}")

result, error = spi.quad(f, a, b)
print(f"Integral using scipy.quad: {result} with error {error}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Integration of f(x) = x^2 from {a} to {b}')
plt.grid()
plt.show()
