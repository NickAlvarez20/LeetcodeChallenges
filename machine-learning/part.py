import numpy as np
import matplotlib.pyplot as plt


class MiniCollider:
    def __init__(self, radius=100):
        self.radius = radius
        # Particle 1: Starts at Top (0, 100)
        self.p1_pos = np.array([0.0, float(radius)])
        # Particle 2: Starts at Bottom (0, -100)
        self.p2_pos = np.array([0.0, -float(radius)])

    def step(self):
        # Update positions to orbit the center (Clockwise vs Counter-Clockwise)
        # We recalculate velocity every step to stay perfectly on the circle
        for i, pos in enumerate([self.p1_pos, self.p2_pos]):
            # Rotation math: x' = x*cos(theta) - y*sin(theta)
            # 0.1 is the speed of the orbit
            angle = 0.1 if i == 0 else -0.1
            c, s = np.cos(angle), np.sin(angle)
            j = np.array([[c, -s], [s, c]])

            if i == 0:
                self.p1_pos = np.dot(j, self.p1_pos)
            else:
                self.p2_pos = np.dot(j, self.p2_pos)

    def detect_collision(self):
        distance = np.linalg.norm(self.p1_pos - self.p2_pos)
        # If they are within 15 units of each other, they SMASH
        if distance < 15.0:
            return True, 20.0  # High energy release
        return False, 0


def show_debris(energy):
    num_particles = int(energy * 15)
    angles = np.random.uniform(0, 2 * np.pi, num_particles)
    speeds = np.random.exponential(scale=energy, size=num_particles)

    dx = np.cos(angles) * speeds
    dy = np.sin(angles) * speeds

    plt.figure(figsize=(8, 8))
    plt.style.use("dark_background")
    plt.scatter(dx, dy, c=speeds, cmap="plasma", s=15, alpha=0.9)
    plt.title(f"PARTICLE COLLISION EVENT: {energy} GeV")
    plt.show()


# --- RUN EXPERIMENT ---
lhc = MiniCollider(radius=100)
print("Particles entering the ring...")

for i in range(200):
    lhc.step()
    hit, energy = lhc.detect_collision()

    if hit:
        print(f"💥 HIT DETECTED AT STEP {i}")
        show_debris(energy)
        break
