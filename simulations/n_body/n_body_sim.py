"""
Cosmos Engine — N-Body Gravitational Simulation
=================================================
A simple N-body gravitational simulator using
velocity Verlet integration.

Author: Saheb Karami
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11  # Gravitational constant


class Body:
    """A celestial body with mass, position, and velocity."""

    def __init__(self, name: str, mass: float, position: np.ndarray, velocity: np.ndarray):
        self.name = name
        self.mass = mass
        self.pos = position.astype(np.float64)
        self.vel = velocity.astype(np.float64)
        self.acc = np.zeros(3, dtype=np.float64)


class NBodySimulation:
    """N-body gravitational simulation."""

    def __init__(self, bodies: list, dt: float = 3600):
        self.bodies = bodies
        self.dt = dt
        self.time = 0
        self.history = {b.name: [b.pos.copy()] for b in bodies}

    def compute_accelerations(self):
        """Compute gravitational acceleration for each body."""
        for b in self.bodies:
            b.acc = np.zeros(3)
        for i, b1 in enumerate(self.bodies):
            for j, b2 in enumerate(self.bodies):
                if i == j:
                    continue
                r = b2.pos - b1.pos
                dist = np.linalg.norm(r)
                if dist < 1e6:
                    dist = 1e6
                b1.acc += G * b2.mass * r / dist**3

    def step(self):
        """Advance simulation by one time step (velocity Verlet)."""
        for b in self.bodies:
            b.vel += 0.5 * b.acc * self.dt
        for b in self.bodies:
            b.pos += b.vel * self.dt
        self.compute_accelerations()
        for b in self.bodies:
            b.vel += 0.5 * b.acc * self.dt
        self.time += self.dt
        for b in self.bodies:
            self.history[b.name].append(b.pos.copy())

    def run(self, n_steps: int):
        """Run simulation for n_steps."""
        self.compute_accelerations()
        for _ in range(n_steps):
            self.step()

    def plot(self, save_path: str = None):
        """Plot the trajectories of all bodies."""
        fig, ax = plt.subplots(figsize=(10, 10), facecolor='#0a0a1a')
        ax.set_facecolor('#0a0a1a')
        colors = ['#FFD700', '#4FC3F7', '#FF6F00', '#E91E63', '#76FF03', '#B388FF']
        for i, (name, positions) in enumerate(self.history.items()):
            positions = np.array(positions)
            color = colors[i % len(colors)]
            ax.plot(positions[:, 0] / 1e9, positions[:, 1] / 1e9,
                    color=color, alpha=0.4, linewidth=0.8)
            ax.scatter(positions[-1, 0] / 1e9, positions[-1, 1] / 1e9,
                       color=color, s=100, label=name, zorder=5,
                       edgecolors='white', linewidth=0.5)
        ax.set_xlabel('X (x10^9 m)', color='white', fontsize=12)
        ax.set_ylabel('Y (x10^9 m)', color='white', fontsize=12)
        ax.set_title('N-Body Gravitational Simulation', color='white', fontsize=16, pad=20)
        ax.legend(loc='upper right', facecolor='#1a1a2e', edgecolor='white', labelcolor='white')
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('white')
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.1, color='white')
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150, facecolor='#0a0a1a')
            print(f"Plot saved to {save_path}")
        plt.show()


def solar_system_demo():
    """Run a simplified inner solar system simulation."""
    sun = Body('Sun', 1.989e30, np.array([0, 0, 0]), np.array([0, 0, 0]))
    mercury = Body('Mercury', 3.301e23, np.array([5.79e10, 0, 0]), np.array([0, 47_400, 0]))
    venus = Body('Venus', 4.867e24, np.array([1.082e11, 0, 0]), np.array([0, 35_020, 0]))
    earth = Body('Earth', 5.972e24, np.array([1.496e11, 0, 0]), np.array([0, 29_780, 0]))
    mars = Body('Mars', 6.417e23, np.array([2.279e11, 0, 0]), np.array([0, 24_130, 0]))

    sim = NBodySimulation([sun, mercury, venus, earth, mars], dt=3600 * 6)
    print("Running inner solar system simulation...")
    sim.run(n_steps=1460)  # ~1 year
    print(f"   Simulated time: {sim.time / (3600*24*365):.2f} years")
    sim.plot('simulations/n_body/solar_system_trajectories.png')


if __name__ == '__main__':
    solar_system_demo()
