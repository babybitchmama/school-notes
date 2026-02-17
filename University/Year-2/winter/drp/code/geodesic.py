import numpy as np
import matplotlib.pyplot as plt


def plot_dual_patch_geodesic(z0, z1, points=500):
    # Setup the figure with two subplots: z-disk and w-disk
    _, (ax_z, ax_w) = plt.subplots(1, 2, figsize=(12, 6))

    # Draw unit boundaries for both
    theta = np.linspace(0, 2*np.pi, 200)
    for ax in [ax_z, ax_w]:
        ax.plot(np.cos(theta), np.sin(theta), 'k--', color="k", lw=1, alpha=0.5)
        ax.set_aspect('equal')
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        ax.grid(True, linestyle=':', alpha=0.6)

    ax_z.set_title(r"Patch $z$ ($|z| \leq 1$)")
    ax_w.set_title(r"Patch $w = 1/z$ ($|w| \leq 1$)")

    # 1. Map to Sphere
    def to_sphere(z):
        mag_sq = np.abs(z)**2
        return np.array([2*z.real, 2*z.imag, 1-mag_sq]) / (1+mag_sq)

    p0, p1 = to_sphere(z0), to_sphere(z1)

    # 2. Generate FULL Geodesic (0 to 2*pi)
    # We find an orthogonal basis on the plane of the great circle
    v1 = p0 / np.linalg.norm(p0)
    v2 = p1 - np.dot(p1, v1) * v1
    v2 /= np.linalg.norm(v2)

    t = np.linspace(0, 2*np.pi, points)
    sphere_pts = np.cos(t)[:, None] * v1 + np.sin(t)[:, None] * v2

    # 3. Project to complex coordinates
    # z = (x + iy) / (1 + z_coord) is the standard stereographic from South Pole
    x, y, z_c = sphere_pts[:, 0], sphere_pts[:, 1], sphere_pts[:, 2]
    z_vals = (x + 1j*y) / (1 + z_c)

    # 4. Filter and Plot
    mask_z = np.abs(z_vals) <= 1.001 # Points in z-disk
    mask_w = np.abs(z_vals) >= 0.999 # Points in w-disk (where |1/z| <= 1)

    # Plot on Z-chart
    ax_z.plot(z_vals[mask_z].real, z_vals[mask_z].imag, 'r-', lw=2, label='Geodesic')

    # Plot on W-chart (transform z -> 1/z)
    w_vals = 1 / z_vals[mask_w]
    ax_w.plot(w_vals.real, w_vals.imag, 'b-', lw=2, label='Geodesic (1/z)')

    # Mark original points
    if np.abs(z0) <= 1: ax_z.scatter(z0.real, z0.imag, color='green', zorder=5)
    else: ax_w.scatter((1/z0).real, (1/z0).imag, color='green', zorder=5)

    plt.tight_layout()
    plt.show()

# Example: A geodesic that clearly crosses the boundary
plot_dual_patch_geodesic(complex(0.5, 0.1), complex(1.5, 0.8))
