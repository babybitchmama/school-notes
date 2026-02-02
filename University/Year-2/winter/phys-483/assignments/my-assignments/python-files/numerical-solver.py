import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
M = 1.0       # mass
b = 0.1       # extra term in metric
epsilon = 0.95  # energy
ell = 3.0     # angular momentum

def V_eff(r, L, M, b):
    """Effective potential for timelike particle."""
    return (1 - 2*M/r + b/r**2) * (1 + L**2 / r**2)

def geodesic_equations(tau, y, L, M, b):
    r, phi = y
    dr_dtau = np.sqrt(epsilon**2 - V_eff(r, L, M, b))
    dphi_dtau = L / r**2
    return [dr_dtau, dphi_dtau]

# Initial conditions
r0 = 6.0
phi0 = 0.0
y0 = [r0, phi0]

# Integrate
tau_span = (0, 50)
sol = solve_ivp(lambda tau, y: geodesic_equations(tau, y, ell, M, b),
                tau_span, y0, max_step=0.01)

# Convert to Cartesian coordinates for plotting
r = sol.y[0]
phi = sol.y[1]
x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Timelike geodesic trajectory")
plt.axis('equal')

# save file to image-files/timelike-geodesic.png
plt.savefig("image-files/timelike-geodesic.png")

plt.show()
